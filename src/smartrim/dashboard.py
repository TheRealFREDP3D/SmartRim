import glob
import json
import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from smartrim.config import (
    ALERTS_DIR,
    BASE_DIR,
    MCP_DELAY,
    MCP_URL,
    RUN_ID,
    SNAPSHOTS_DIR,
)

try:
    from smartrim.mcp_client import McpError
except ImportError:
    McpError = Exception

# Page configuration
st.set_page_config(
    page_title="SmartRim Command Center",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .status-urgent { color: #dc2626; font-weight: bold; }
    .status-warning { color: #f59e0b; font-weight: bold; }
    .status-info { color: #3b82f6; }
    .alert-banner-urgent {
        background: #fee2e2; border-left: 6px solid #dc2626;
        padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;
        font-size: 1.1rem; color: #111827;
    }
    .alert-banner-ok {
        background: #dcfce7; border-left: 6px solid #16a34a;
        padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;
        font-size: 1.1rem; color: #111827;
    }
    .colonist-card {
        background: #f8fafc; border: 1px solid #e2e8f0;
        padding: 0.75rem; border-radius: 0.5rem; margin-bottom: 0.5rem;
        color: #111827;
    }
    .big-metric { font-size: 2rem; font-weight: bold; }
    .compact { font-size: 0.85rem; line-height: 1.2; }
    .stMarkdown p { margin-bottom: 0.25rem; }
    section.main > div { padding-top: 0.25rem; }
    header[data-testid="stHeader"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .block-container { padding-top: 0.5rem; padding-bottom: 0.5rem; }
</style>
""", unsafe_allow_html=True)


# ---------- Data loading ----------

@st.cache_data(ttl=5)
def load_current_alerts():
    alert_path = os.path.join(ALERTS_DIR, "current.json")
    if os.path.exists(alert_path):
        with open(alert_path, encoding='utf-8') as f:
            return json.load(f)
    return []


@st.cache_data(ttl=30)
def load_all_advice():
    advice_path = os.path.join(BASE_DIR, "memory", "advice", "advice.jsonl")
    advice_list = []
    if os.path.exists(advice_path):
        with open(advice_path, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    advice_list.append(json.loads(line))
    return advice_list


@st.cache_data(ttl=60)
def load_lessons():
    lessons_path = os.path.join(BASE_DIR, "memory", "lessons.jsonl")
    lessons_list = []
    if os.path.exists(lessons_path):
        with open(lessons_path, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    lessons_list.append(json.loads(line))
    return lessons_list


@st.cache_data(ttl=60)
def load_runs_metadata():
    runs_dir = os.path.join(BASE_DIR, "memory", "runs")
    runs = []
    if os.path.exists(runs_dir):
        for file in glob.glob(os.path.join(runs_dir, "*.end.json")):
            with open(file, encoding='utf-8') as f:
                runs.append(json.load(f))
    return runs


@st.cache_data(ttl=60)
def load_run_snapshots(run_id):
    snapshot_dir = os.path.join(SNAPSHOTS_DIR, run_id)
    snapshots = []
    if os.path.exists(snapshot_dir):
        for file in glob.glob(os.path.join(snapshot_dir, "day-*.json")):
            with open(file, encoding='utf-8') as f:
                snapshots.append(json.load(f))
        snapshots.sort(key=lambda x: x.get('day', ''))
    return snapshots


@st.cache_data(ttl=60)
def load_debriefs():
    debriefs_dir = os.path.join(BASE_DIR, "memory", "debriefs")
    debriefs = []
    if os.path.exists(debriefs_dir):
        for file in glob.glob(os.path.join(debriefs_dir, "*.md")):
            with open(file, encoding='utf-8') as f:
                debriefs.append({'filename': os.path.basename(file), 'content': f.read()})
    return debriefs


@st.cache_data(ttl=10)
def load_reflex_actions(limit=8):
    path = os.path.join(BASE_DIR, "memory", "actions.jsonl")
    out = []
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    out.reverse()
    return out[:limit]


def get_live_game_state():
    try:
        from smartrim.mcp_client import McpClient
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        status = client.call_tool("get_status")
        if status and not status.get("error"):
            return status
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError) as e:
        st.error(f"Failed to connect to MCP server: {e}")
    return None


@st.cache_data(ttl=8)
def fetch_colonists():
    try:
        from smartrim.mcp_client import McpClient
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        return client.call_tool("list_colonists")
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError):
        return None


@st.cache_data(ttl=8)
def fetch_resources():
    try:
        from smartrim.mcp_client import McpClient
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        return client.call_tool("get_resources")
    except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError):
        return None


def mood_color(mood):
    try:
        m = float(mood)
    except (TypeError, ValueError):
        return "#6b7280"
    if m < 5:
        return "#dc2626"
    if m < 20:
        return "#f59e0b"
    if m < 35:
        return "#eab308"
    return "#16a34a"


# ---------- Command Center (dense second-screen layout) ----------

def _reflex_enabled():
    return os.getenv("REFLEX_KILL", "1") != "1"


def _reflex_dry_run():
    return os.getenv("REFLEX_DRY_RUN", "1") != "0"


def _game_colonists(game_state):
    if not game_state:
        return []
    bundled = (game_state.get("bundled") or {}).get("list_colonists") or {}
    return bundled.get("colonists", []) or []


def _game_alerts(game_state):
    if not game_state:
        return [], []
    bundled = (game_state.get("bundled") or {}).get("get_alerts") or {}
    active = bundled.get("activeAlerts", []) or []
    recent_msgs = bundled.get("recentMessages", []) or []
    return active, recent_msgs


def command_center_body():
    game_state = get_live_game_state()
    sm_alerts = load_current_alerts()

    if not game_state:
        st.error("❌ Game Not Connected")

    # ---------- Alert banner ----------
    urgent = [a for a in sm_alerts if a.get("type") == "urgent"]
    warnings = [a for a in sm_alerts if a.get("type") == "warning"]
    if urgent:
        msgs = " · ".join(a.get("message", "") for a in urgent)
        st.markdown(f'<div class="alert-banner-urgent">🚨 {msgs}</div>', unsafe_allow_html=True)
    elif warnings:
        msgs = " · ".join(a.get("message", "") for a in warnings)
        st.markdown(f'<div class="alert-banner-urgent" style="background:#fef3c7;border-color:#f59e0b;">⚠️ {msgs}</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="alert-banner-ok">✅ All clear — no active alerts</div>', unsafe_allow_html=True)

    # ---------- Colonists (full width) ----------
    st.subheader("👥 Colonists")
    colonists = _game_colonists(game_state)[:8]
    if colonists:
        ccols = st.columns(4)
        for i, c in enumerate(colonists):
            name = c.get("name", "?")
            mood = c.get("mood", 0)
            health = c.get("health", 0)
            job = c.get("job", "")
            downed = c.get("downed", False)
            badge = " [DOWNED]" if downed else ""
            color = mood_color(mood)
            with ccols[i % 4]:
                st.markdown(
                    f'<div class="colonist-card">'
                    f'<b>{name}</b>{badge}<br>'
                    f'<span style="color:{color};font-weight:bold;">Mood {mood}%</span> · '
                    f'HP {health}%<br><small>{job}</small></div>',
                    unsafe_allow_html=True,
                )
    else:
        st.info("No colonist data.")

    # ---------- Resources (full width, under colonists) ----------
    st.subheader("📦 Resources")
    res_data = fetch_resources()
    resources = (res_data or {}).get("resources", []) if isinstance(res_data, dict) else []
    if resources:
        important = ["Meal", "Medicine", "Steel", "Wood", "Component", "Food", "Cloth", "Leather"]
        filtered = [r for r in resources
                    if any(k.lower() in str(r.get("label", "")).lower() for k in important)]
        if filtered:
            icon_map = {
                "steel": "steel.png", "wood": "wood.png", "medicine": "medicine.png",
                "component": "component.png", "cloth": "cloth.png", "leather": "leather.png",
                "food": "food.png", "meal": "food.png",
            }
            def _icon_for(label):
                low = str(label).lower()
                for key, fn in icon_map.items():
                    if key in low:
                        return os.path.join(os.path.dirname(__file__), "assets", "icons", fn)
                return None
            rcols = st.columns(8)
            for i, r in enumerate(filtered[:8]):
                label = r.get("label", "?")
                count = r.get("count", 0)
                with rcols[i % 8]:
                    ipath = _icon_for(label)
                    if ipath and os.path.exists(ipath):
                        st.image(ipath, width=28)
                    st.caption(f"{label}: {count}")
        else:
            st.info("No key resources.")
    else:
        st.info("No resource data.")

    # ---------- Alerts + Reflex | Lessons (two columns) ----------
    aleft, aright = st.columns([3, 2])
    with aleft:
        st.subheader("🚨 Live Alerts")
        active_game, _ = _game_alerts(game_state)
        for a in sm_alerts[:4]:
            sev = a.get("type", "info")
            icon = "🔴" if sev == "urgent" else "🟡" if sev == "warning" else "🟢"
            st.markdown(f"{icon} **{a.get('message','')}**  \n<small>{a.get('timestamp','')}</small>",
                        unsafe_allow_html=True)
        for ga in active_game[:4]:
            prio = ga.get("priority", "Medium")
            icon = "🔴" if prio == "High" else "🟡" if prio == "Medium" else "🟢"
            st.markdown(f"{icon} {ga.get('label','')}  \n<small>{ga.get('explanation','')[:120]}</small>",
                        unsafe_allow_html=True)
        if not sm_alerts and not active_game:
            st.info("No active alerts.")

        st.subheader("⏸ Why paused? / Reflex")
        if game_state and game_state.get("paused"):
            st.warning("Game is paused.")
        last_urgent = urgent[-1] if urgent else None
        if last_urgent:
            st.markdown(f"Last urgent: **{last_urgent.get('message','')}** at {last_urgent.get('timestamp','')[:16]}")
        ractions = load_reflex_actions(3)
        if ractions:
            ra = ractions[0]
            status = "dry-run" if ra.get("dry_run") else ("ok" if ra.get("success") else "failed")
            st.markdown(f"Last reflex: `{ra.get('action','?')}` — {status} ({ra.get('timestamp','')[:16]})")
            st.markdown(f"Would: {ra.get('would_do', ra.get('message',''))}")
        else:
            st.info("No reflex actions yet.")
        st.markdown(f"Reflex: {'enabled' if _reflex_enabled() else 'disabled'} · "
                    f"{'dry-run' if _reflex_dry_run() else 'LIVE writes'}")

    with aright:
        st.subheader("📚 Active Lessons")
        lessons = [ls for ls in load_lessons() if ls.get("status", "active") == "active"]
        lessons.sort(key=lambda x: (x.get("confidence") or 0), reverse=True)
        for ls in lessons[:5]:
            st.markdown(f"- **{ls.get('id','?')}** (conf {ls.get('confidence','?')})  \n  {ls.get('title','')}")
        if not lessons:
            st.info("No active lessons.")

    # ---------- Trends (full width) ----------
    st.subheader("📈 Trends")
    snapshots = load_run_snapshots(RUN_ID)
    if snapshots:
        tdata = []
        for snap in snapshots:
            s = snap.get("summary", {})
            tdata.append({
                "day": str(s.get("day", "?")),
                "mood": s.get("min_mood", 0),
                "food": s.get("food_days", 0),
                "wealth": s.get("wealth", 0),
            })
        tdf = pd.DataFrame(tdata)
        fig_mood = go.Figure()
        fig_mood.add_trace(go.Scatter(x=tdf["day"], y=tdf["mood"], name="Min mood", mode="lines+markers", fill="tozeroy", line={"color": "#16a34a"}))
        fig_mood.update_layout(height=140, margin={"l": 10, "r": 10, "t": 5, "b": 10},
                               yaxis={"title": "Mood", "range": [0, 100]},
                               xaxis={"tickangle": -30, "tickfont": {"size": 8}},
                               yaxis_tickfont={"size": 8})
        st.plotly_chart(fig_mood, use_container_width=True)

        fig_food = go.Figure()
        fig_food.add_trace(go.Scatter(x=tdf["day"], y=tdf["food"], name="Food days", mode="lines+markers", fill="tozeroy", line={"color": "#f59e0b"}))
        fig_food.update_layout(height=140, margin={"l": 10, "r": 10, "t": 5, "b": 10},
                               yaxis={"title": "Food days"},
                               xaxis={"tickangle": -30, "tickfont": {"size": 8}},
                               yaxis_tickfont={"size": 8})
        st.plotly_chart(fig_food, use_container_width=True)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=tdf["day"], y=tdf["wealth"], name="Wealth", mode="lines+markers", fill="tozeroy", line={"color": "#3b82f6"}))
        fig2.update_layout(height=120, margin={"l": 10, "r": 10, "t": 5, "b": 10},
                           xaxis={"tickangle": -30, "tickfont": {"size": 8}},
                           yaxis={"tickfont": {"size": 8}})
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No trend data yet.")

    # ---------- Bottom: streaming panels ----------
    st.divider()
    bleft, bright = st.columns(2)
    with bleft:
        st.subheader("🧾 Action Audit Log")
        ractions = load_reflex_actions(6)
        if ractions:
            for ra in ractions:
                status = "✅" if ra.get("success") else "🟡" if ra.get("dry_run") else "❌"
                st.markdown(f"{status} `{ra.get('timestamp','')[:16]}` {ra.get('action','?')}  \n<small>{ra.get('message','')}</small>",
                            unsafe_allow_html=True)
        else:
            st.info("No actions yet.")
    with bright:
        st.subheader("💬 In-Game Say Stream")
        _, recent_msgs = _game_alerts(game_state)
        if recent_msgs:
            for m in recent_msgs[:6]:
                st.markdown(f"`{m.get('tick','?')}` {m.get('text','')}")
        else:
            # Fall back to recent advice situations
            adv = sorted(load_all_advice(), key=lambda x: x.get("timestamp", ""), reverse=True)[:5]
            for a in adv:
                st.markdown(f"`{a.get('timestamp','')[:16]}` {a.get('situation','')}")
            if not adv:
                st.info("No messages yet.")

    # ---------- Quick actions ----------
    st.divider()
    q1, q2, q3, q4 = st.columns(4)
    with q1:
        if st.button("⏸ Pause Game", use_container_width=True):
            try:
                from smartrim import counselor as c
                st.write(c.pause())
            except Exception as e:
                st.error(str(e))
    with q2:
        if st.button("▶️ Resume Game", use_container_width=True):
            try:
                from smartrim import counselor as c
                st.write(c.resume())
            except Exception as e:
                st.error(str(e))
    with q3:
        if st.button("📋 Daily Summary", use_container_width=True):
            try:
                from smartrim import counselor as c
                st.write(c.daily_summary())
            except Exception as e:
                st.error(str(e))
    with q4:
        if st.button("🔄 Refresh Now", use_container_width=True):
            st.cache_data.clear()
            st.rerun()


# ---------- Existing tabs (kept) ----------

def live_monitor_tab():
    st.header("📡 Live Game Monitor")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with col2:
        game_connected = st.empty()
    with col3:
        run_id_display = st.empty()

    game_state = get_live_game_state()

    if game_state:
        game_connected.success("✅ Game Connected")
        run_id_display.info(f"Run ID: {RUN_ID}")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Days Passed", game_state.get('daysPassed', 0))
        with col2:
            st.metric("Colonists", game_state.get('colonistCount', 0))
        with col3:
            st.metric("Wealth", f"{game_state.get('wealthTotal', 0):,}")
        with col4:
            st.metric("Difficulty", game_state.get('difficulty', 'Unknown'))

        alerts = load_current_alerts()
        st.subheader("Current Alerts")
        if alerts:
            for alert in alerts:
                severity = alert.get('type', 'info')
                icon = "🚨" if severity == "urgent" else "⚠️" if severity == "warning" else "ℹ️"
                severity_class = f"status-{severity}"
                st.markdown(f"""
                <div class="metric-card">
                    <span class="{severity_class}">{icon} {severity.upper()}</span>: {alert.get('message', 'No message')}
                    <br><small>{alert.get('timestamp', '')}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No current alerts")

        try:
            from smartrim.mcp_client import McpClient
            client = McpClient(MCP_URL, delay=MCP_DELAY)
            colonists = client.call_tool("list_colonists")
            if colonists and colonists.get('colonists'):
                st.subheader("Colonists")
                colonist_df = pd.DataFrame(colonists['colonists'])
                display_cols = ['name', 'age', 'mood', 'health', 'job']
                available_cols = [col for col in display_cols if col in colonist_df.columns]
                if available_cols:
                    st.dataframe(colonist_df[available_cols], use_container_width=True)
        except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError) as e:
            st.warning(f"Could not load colonist data: {e}")

        try:
            from smartrim.mcp_client import McpClient
            client = McpClient(MCP_URL, delay=MCP_DELAY)
            resources = client.call_tool("get_resources")
            if resources and resources.get('resources'):
                st.subheader("Key Resources")
                res_df = pd.DataFrame(resources['resources'])
                important = ['Meal', 'Medicine', 'Steel', 'Wood', 'Component', 'Food']
                filtered = res_df[res_df['label'].str.contains('|'.join(important), case=False, na=False)]
                if not filtered.empty:
                    st.dataframe(filtered, use_container_width=True)
        except (McpError, ValueError, KeyError, TypeError, OSError, AttributeError) as e:
            st.warning(f"Could not load resource data: {e}")
    else:
        game_connected.error("❌ Game Not Connected")
        run_id_display.info(f"Run ID: {RUN_ID}")
        st.warning("Unable to connect to RimWorld MCP server. Make sure RimWorld is running with the RimMolt mod.")


def advice_browser_tab():
    st.header("📚 Advice Browser")
    advice_list = load_all_advice()
    if not advice_list:
        st.info("No advice records found.")
        return
    df = pd.DataFrame(advice_list)
    col1, col2, col3 = st.columns(3)
    with col1:
        run_filter = st.multiselect("Filter by Run ID", options=df['run_id'].unique(), default=df['run_id'].unique())
    with col2:
        severity_filter = st.multiselect("Filter by Severity", options=df['severity'].unique(), default=df['severity'].unique())
    with col3:
        status_filter = st.multiselect("Filter by Status", options=df['status'].unique(), default=df['status'].unique())
    filtered_df = df[df['run_id'].isin(run_filter) & df['severity'].isin(severity_filter) & df['status'].isin(status_filter)]
    st.metric("Total Advice Records", len(filtered_df))
    for _, row in filtered_df.iterrows():
        with st.expander(f"{row['timestamp']} - {row['severity'].upper()} - {row['trigger']}"):
            st.markdown(f"**Situation:** {row.get('situation', 'N/A')}")
            st.markdown(f"**Status:** {row.get('status', 'N/A')}")
            if row.get('risks'):
                st.markdown("**Risks:**")
                for risk in row['risks']:
                    st.markdown(f"- {risk.get('label', '')} ({risk.get('severity', '')})")
            if row.get('actions'):
                st.markdown("**Recommended Actions:**")
                for action in row['actions']:
                    st.markdown(f"- {action.get('action', '')} (Rank: {action.get('rank', 'N/A')})")
                    st.markdown(f"  *Rationale:* {action.get('rationale', 'N/A')}")
            if row.get('linked_lessons'):
                st.markdown(f"**Linked Lessons:** {', '.join(row['linked_lessons'])}")
            if row.get('outcome_note'):
                st.markdown(f"**Outcome:** {row['outcome_note']}")


def lesson_explorer_tab():
    st.header("📖 Lesson Explorer")
    lessons_list = load_lessons()
    if not lessons_list:
        st.info("No lessons found in lessons.jsonl")
        return
    df = pd.DataFrame(lessons_list)
    if 'status' not in df.columns:
        df['status'] = 'active'
    if 'tags' not in df.columns:
        df['tags'] = [[] for _ in range(len(df))]
    if 'times_applied' not in df.columns:
        df['times_applied'] = 0
    if 'times_helped' not in df.columns:
        df['times_helped'] = 0
    if 'times_failed' not in df.columns:
        df['times_failed'] = 0
    col1, col2 = st.columns(2)
    with col1:
        status_options = sorted(df['status'].dropna().unique().tolist())
        status_filter = st.multiselect("Filter by Status", options=status_options, default=status_options)
    with col2:
        all_tags = sorted({t for tags in df['tags'] for t in (tags or [])})
        tag_filter = st.multiselect("Filter by Tag", options=all_tags, default=all_tags)
    filtered_df = df[df['status'].isin(status_filter)]
    if tag_filter:
        filtered_df = filtered_df[filtered_df['tags'].apply(lambda ts: any(t in (ts or []) for t in tag_filter))]
    st.metric("Total Lessons", len(filtered_df))
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Times Used", int(filtered_df['times_applied'].sum()))
    with col2:
        st.metric("Times Helped", int(filtered_df['times_helped'].sum()))
    with col3:
        st.metric("Times Failed", int(filtered_df['times_failed'].sum()))
    total_used = int(filtered_df['times_applied'].sum())
    if total_used > 0:
        effectiveness_data = {
            'Helped': int(filtered_df['times_helped'].sum()),
            'Failed': int(filtered_df['times_failed'].sum()),
            'Unknown': total_used - int(filtered_df['times_helped'].sum()) - int(filtered_df['times_failed'].sum()),
        }
        fig = px.pie(values=list(effectiveness_data.values()), names=list(effectiveness_data.keys()),
                     title="Lesson Effectiveness")
        st.plotly_chart(fig, use_container_width=True)
    for _, row in filtered_df.iterrows():
        with st.expander(f"{row.get('title', 'Untitled')} - {row.get('status', 'N/A')}"):
            st.markdown(f"**ID:** {row.get('id', 'N/A')}")
            st.markdown(f"**Trigger:** {row.get('trigger', 'N/A')}")
            st.markdown(f"**Recommendation:** {row.get('recommendation', 'N/A')}")
            st.markdown(f"**Rationale:** {row.get('rationale', 'N/A')}")
            st.markdown(f"**Confidence:** {row.get('confidence', 'N/A')}")
            st.markdown(f"**Tags:** {', '.join(row.get('tags') or [])}")
            st.markdown(f"**Used Count:** {row.get('times_applied', 0)}")
            st.markdown(f"**Helped Count:** {row.get('times_helped', 0)}")
            st.markdown(f"**Failed Count:** {row.get('times_failed', 0)}")


def run_history_tab():
    st.header("📈 Run History")
    runs = load_runs_metadata()
    if not runs:
        st.info("No run metadata found.")
        return
    df = pd.DataFrame(runs)
    display_cols = ['run_id', 'arm', 'days_passed', 'urgent_alerts', 'auto_pauses',
                    'reflex_snapshots', 'difficulty', 'storyteller', 'stop_reason']
    available_cols = [col for col in display_cols if col in df.columns]
    st.dataframe(df[available_cols], use_container_width=True)
    selected_run = st.selectbox("Select Run for Details", options=df['run_id'].unique())
    if selected_run:
        run_data = df[df['run_id'] == selected_run].iloc[0]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Days Survived", run_data['days_passed'])
        with col2:
            st.metric("Urgent Alerts", run_data['urgent_alerts'])
        with col3:
            st.metric("Auto Pauses", run_data['auto_pauses'])
        snapshots = load_run_snapshots(selected_run)
        if snapshots:
            st.subheader(f"Snapshots for {selected_run}")
            timeline_data = []
            for snap in snapshots:
                summary = snap.get('summary', {})
                timeline_data.append({
                    'day': summary.get('day', 'Unknown'),
                    'colonist_count': summary.get('colonist_count', 0),
                    'min_mood': summary.get('min_mood', 0),
                    'min_health': summary.get('min_health', 0),
                    'food_days': summary.get('food_days', 0),
                    'wealth': summary.get('wealth', 0),
                })
            timeline_df = pd.DataFrame(timeline_data)
            col1, col2 = st.columns(2)
            with col1:
                fig_mood = px.line(timeline_df, x='day', y='min_mood', title='Minimum Mood Over Time', markers=True)
                st.plotly_chart(fig_mood, use_container_width=True)
            with col2:
                fig_food = px.line(timeline_df, x='day', y='food_days', title='Food Days Supply Over Time', markers=True)
                st.plotly_chart(fig_food, use_container_width=True)
            st.subheader("Snapshot Details")
            for snap in snapshots:
                with st.expander(f"Day: {snap.get('day', 'Unknown')}"):
                    st.json(snap.get('summary', {}))


def debrief_viewer_tab():
    st.header("📝 Debrief Viewer")
    debriefs = load_debriefs()
    if not debriefs:
        st.info("No debriefs found.")
        return
    debrief_options = [d['filename'] for d in debriefs]
    selected_debrief = st.selectbox("Select Debrief", options=debrief_options)
    if selected_debrief:
        debrief_content = next(d['content'] for d in debriefs if d['filename'] == selected_debrief)
        st.markdown(debrief_content)


def timelapse_tab():
    st.header("🎞 Timelapse")
    try:
        from smartrim.timelapse import build_gif, capture, list_captures
    except Exception as e:
        st.error(f"Timelapse module unavailable: {e}")
        return
    data = list_captures(RUN_ID)
    st.write(f"Run: {data['run_id']}  |  Captures: {len(data['files'])}")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📸 Capture now", use_container_width=True):
            r = capture(RUN_ID)
            st.write(r)
            st.cache_data.clear()
    with c2:
        if st.button("🎞 Build GIF", use_container_width=True):
            r = build_gif(RUN_ID)
            st.write(r)
            st.cache_data.clear()
    files = data["files"]
    d = data["dir"]
    if not files:
        st.info("No captures yet. Enable TIMELAPSE_ENABLED and wait for configured hours, or click Capture now.")
        return
    latest = os.path.join(d, files[-1])
    st.image(latest, caption=f"Latest: {files[-1]}", use_container_width=True)
    gif_path = os.path.join(d, "timelapse.gif")
    if os.path.exists(gif_path):
        st.subheader("Animated GIF")
        st.image(gif_path)
    st.subheader("Browse frames")
    idx = st.slider("Frame", 0, len(files) - 1, len(files) - 1)
    st.image(os.path.join(d, files[idx]), caption=files[idx], use_container_width=True)


# ---------- Main ----------

def main():
    st.markdown('<h1 class="main-header">🎮 SmartRim</h1>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### Navigation")
        mode = st.radio(
            "View",
            ["🎯 Command Center", "📡 Live Monitor", "🎞 Timelapse", "📚 Advice Browser",
             "📖 Lesson Explorer", "📈 Run History", "📝 Debrief Viewer"],
            index=0,
        )
        st.divider()
        # Session details (moved from top bar)
        try:
            gs = get_live_game_state()
        except Exception:
            gs = None
        if gs:
            cond = gs.get("conditions") or {}
            temp = (cond.get("temperature") or {}).get("outdoorC", "?")
            hour = cond.get("hour", "?")
            day = gs.get("daysPassed", "?")
            storyteller = gs.get("storyteller", "?")
            difficulty = gs.get("difficulty", "?")
            paused = "⏸ PAUSED" if gs.get("paused") else "▶ running"
            reflex = "● live" if _reflex_enabled() else "○ off"
            dry = "dry" if _reflex_dry_run() else "LIVE"
            st.markdown("### Session")
            st.markdown(f"**Day {day}** · Hour {hour} · {temp}°C")
            st.markdown(f"{storyteller} · {difficulty}")
            st.markdown(f"{paused} · reflex {reflex} ({dry})")
            st.markdown(f"Colonists: {gs.get('colonistCount', '?')}")
        else:
            st.markdown("### Session")
            st.error("Game not connected")
        st.divider()
        st.markdown("### Auto-refresh")
        refresh = st.selectbox("Interval (s)", [0, 5, 10, 30], index=2,
                               help="0 disables auto-refresh")
        run_every = None if refresh == 0 else refresh
        st.divider()
        st.caption(f"Run: {RUN_ID} · {datetime.now().strftime('%H:%M:%S')}")

    if mode == "🎯 Command Center":
        # Define fragment with chosen interval
        @st.fragment(run_every=run_every)
        def _cc():
            command_center_body()
        _cc()
    elif mode == "📡 Live Monitor":
        live_monitor_tab()
    elif mode == "🎞 Timelapse":
        timelapse_tab()
    elif mode == "📚 Advice Browser":
        advice_browser_tab()
    elif mode == "📖 Lesson Explorer":
        lesson_explorer_tab()
    elif mode == "📈 Run History":
        run_history_tab()
    elif mode == "📝 Debrief Viewer":
        debrief_viewer_tab()


if __name__ == "__main__":
    main()
