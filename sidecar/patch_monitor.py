path = r"C:\Users\fred\Desktop\RimWorld Consellor\RimAutonomous\sidecar\monitor.py"
s = open(path, encoding="utf-8").read()

old = '''                    if urgent:
                        print(f"{len(alerts)} alert(s) ({len(urgent)} urgent) - pausing game")
                        try:
                            import advice_log
                            advice_log.log_advice(
                                run_id=RUN_ID,
                                snapshot_day=current_day or "unknown",
                                trigger="reflex",
                                severity="urgent",
                                situation="; ".join(a.get("message", "") for a in urgent),
                                actions=[{"rank": 1, "action": "Pause game and assess", "rationale": "Reflex check triggered urgent alert"}],
                                risks=[{"label": a.get("message", ""), "severity": "urgent"} for a in urgent],
                                reflex_name=",".join(sorted(set(a.get("category", "") for a in urgent))),
                                auto_paused=True,
                            )
                        except Exception as e:
                            print(f"advice log error: {e}")
                        try:
                            client.call_tool("set_speed", {"action": "pause"})
                        except Exception:
                            pass'''

new = '''                    if urgent:
                        print(f"{len(alerts)} alert(s) ({len(urgent)} urgent)")
                        if not OBSERVE_ONLY:
                            try:
                                import advice_log
                                advice_log.log_advice(
                                    run_id=RUN_ID,
                                    snapshot_day=current_day or "unknown",
                                    trigger="reflex",
                                    severity="urgent",
                                    situation="; ".join(a.get("message", "") for a in urgent),
                                    actions=[{"rank": 1, "action": "Pause game and assess", "rationale": "Reflex check triggered urgent alert"}],
                                    risks=[{"label": a.get("message", ""), "severity": "urgent"} for a in urgent],
                                    reflex_name=",".join(sorted(set(a.get("category", "") for a in urgent))),
                                    auto_paused=True,
                                )
                            except Exception as e:
                                print(f"advice log error: {e}")
                            try:
                                client.call_tool("set_speed", {"action": "pause"})
                            except Exception:
                                pass'''

assert old in s, "old block not found"
s = s.replace(old, new)
open(path, "w", encoding="utf-8").write(s)
print("patched")
