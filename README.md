# AstraVital | Crew Health & Care System (CHCS)

AstraVital is an offline, edge-computing software application engineered for long-duration deep-space transit. Built for the NASA Space Apps Challenge, this backend engine operates completely independently of real-time Earth cloud servers to overcome deep-space communication latency.

## Core Application Features
* **Predictive Velocity Analytics:** Evaluates 7-day rate-of-change decay to proactively detect physiological deconditioning (muscle/mass loss) early.
* **UTC Window & Streak Tracking:** Synchronizes daily check-in windows to Coordinated Universal Time (UTC) to maintain protocol discipline and mitigate circadian desynchronization.
* **Encrypted Payload Compression:** Automatically encrypts and compresses crew health records into a 427-byte binary buffer, queueing data safely during orbital communication blackouts.

## Technical Execution
The core engine (`astravital_core.py`) is written in Python 3.x and designed to run locally on spacecraft edge hardware (such as an ARM-based SBC or Raspberry Pi). It utilizes offline data structures (immutable sets, frozen tuples, and nested dictionaries) to guarantee deterministic state management without external database dependencies.
