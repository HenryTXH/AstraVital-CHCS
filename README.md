# AstraVital | Crew Health & Care System (CHCS)

[![NASA Space Apps Challenge](https://img.shields.io/badge/NASA-Space%20Apps%202026-blue.svg)](https://www.spaceappschallenge.org/)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-orange.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Executive Summary: Privacy-First Kiosk & NFC Architecture

**AstraVital** is an offline, edge-computing crew health and care ecosystem engineered for long-duration deep-space transit. Built for the **NASA Space Apps Challenge**, the system solves deep-space communication latency and privacy compliance fatigue through a revolutionary **passive NFC Smart Card** and **Edge Kiosk** hardware architecture. 

- **Privacy-First Authentication:** Replaces invasive facial-recognition cameras and cloud servers with battery-free, microchip-embedded NFC badges for instant, secure local identification.
- **100% Offline Resilience:** Operates entirely independently on spacecraft single-board computers, ensuring zero-latency tracking and robust data queueing during 20-minute communication blackouts.

<div align="center">
  <img width="1600" height="1000" alt="AstraVital_OpenFront_Kiosk_Dashboard_Concept" src="https://github.com/user-attachments/assets/3c7ed60a-4990-4dde-9d48-c3a3922bfb74" />
</div>

---

## 🛡️ Hardware & Smart Card Architecture

<div align="center">
  <img width="48%" alt="AstraVital_NFC" src="https://github.com/user-attachments/assets/179bf3ac-7ff5-4ac4-8660-dcc2a815c277" />
  <img width="48%" alt="AstraVital_kiosk" src="https://github.com/user-attachments/assets/389e0efd-0b4f-4997-8379-6ebb826d9ac2" />
</div>

> **Figure: Privacy-First NFC Crew Smart Card and AstraVital Edge Kiosk Architecture.**  
> These visuals illustrate our offline health monitoring workflow: astronauts tap their battery-free NFC Smart Card against the kiosk's inductive pad to authenticate locally on the onboard edge computer. A physical hardware kill-switch ensures zero camera surveillance, protecting astronaut privacy while guaranteeing 100% operational autonomy during deep-space transit.

---

## ⚡ Aerospace-Grade Electrical & Physical Architecture

- **Power Protection Topology:** Engineered for spacecraft 28V DC microgrid buses with Transient Voltage Suppressor (TVS) surge-protection diodes and high-efficiency buck converters providing regulated 5V and 3.3V rails.
- **Structural Enclosure:** Ruggedized Anodized Aluminum 6061-T6 chassis with built-in stabilization grab-rails for microgravity handling and fanless thermal dissipation.

<div align="center">
  <img width="48%" alt="Power Protection & Microgrid Integration Schematic" src="https://github.com/user-attachments/assets/54ddae55-b78c-4579-a087-503192796e59" />
  <img width="48%" alt="Structural Enclosure Cutaway" src="https://github.com/user-attachments/assets/5874b89a-468a-4226-8689-0b36aae3a595" />
</div>

---

## 🚀 Core Application Features

- **Predictive Velocity Analytics:** Evaluates 7-day rate-of-change decay (`>0.3 kg/day` mass drop detection) to proactively detect physiological deconditioning (muscle/mass loss) early.
- **UTC Window & Streak Tracking:** Synchronizes daily check-in windows to Coordinated Universal Time (`06:00–10:00 UTC`) to maintain protocol discipline and mitigate circadian desynchronization.
- **Encrypted Payload Compression:** Automatically encrypts and compresses crew health records into a 427-byte binary buffer, queueing data safely during orbital communication blackouts.

---

## ⚙️ Technical Execution

The core engine (`astravital_core.py`) is written in Python 3.x and designed to run locally on spacecraft edge hardware (such as an ARM-based SBC or Raspberry Pi). It utilizes offline data structures (immutable sets, frozen tuples, and nested dictionaries) to guarantee deterministic state management without external database dependencies.

<div align="center">
  <img width="1600" height="1050" alt="AstraVital_Kiosk_Concept_Structure" src="https://github.com/user-attachments/assets/f356a511-f110-40e9-899a-b167731ffd32" />
</div>

---

## 🌐 Interactive Frontend Prototype & Official Documentation

🔗 **[AstraVital Dashboard Prototype (HTML)](https://henrytxh.github.io/AstraVital-CHCS/)**

<div align="center">
  <img width="48%" alt="AstraVital Dashboard Page 1" src="https://github.com/user-attachments/assets/3b9b03e6-f230-45fe-b425-0151f184ca4e" />
  <img width="48%" alt="AstraVital Dashboard Page 2" src="https://github.com/user-attachments/assets/3ad52e34-6d46-49a9-8b3d-04079ab7770b" />
</div>

### 📂 Official Project Backups & Submission Links
- **Official Google Docs Report Backup:** [AstraVital Submission Report](https://docs.google.com/document/d/1W9MOtGkEi7itcF7fo7kuMoXMvS46rdy-4VcFw_8g03I/edit?usp=sharing)
- **Presentation Slides:** Accessible via repository backup assets (`Presentation_Slides_AstraVital.pdf`).
