Algorithm 1.1: AstraVital Closed Kiosk Multi-Sensor Check-In & Decay Engine
Evaluates 7-day rate-of-change velocity. If muscle/mass drops rapidly, it flags a proactive TREND TO REVIEW state before a clinical emergency occurs.

====================================================================
Algorithm 1.1: AstraVital Closed Kiosk Multi-Sensor Check-In & Decay Engine
====================================================================
Required: 
  - ACTIVE_CREW_IDS: Set of authorized string identifiers
  - SAFETY_THRESHOLDS: Dictionary of immutable (min, max) tuple bounds
  - crew_database: Nested dictionary storing current metrics and 7-day history
  - incoming_id: String scanned at the kiosk
  - live_readings: Dictionary of current biometric sensor stream

Ensured: 
  - Updated crew status ('GREEN', 'AMBER', or 'RED')
  - Active warning logs and automated countermeasure triggers

Initialize:
  status ← "GREEN"
  reasons[] ← empty list
  daily_velocity ← 0.0

begin
  1: IF incoming_id NOT IN ACTIVE_CREW_IDS THEN
  2:     PRINT "ACCESS DENIED: Unauthorized Crew ID."
  3:     RETURN Error_State
  4: END IF

  5: FOR EACH metric, value IN live_readings DO
  6:     min_lim, max_lim ← SAFETY_THRESHOLDS[metric]
  7:     IF (value < min_lim) OR (value > max_lim) THEN
  8:         IF (metric == "spo2" AND value < 93) OR (metric == "radiation_mSv" AND value > max_lim * 1.1) THEN
  9:             status ← "RED"
  10:            APPEND "CRITICAL BREACH: " + metric TO reasons
  11:        ELSE
  12:            IF status != "RED" THEN status ← "AMBER" END IF
  13:            APPEND "CAUTION: " + metric TO reasons
  14:        END IF
  15:    END IF
  16: END FOR

  17: history_list ← crew_database[incoming_id]["7_day_history"]["mass_kg"]
  18: total_drop ← history_list[0] - history_list[LENGTH(history_list) - 1]
  19: daily_velocity ← total_drop / 7.0

  20: IF daily_velocity > 0.3 THEN
  21:     IF status == "GREEN" THEN status ← "AMBER" END IF
  22:     APPEND "PREDICTIVE ALERT: Rapid downward mass velocity detected." TO reasons
  23: END IF

  24: crew_database[incoming_id]["status"] ← status
  25: crew_database[incoming_id]["active_warnings"] ← reasons
  26: RETURN crew_database[incoming_id]
end

Algorithm 2.1: Deep-Space Edge Compression & Latency Simulation
Simulates the communication blackout by converting Python dictionary states into encrypted binary payloads, queueing them in a local buffer.

====================================================================
Algorithm 2.1: Deep-Space Edge Payload Compression & Latency Queueing
====================================================================
Required: 
  - packet_data: Fully evaluated crew health dictionary record

Ensured: 
  - Compressed binary payload string
  - Secure local buffer queue status for orbital transmission

Initialize:
  compressed_packet ← ""
  buffer_status ← "QUEUED"

begin
  1: PRINT "Real-time Earth connection offline (Deep-Space Latency Active)."
  2: PRINT "Compressing telemetry packet into encrypted binary payload..."
  
  3: // Simulate local processing delay
  4: DELAY 400 milliseconds

  5: compressed_packet ← CONVERT_TO_JSON_AND_ENCRYPT(packet_data)
  6: payload_size ← LENGTH(compressed_packet)

  7: PRINT "Packet successfully compressed: " + payload_size + " bytes."
  8: PRINT "Status: Queued in local secure buffer for next orbital window."

  9: RETURN (compressed_packet, buffer_status)
end

Algorithm 3.1: Compliance & Punctuality Tracker
Synchronizes the check-in window to the mission UTC clock. Prevents circadian confusion and tracks daily protocol compliance streaks.
====================================================================
Algorithm 3.1: AstraVital Compliance & Punctuality Tracker
====================================================================
Required: 
  - crew_database: Dictionary tracking all crew records
  - scanned_id: String ID from the kiosk badge scanner
  - checkin_time_str: Current timestamp string in UTC (e.g., "08:30")

Ensured: 
  - Updated check-in UTC timestamp
  - Incremented daily compliance streak
  - Verified punctuality status ('ON_TIME' or 'LATE_CHECKIN')

Initialize:
  window_start ← "06:00"
  window_end   ← "10:00"

begin
  1: IF scanned_id NOT IN crew_database THEN
  2:     RETURN "Error: Unrecognized ID Badge."
  3: END IF

  4: astro_compliance ← crew_database[scanned_id]["compliance"]
  5: astro_compliance["last_checkin"] ← checkin_time_str + " UTC"

  6: IF checkin_time_str >= window_start AND checkin_time_str <= window_end THEN
  7:     astro_compliance["punctuality_status"] ← "ON_TIME"
  8:     astro_compliance["streak_days"] ← astro_compliance["streak_days"] + 1
  9:     PRINT "Check-in ON TIME. Streak incremented."
  10: ELSE
  11:    astro_compliance["punctuality_status"] ← "LATE_CHECKIN"
  12:    PRINT "WARNING: Check-in outside primary UTC window. Streak preserved."
  13: END IF

  14: RETURN astro_compliance
end




