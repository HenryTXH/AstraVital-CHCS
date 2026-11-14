# AstraVital | Crew Health & Care System (CHCS)

[![NASA Space Apps Challenge](https://img.shields.io/badge/NASA-Space%20Apps%202026-blue.svg)](https://www.spaceappschallenge.org/)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-orange.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live-Frontend%20Prototype-success.svg)](https://henrytxh.github.io/AstraVital-CHCS/)

AstraVital is an offline, edge-computing software application and hardware kiosk concept engineered for long-duration deep-space transit. Built for the **NASA Space Apps Challenge**, this system operates completely independently of real-time Earth cloud servers to overcome deep-space communication blackouts and latency.

---

## 🛡️ Privacy-First Hardware & Smart Card Architecture

<div align="center">
  <img src="AstraVital_NFC%20.jpg" width="48%" alt="Privacy-First NFC Crew Smart Card" />
  <img src="AstraVital_kiosk.jpg" width="48%" alt="AstraVital Edge Kiosk Prototype" />
</div>

> **Figure: Privacy-First NFC Crew Smart Card and AstraVital Edge Kiosk Architecture.**  
> These visuals illustrate our privacy-first, offline health monitoring workflow built around a passive NFC Crew Smart Card and the onboard AstraVital Edge Kiosk prototype. Instead of relying on invasive facial-recognition cameras or Earth-bound cloud servers, each astronaut carries an encrypted, microchip-embedded badge that requires zero internal battery power. When tapped against the kiosk’s dedicated NFC pad, the card emits short-range inductive waves that instantly authenticate the user on the enclosure's internal single-board edge computer—unlocking real-time biometric telemetry directly on the integrated display. The kiosk’s physical hardware kill-switch ensures zero camera surveillance, while the card's overlapping security shield highlights local data isolation, guaranteeing that crew health logs remain private, friction-free, and 100% operational even during 20-minute deep-space communication blackouts.

---

## 🚀 Core Application Features

- **Predictive Velocity Analytics:** Evaluates 7-day rate-of-change decay (`>0.3 kg/day` mass drop detection) to proactively identify physiological deconditioning and muscle/mass loss early.
- **UTC Window & Streak Tracking:** Synchronizes daily check-in windows to Coordinated Universal Time (`06:00–10:00 UTC`) to maintain protocol discipline and mitigate circadian desynchronization.
- **Encrypted Payload Compression:** Automatically encrypts and compresses crew health records into a 427-byte binary buffer, queueing data safely in local storage during orbital communication blackouts.

---

## ⚙️ Technical Execution (`astravital_core.py`)

The core engine (`astravital_core.py`) is written in Python 3.x and designed to run locally on spacecraft edge hardware (such as an ARM-based SBC or Raspberry Pi 4). It utilizes robust offline data structures to guarantee deterministic state management without external database dependencies:
* **Immutable Sets (`ACTIVE_CREW_IDS`):** O(1) secure astronaut credential verification.
* **Frozen Tuples (`SAFETY_THRESHOLDS`):** Non-overwritable biometric boundary limits.
* **Structured Dictionaries (`crew_health_database`):** Local tracking of telemetry history, compliance streaks, and operational status (`GREEN`, `AMBER`, `RED`).

---

## 🌐 Interactive Frontend Prototype

You can explore the live, interactive web dashboard prototype deployed via GitHub Pages:
🔗 **[AstraVital Dashboard Prototype (HTML)](https://henrytxh.github.io/AstraVital-CHCS/)**

---

## 📂 Repository Structure

```text
AstraVital-CHCS/
├── index.html              # Live HTML/JS frontend dashboard
├── astravital_core.py      # Core Python backend (Phases 1, 2, & 3 logic)
├── AstraVital_NFC .jpg     # NFC Smart Card architecture visual
├── AstraVital_kiosk.jpg    # Edge Kiosk hardware prototype visual
├── ALGORITHMS.md           # Detailed pseudocode and algorithmic documentation
└── README.md               # Project documentation
