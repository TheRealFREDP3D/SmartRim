import os
import json
import glob
from datetime import datetime
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import plotly.express as px
from config import *

# Page configuration
st.set_page_config(
    page_title="SmartRim Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
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
    .status-urgent {
        color: #dc2626;
        font-weight: bold;
    }
    .status-warning {
        color: #f59e0b;
        font-weight: bold;
    }
    .status-info {
        color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)


# Data loading functions
@st.cache_data(ttl=10)
def load_current_alerts():
    """Load current alerts from the monitor."""
    alert_path = os.path.join(ALERTS_DIR, "current.json")
    if os.path.exists(alert_path):
        with open(alert_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


@st.cache_data(ttl=60)
def load_all_advice():
    """Load all advice from advice.jsonl."""
    advice_path = os.path.join(BASE_DIR, "memory", "advice", "advice.jsonl")
    advice_list = []
    if os.path.exists(advice_path):
        with open(advice_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    advice_list.append(json.loads(line))
    return advice_list


@st.cache_data(ttl=60)
def load_lessons():
    """Load lessons from lessons.jsonl."""
    lessons_path = os.path.join(BASE_DIR, "memory", "lessons.jsonl")
    lessons_list = []
    if os.path.exists(lessons_path):
        with open(lessons_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    lessons_list.append(json.loads(line))
    return lessons_list


@st.cache_data(ttl=60)
def load_runs_metadata():
    """Load run metadata from memory/runs directory."""
    runs_dir = os.path.join(BASE_DIR, "memory", "runs")
    runs = []
    if os.path.exists(runs_dir):
        for file in glob.glob(os.path.join(runs_dir, "*.end.json")):
            with open(file, 'r', encoding='utf-8') as f:
                runs.append(json.load(f))
    return runs


@st.cache_data(ttl=60)
def load_run_snapshots(run_id):
    """Load all snapshots for a specific run."""
    snapshot_dir = os.path.join(SNAPSHOTS_DIR, run_id)
    snapshots = []
    if os.path.exists(snapshot_dir):
        for file in glob.glob(os.path.join(snapshot_dir, "day-*.json")):
            with open(file, 'r', encoding='utf-8') as f:
                snapshots.append(json.load(f))
        # Sort by day
        snapshots.sort(key=lambda x: x.get('day', ''))
    return snapshots


@st.cache_data(ttl=60)
def load_debriefs():
    """Load debrief summaries."""
    debriefs_dir = os.path.join(BASE_DIR, "memory", "debriefs")
    debriefs = []
    if os.path.exists(debriefs_dir):
        for file in glob.glob(os.path.join(debriefs_dir, "*.md")):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                debriefs.append({
                    'filename': os.path.basename(file),
                    'content': content
                })
    return debriefs


def get_live_game_state():
    """Get current game state from MCP server."""
    try:
        from mcp_client import McpClient
        client = McpClient(MCP_URL, delay=MCP_DELAY)
        status = client.call_tool("get_status")
        if status and not status.get("error"):
            return status
    except Exception as e:
        st.error(f"Failed to connect to MCP server: {e}")
    return None


# Live Monitor Tab
def live_monitor_tab():
    st.header("🎮 Live Game Monitor")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    
    with col2:
        game_connected = st.empty()
    
    with col3:
        run_id_display = st.empty()
    
    # Try to get live game state
    game_state = get_live_game_state()
    
    if game_state:
        game_connected.success("✅ Game Connected")
        run_id_display.info(f"Run ID: {RUN_ID}")
        
        # Display game status
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Days Passed", game_state.get('daysPassed', 0))
        
        with col2:
            st.metric("Colonists", game_state.get('colonistCount', 0))
        
        with col3:
            st.metric("Wealth", f"{game_state.get('wealthTotal', 0):,}")
        
        with col4:
            st.metric("Difficulty", game_state.get('difficulty', 'Unknown'))
        
        # Load current alerts
        alerts = load_current_alerts()
        
        st.subheader("Current Alerts")
        if alerts:
            for alert in alerts:
                severity = alert.get('type', 'info')
                icon = "🔴" if severity == "urgent" else "⚠️" if severity == "warning" else "ℹ️"
                severity_class = f"status-{severity}"
                st.markdown(f"""
                <div class="metric-card">
                    <span class="{severity_class}">{icon} {severity.upper()}</span>: {alert.get('message', 'No message')}
                    <br><small>{alert.get('timestamp', '')}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No current alerts")
        
        # Get colonist details
        try:
            from mcp_client import McpClient
            client = McpClient(MCP_URL, delay=MCP_DELAY)
            colonists = client.call_tool("list_colonists")
            
            if colonists and colonists.get('colonists'):
                st.subheader("Colonists")
                colonist_df = pd.DataFrame(colonists['colonists'])
                
                # Select columns to display
                display_cols = ['name', 'age', 'mood', 'health', 'job']
                available_cols = [col for col in display_cols if col in colonist_df.columns]
                if available_cols:
                    st.dataframe(colonist_df[available_cols], use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load colonist data: {e}")
        
        # Get resources
        try:
            from mcp_client import McpClient
            client = McpClient(MCP_URL, delay=MCP_DELAY)
            resources = client.call_tool("get_resources")
            
            if resources and resources.get('resources'):
                st.subheader("Key Resources")
                res_df = pd.DataFrame(resources['resources'])
                # Filter for important resources
                important = ['Meal', 'Medicine', 'Steel', 'Wood', 'Component', 'Food']
                filtered = res_df[res_df['label'].str.contains('|'.join(important), case=False, na=False)]
                if not filtered.empty:
                    st.dataframe(filtered, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load resource data: {e}")
    else:
        game_connected.error("❌ Game Not Connected")
        run_id_display.info(f"Run ID: {RUN_ID}")
        st.warning("Unable to connect to RimWorld MCP server. Make sure RimWorld is running with the RimMolt mod.")


# Advice Browser Tab
def advice_browser_tab():
    st.header("📋 Advice Browser")
    
    advice_list = load_all_advice()
    
    if not advice_list:
        st.info("No advice records found.")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(advice_list)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        run_filter = st.multiselect(
            "Filter by Run ID",
            options=df['run_id'].unique(),
            default=df['run_id'].unique()
        )
    
    with col2:
        severity_filter = st.multiselect(
            "Filter by Severity",
            options=df['severity'].unique(),
            default=df['severity'].unique()
        )
    
    with col3:
        status_filter = st.multiselect(
            "Filter by Status",
            options=df['status'].unique(),
            default=df['status'].unique()
        )
    
    # Apply filters
    filtered_df = df[
        df['run_id'].isin(run_filter) &
        df['severity'].isin(severity_filter) &
        df['status'].isin(status_filter)
    ]
    
    st.metric("Total Advice Records", len(filtered_df))
    
    # Display advice
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


# Lesson Explorer Tab
def lesson_explorer_tab():
    st.header("📚 Lesson Explorer")
    
    lessons_list = load_lessons()
    
    if not lessons_list:
        st.info("No lessons found in lessons.jsonl")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(lessons_list)
    
    # Normalize schema-derived columns
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

    # Filters
    col1, col2 = st.columns(2)

    with col1:
        status_options = sorted(df['status'].dropna().unique().tolist())
        status_filter = st.multiselect(
            "Filter by Status",
            options=status_options,
            default=status_options,
        )

    with col2:
        all_tags = sorted({t for tags in df['tags'] for t in (tags or [])})
        tag_filter = st.multiselect(
            "Filter by Tag",
            options=all_tags,
            default=all_tags,
        )

    # Apply filters
    filtered_df = df[df['status'].isin(status_filter)]
    if tag_filter:
        filtered_df = filtered_df[filtered_df['tags'].apply(lambda ts: any(t in (ts or []) for t in tag_filter))]

    st.metric("Total Lessons", len(filtered_df))

    # Effectiveness metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        total_used = int(filtered_df['times_applied'].sum())
        st.metric("Total Times Used", total_used)

    with col2:
        total_helped = int(filtered_df['times_helped'].sum())
        st.metric("Times Helped", total_helped)

    with col3:
        total_failed = int(filtered_df['times_failed'].sum())
        st.metric("Times Failed", total_failed)

    # Effectiveness chart
    if total_used > 0:
        effectiveness_data = {
            'Helped': total_helped,
            'Failed': total_failed,
            'Unknown': total_used - total_helped - total_failed,
        }
        fig = px.pie(
            values=list(effectiveness_data.values()),
            names=list(effectiveness_data.keys()),
            title="Lesson Effectiveness",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Display lessons
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


# Run History Tab
def run_history_tab():
    st.header("📊 Run History")
    
    runs = load_runs_metadata()
    
    if not runs:
        st.info("No run metadata found.")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(runs)
    
    # Display summary table
    st.subheader("Run Summary")
    display_cols = ['run_id', 'arm', 'days_passed', 'urgent_alerts', 'auto_pauses', 
                    'reflex_snapshots', 'difficulty', 'storyteller', 'stop_reason']
    available_cols = [col for col in display_cols if col in df.columns]
    st.dataframe(df[available_cols], use_container_width=True)
    
    # Select run for detailed view
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
        
        # Load snapshots for this run
        snapshots = load_run_snapshots(selected_run)
        
        if snapshots:
            st.subheader(f"Snapshots for {selected_run}")
            
            # Create timeline data
            timeline_data = []
            for snap in snapshots:
                summary = snap.get('summary', {})
                timeline_data.append({
                    'day': summary.get('day', 'Unknown'),
                    'colonist_count': summary.get('colonist_count', 0),
                    'min_mood': summary.get('min_mood', 0),
                    'min_health': summary.get('min_health', 0),
                    'food_days': summary.get('food_days', 0),
                    'wealth': summary.get('wealth', 0)
                })
            
            timeline_df = pd.DataFrame(timeline_data)
            
            # Charts
            col1, col2 = st.columns(2)
            
            with col1:
                fig_mood = px.line(timeline_df, x='day', y='min_mood', 
                                   title='Minimum Mood Over Time', markers=True)
                st.plotly_chart(fig_mood, use_container_width=True)
            
            with col2:
                fig_food = px.line(timeline_df, x='day', y='food_days',
                                    title='Food Days Supply Over Time', markers=True)
                st.plotly_chart(fig_food, use_container_width=True)
            
            # Snapshot details
            st.subheader("Snapshot Details")
            for snap in snapshots:
                with st.expander(f"Day: {snap.get('day', 'Unknown')}"):
                    summary = snap.get('summary', {})
                    st.json(summary)


# Debrief Viewer Tab
def debrief_viewer_tab():
    st.header("📝 Debrief Viewer")
    
    debriefs = load_debriefs()
    
    if not debriefs:
        st.info("No debriefs found.")
        return
    
    # Select debrief
    debrief_options = [d['filename'] for d in debriefs]
    selected_debrief = st.selectbox("Select Debrief", options=debrief_options)
    
    if selected_debrief:
        debrief_content = next(d['content'] for d in debriefs if d['filename'] == selected_debrief)
        st.markdown(debrief_content)


# Main app
def main():
    st.markdown('<h1 class="main-header">🎮 SmartRim Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    tab = st.sidebar.radio(
        "Navigate",
        ["🎮 Live Monitor", "📋 Advice Browser", "📚 Lesson Explorer", "📊 Run History", "📝 Debrief Viewer"]
    )
    
    if tab == "🎮 Live Monitor":
        live_monitor_tab()
    elif tab == "📋 Advice Browser":
        advice_browser_tab()
    elif tab == "📚 Lesson Explorer":
        lesson_explorer_tab()
    elif tab == "📊 Run History":
        run_history_tab()
    elif tab == "📝 Debrief Viewer":
        debrief_viewer_tab()


if __name__ == "__main__":
    main()
