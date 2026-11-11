"""
AstraVital | Crew Health & Care System (CHCS)
Complete Backend: Phase 1 (Data Logic), Phase 2 (Edge Latency), & Phase 3 (Compliance/Punctuality)
Author: Solo Engineering Team
"""

import json
import time
from datetime import datetime

# 1. SET: Unique, unmodifiable collection of authorized crew member IDs
ACTIVE_CREW_IDS = {
    "ASTRO_01_KALEB",
    "ASTRO_02_ELENA",
    "ASTRO_03_TARIQ",
    "ASTRO_04_MEI",
    "ASTRO_05_ZACK",
}

# 2. TUPLE: Immutable safety threshold ranges (Warning_Low, Warning_High)
SAFETY_THRESHOLDS = {
    "mass_kg": (50.0, 100.0),
    "heart_rate": (50, 100),
    "spo2": (95, 100),
    "radiation_mSv": (0.0, 15.0),
}

# 3. DICTIONARY: Structured database tracking crew metrics, history, and punctuality
crew_health_database = {
    "ASTRO_01_KALEB": {
        "name": "Kaleb Vance (Commander)",
        "status": "GREEN",
        "current_metrics": {
            "mass_kg": 74.5,
            "heart_rate": 68,
            "spo2": 98,
            "radiation_mSv": 4.2,
        },
        "7_day_history": {
            "mass_kg": [74.9, 74.8, 74.7, 74.6, 74.5, 74.5, 74.5]
        },
        "compliance": {
            "streak_days": 14,
            "punctuality_status": "PENDING",
            "last_checkin": "None",
        },
    },
    "ASTRO_02_ELENA": {
        "name": "Elena Rostova (Mission Specialist)",
        "status": "GREEN",
        "current_metrics": {
            "mass_kg": 59.5,
            "heart_rate": 88,
            "spo2": 97,
            "radiation_mSv": 11.2,
        },
        "7_day_history": {
            "mass_kg": [66.0, 65.0, 64.0, 63.0, 62.0, 61.0, 59.5]
        },
        "compliance": {
            "streak_days": 9,
            "punctuality_status": "PENDING",
            "last_checkin": "None",
        },
    },
    "ASTRO_03_TARIQ": {
        "name": "Tariq Al-Hassan (Flight Engineer)",
        "status": "GREEN",
        "current_metrics": {
            "mass_kg": 78.0,
            "heart_rate": 115,
            "spo2": 91,
            "radiation_mSv": 16.5,
        },
        "7_day_history": {
            "mass_kg": [78.1, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0]
        },
        "compliance": {
            "streak_days": 3,
            "punctuality_status": "PENDING",
            "last_checkin": "None",
        },
    },
    "ASTRO_04_MEI": {
        "name": "Mei-Ling Zhou (Payload Specialist)",
        "status": "GREEN",
        "current_metrics": {
            "mass_kg": 61.2,
            "heart_rate": 72,
            "spo2": 99,
            "radiation_mSv": 2.1,
        },
        "7_day_history": {
            "mass_kg": [61.3, 61.2, 61.2, 61.2, 61.2, 61.2, 61.2]
        },
        "compliance": {
            "streak_days": 21,
            "punctuality_status": "PENDING",
            "last_checkin": "None",
        },
    },
    "ASTRO_05_ZACK": {
        "name": "Zack Taylor (Systems Specialist)",
        "status": "GREEN",
        "current_metrics": {
            "mass_kg": 82.4,
            "heart_rate": 75,
            "spo2": 98,
            "radiation_mSv": 5.0,
        },
        "7_day_history": {
            "mass_kg": [82.5, 82.4, 82.4, 82.4, 82.4, 82.4, 82.4]
        },
        "compliance": {
            "streak_days": 12,
            "punctuality_status": "PENDING",
            "last_checkin": "None",
        },
    },
}


def evaluate_predictive_decay(history_list):
  """Phase 1: Analyzes 7-day rate-of-change velocity to catch downward muscle/mass trends early."""
  if len(history_list) < 7:
    return False
  total_drop = history_list[0] - history_list[-1]
  daily_velocity = total_drop / 7.0
  return daily_velocity > 0.3


def simulate_deep_space_uplink(packet_data):
  """Phase 2: Simulates deep-space communication delay and local edge payload compression."""
  print(
      "\n[EDGE SYSTEM] Real-time Earth connection offline (Deep-Space Latency"
      " Active)."
  )
  print(
      "[EDGE SYSTEM] Compressing telemetry packet into encrypted binary"
      " payload..."
  )
  time.sleep(0.4)
  compressed_packet = json.dumps(packet_data)
  print(
      f"[EDGE SYSTEM] Packet successfully compressed ({len(compressed_packet)} bytes)."
  )
  print(
      "[EDGE SYSTEM] Status: Queued in local secure buffer for next orbital"
      " transmission window."
  )


def evaluate_punctuality_and_compliance(astro_id, checkin_time_str):
  """Phase 3: Validates check-in timestamp against UTC Mission Window (06:00 - 10:00 UTC)."""
  astro_compliance = crew_health_database[astro_id]["compliance"]
  astro_compliance["last_checkin"] = checkin_time_str + " UTC"

  # Define UTC Check-in Window
  window_start = "06:00"
  window_end = "10:00"

  if window_start <= checkin_time_str <= window_end:
    astro_compliance["punctuality_status"] = "ON_TIME"
    astro_compliance["streak_days"] += 1
    print(
        "[COMPLIANCE] Check-in ON TIME. Streak incremented to"
        f" {astro_compliance['streak_days']} days."
    )
  else:
    astro_compliance["punctuality_status"] = "LATE_CHECKIN"
    print(
        "[COMPLIANCE] WARNING: Check-in outside primary window"
        f" ({window_start}-{window_end} UTC). Streak preserved."
    )


def process_kiosk_checkin(astro_id, live_readings, checkin_time_str):
  """Complete workflow combining ID authentication, compliance tracking, tuple bounds, and edge latency."""
  if astro_id not in ACTIVE_CREW_IDS:
    return f"ACCESS DENIED: Crew ID '{astro_id}' not recognized in active roster."

  # Run Phase 3 Compliance & Punctuality Evaluation
  evaluate_punctuality_and_compliance(astro_id, checkin_time_str)

  astro_data = crew_health_database[astro_id]
  status = "GREEN"
  reasons = []

  # Evaluate current metrics against TUPLE safety bounds
  for metric, value in live_readings.items():
    if metric in SAFETY_THRESHOLDS:
      min_lim, max_lim = SAFETY_THRESHOLDS[metric]
      if not (min_lim <= value <= max_lim):
        if (metric == "spo2" and value < 93) or (
            metric == "radiation_mSv" and value > max_lim * 1.1
        ):
          status = "RED"
          reasons.append(
              f"CRITICAL BREACH [{metric}]: {value} dangerously out of bounds!"
          )
        else:
          if status != "RED":
            status = "AMBER"
          reasons.append(
              f"CAUTION [{metric}]: {value} outside normal range"
              f" {(min_lim, max_lim)}."
          )

  # Check 7-day Predictive Decay (Dictionary history check)
  for metric, history in astro_data["7_day_history"].items():
    if metric == "mass_kg" and evaluate_predictive_decay(history):
      if status == "GREEN":
        status = "AMBER"
      reasons.append(
          "PREDICTIVE ALERT: Rapid downward mass/muscle velocity detected over 7"
          " days."
      )

  # Update Dictionary State
  astro_data["status"] = status
  astro_data["current_metrics"] = live_readings
  astro_data["active_warnings"] = reasons

  # Trigger Phase 2 Deep-Space Latency Simulation
  simulate_deep_space_uplink(astro_data)

  return astro_data


# --- HACKATHON DEMO EXECUTION (PHASES 1, 2, & 3 COMBINED) ---
if __name__ == "__main__":
  print("==========================================================")
  print("  ASTRAVITAL CHCS | ID SCAN, PUNCTUALITY & LATENCY SYSTEM")
  print("==========================================================")

  # Testing Scenario: Elena scans her badge at 08:30 UTC (On Time)
  scanned_id = "ASTRO_02_ELENA"
  kiosk_scan = {
      "mass_kg": 59.5,
      "heart_rate": 88,
      "spo2": 97,
      "radiation_mSv": 11.2,
  }
  checkin_timestamp = "08:30"  # Within 06:00 - 10:00 UTC window

  print(f"\n[SCANNER] ID Badge Scanned: {scanned_id} at {checkin_timestamp} UTC")
  result = process_kiosk_checkin(scanned_id, kiosk_scan, checkin_timestamp)

  print(f"\nFinal Kiosk Record Output for {scanned_id}:")
  print(json.dumps(result, indent=4))
