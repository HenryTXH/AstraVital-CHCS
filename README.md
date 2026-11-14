<img width="1600" height="1000" alt="AstraVital_OpenFront_Kiosk_Dashboard_Concept" src="https://github.com/user-attachments/assets/3c7ed60a-4990-4dde-9d48-c3a3922bfb74" />

# AstraVital | Crew Health & Care System (CHCS)

[![NASA Space Apps Challenge](https://img.shields.io/badge/NASA-Space%20Apps%202026-blue.svg)](https://www.spaceappschallenge.org/)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-orange.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AstraVital is an offline, edge-computing software application and hardware kiosk concept engineered for long-duration deep-space transit. Built for the **NASA Space Apps Challenge**, this backend engine operates completely independently of real-time Earth cloud servers to overcome deep-space communication latency.

---

## Core Application Features
- **Predictive Velocity Analytics:** Evaluates 7-day rate-of-change decay (`>0.3 kg/day` mass drop detection) to proactively detect physiological deconditioning (muscle/mass loss) early.
- **UTC Window & Streak Tracking:** Synchronizes daily check-in windows to Coordinated Universal Time (`06:00–10:00 UTC`) to maintain protocol discipline and mitigate circadian desynchronization.
- **Encrypted Payload Compression:** Automatically encrypts and compresses crew health records into a 427-byte binary buffer, queueing data safely during orbital communication blackouts.

---

## 🛡️ Privacy-First Hardware & Smart Card Architecture

<div align="center">
  <img width="48%" alt="AstraVital_NFC_Smart_Card" src="PASTE_GITHUB_ASSET_URL_FOR_NFC_HERE" />
  <img width="48%" alt="AstraVital_Edge_Kiosk" src="PASTE_GITHUB_ASSET_URL_FOR_KIOSK_HERE" />
</div>

> **Figure: Privacy-First NFC Crew Smart Card and AstraVital Edge Kiosk Architecture.**  
> These visuals illustrate our privacy-first, offline health monitoring workflow built around a passive NFC Crew Smart Card and the onboard AstraVital Edge Kiosk prototype. Instead of relying on invasive facial-recognition cameras or Earth-bound cloud servers, each astronaut carries an encrypted, microchip-embedded badge that requires zero internal battery power. When tapped against the kiosk’s dedicated NFC pad, the card emits short-range inductive waves that instantly authenticate the user on the enclosure's internal single-board edge computer—unlocking real-time biometric telemetry directly on the integrated display. The kiosk’s physical hardware kill-switch ensures zero camera surveillance, while the card's overlapping security shield highlights local data isolation, guaranteeing that crew health logs remain private, friction-free, and 100% operational even during 20-minute deep-space communication blackouts.

---

## Technical Execution
The core engine (`astravital_core.py`) is written in Python 3.x and designed to run locally on spacecraft edge hardware (such as an ARM-based SBC or Raspberry Pi). It utilizes offline data structures (immutable sets, frozen tuples, and nested dictionaries) to guarantee deterministic state management without external database dependencies.

<img width="1600" height="1050" alt="AstraVital_Kiosk_Concept_Structure" src="https://github.com/user-attachments/assets/f356a511-f110-40e9-899a-b167731ffd32" />

---

## Interactive Frontend Prototype
🔗 **[AstraVital Dashboard Prototype (HTML)](https://henrytxh.github.io/AstraVital-CHCS/)**

<img width="1754" height="1240" alt="AstraVital _ Crew Health   Care System (CHCS)_page-0001" src="https://github.com/user-attachments/assets/3b9b03e6-f230-45fe-b425-0151f184ca4e" />

<img width="1754" height="1240" alt="AstraVital _ Crew Health   Care System (CHCS)_page-0002" src="https://github.com/user-attachments/assets/3ad52e34-6d46-49a9-8b3d-04079ab7770b" />
