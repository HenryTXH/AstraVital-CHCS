<img width="1600" height="1000" alt="AstraVital_OpenFront_Kiosk_Dashboard_Concept" src="https://github.com/user-attachments/assets/3c7ed60a-4990-4dde-9d48-c3a3922bfb74" /># AstraVital | Crew Health & Care System (CHCS)

AstraVital is an offline, edge-computing software application engineered for long-duration deep-space transit. Built for the NASA Space Apps Challenge, this backend engine operates completely independently of real-time Earth cloud servers to overcome deep-space communication latency.

## Core Application Features
* **Predictive Velocity Analytics:** Evaluates 7-day rate-of-change decay to proactively detect physiological deconditioning (muscle/mass loss) early.
* **UTC Window & Streak Tracking:** Synchronizes daily check-in windows to Coordinated Universal Time (UTC) to maintain protocol discipline and mitigate circadian desynchronization.
* **Encrypted Payload Compression:** Automatically encrypts and compresses crew health records into a 427-byte binary buffer, queueing data safely during orbital communication blackouts.

## Technical Execution
The core engine (`astravital_core.py`) is written in Python 3.x and designed to run locally on spacecraft edge hardware (such as an ARM-based SBC or Raspberry Pi). It utilizes offline data structures (immutable sets, frozen tuples, and nested dictionaries) to guarantee deterministic state management without external database dependencies.

<img width="1600" height="1050" alt="AstraVital_Kiosk_Concept_Structure" src="https://github.com/user-attachments/assets/f356a511-f110-40e9-899a-b167731ffd32" />
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1050" viewBox="0 0 1600 1050" role="img" aria-labelledby="title desc">

## Interactive Frontend Prototype
[AstraVital Dashboard Prototype (HTML)](https://henrytxh.github.io/AstraVital-CHCS/)

![Dashboard Overview 1]<img width="1754" height="1240" alt="AstraVital _ Crew Health   Care System (CHCS)_page-0002" src="https://github.com/user-attachments/assets/e005fe51-b323-42b4-a641-e2ccde869d30" />

![Dashboard Overview 2](dashboard-ui-2.jpg)<img width="1754" height="1240" alt="AstraVital _ Crew Health   Care System (CHCS)_page-0002" src="https://github.com/user-attachments/assets/3ad52e34-6d46-49a9-8b3d-04079ab7770b" />

