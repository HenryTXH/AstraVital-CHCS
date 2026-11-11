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
  <title id="title">AstraVital open-front kiosk concept, isometric view</title>
  <desc id="desc">A conceptual wall-mounted open-front kiosk with display, simulated ID selection, optional wearable data dock and local computer/power modules. It is not a sealed pod or flight-ready design.</desc>
  <defs>
    <marker id="leader" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#53deeb"/></marker>
    <style>
      .bg{fill:#071426}.title{font:700 34px Arial,sans-serif;fill:#fff}.sub{font:18px Arial,sans-serif;fill:#b9d3df}
      .front{fill:#112844;stroke:#53deeb;stroke-width:4}.side{fill:#0c1d32;stroke:#53deeb;stroke-width:4}.top{fill:#193654;stroke:#53deeb;stroke-width:4}
      .screen{fill:#071426;stroke:#6ce6ec;stroke-width:4}.part{fill:#1a3855;stroke:#9bb6c9;stroke-width:2}.edge{fill:none;stroke:#53deeb;stroke-width:3;marker-end:url(#leader)}
      .txt{font:700 18px Arial,sans-serif;fill:#f3f9fc}.small{font:15px Arial,sans-serif;fill:#c7dbe5}.call{font:700 16px Arial,sans-serif;fill:#ffd27d}.foot{font:15px Arial,sans-serif;fill:#9fb8c7}
    </style>
  </defs>
  <rect class="bg" width="1600" height="1050" rx="24"/>
  <text class="title" x="70" y="70">ASTRAVITAL | OPEN-FRONT KIOSK CONCEPT</text>
  <text class="sub" x="70" y="105">Isometric illustration for communicating software touchpoints; not an engineering drawing</text>

  <!-- bulkhead mounting concept; bracket geometry and load rating not engineered -->
  <path d="M520 240 L1110 370 L1110 885 L520 755 Z" fill="none" stroke="#29445e" stroke-width="10" stroke-dasharray="15 10"/>
  <path d="M550 275 L605 287 L605 772 L550 760 Z" class="part"/>
  <path d="M1045 385 L1100 397 L1100 885 L1045 873 Z" class="part"/>

  <!-- kiosk shell: open front with side privacy panel, no sealed cabin -->
  <polygon class="top" points="590,230 940,150 1160,245 805,330"/>
  <polygon class="side" points="940,150 1160,245 1160,770 940,675"/>
  <polygon class="front" points="590,230 940,150 940,675 590,755"/>
  <path d="M590 755 L940 675 L1160 770 L805 855 Z" fill="#0a1a2c" stroke="#53deeb" stroke-width="4"/>

  <!-- interaction panel on the front -->
  <polygon class="screen" points="650,300 866,252 866,440 650,488"/>
  <text class="txt" x="758" y="326" text-anchor="middle" transform="rotate(-12 758 326)">ASTRAVITAL</text>
  <text class="small" x="758" y="356" text-anchor="middle" transform="rotate(-12 758 356)">Check-in · trend · next step</text>
  <path d="M680 390 L712 390 L730 370 L748 410 L770 380 L790 390 L835 390" fill="none" stroke="#53deeb" stroke-width="5"/>
  <polygon class="part" points="650,523 748,501 748,550 650,572"/>
  <text class="small" x="699" y="543" text-anchor="middle" transform="rotate(-12 699 543)">BADGE TAP / ROSTER ID</text>
  <polygon class="part" points="770,496 866,474 866,528 770,550"/>
  <text class="small" x="817" y="516" text-anchor="middle" transform="rotate(-12 817 516)">HELP / GUIDE</text>
  <polygon class="part" points="663,618 854,575 854,635 663,678"/>
  <text class="small" x="758" y="619" text-anchor="middle" transform="rotate(-12 758 619)">OPTIONAL DATA DOCK</text>

  <!-- local compute/power service panel, right face -->
  <polygon class="part" points="981,314 1115,372 1115,470 981,412"/>
  <text class="small" x="1048" y="381" text-anchor="middle" transform="rotate(24 1048 381)">LOCAL COMPUTER</text>
  <text class="small" x="1048" y="414" text-anchor="middle" transform="rotate(24 1048 414)">+ DATA STORAGE</text>
  <polygon class="part" points="981,505 1115,563 1115,620 981,562"/>
  <text class="small" x="1048" y="552" text-anchor="middle" transform="rotate(24 1048 552)">POWER MODULE</text>
  <circle cx="1074" cy="674" r="10" fill="#53deeb"/><circle cx="1110" cy="690" r="10" fill="#ffd27d"/>

  <!-- labels / leaders -->
  <path class="edge" d="M390 255 H525 L649 342"/><text class="call" x="85" y="250">1. USER DISPLAY</text><text class="small" x="85" y="278">Large text + step-by-step guide</text>
  <path class="edge" d="M390 425 H520 L649 545"/><text class="call" x="85" y="420">2. BADGE / ID INPUT</text><text class="small" x="85" y="448">Reader is conceptual; roster ID is selected in software</text>
  <path class="edge" d="M390 620 H520 L660 645"/><text class="call" x="85" y="615">3. OPTIONAL DATA LINK</text><text class="small" x="85" y="643">Only after source/device choice</text>
  <path class="edge" d="M1215 350 H1370"/><text class="call" x="1225" y="320">4. OPEN-FRONT BAY</text><text class="small" x="1225" y="380">Not a sealed capsule; airflow</text><text class="small" x="1225" y="405">and host layout require review</text>
  <path class="edge" d="M1215 550 H1370"/><text class="call" x="1225" y="520">5. SERVICE MODULES</text><text class="small" x="1225" y="580">Local computer, storage, power</text><text class="small" x="1225" y="605">Voltage/current interface TBD</text>
  <path class="edge" d="M1000 836 V920 H1370"/><text class="call" x="1225" y="890">6. HABITAT MOUNT</text><text class="small" x="1225" y="920">Mounting brackets + restraint anchors</text><text class="small" x="1225" y="945">shown conceptually only; loads / geometry unengineered</text>

  <rect x="75" y="820" width="850" height="125" rx="16" fill="#2c2631" stroke="#ffbd59" stroke-width="2"/>
  <text class="call" x="100" y="855">SCOPE / SAFETY LIMIT</text>
  <text class="small" x="100" y="885">No camera or medical tests. Brackets and restraint anchors are illustrative, not engineered.</text>
  <text class="small" x="100" y="914">Status: CHECK-IN COMPLETE · TREND TO REVIEW · DATA INCOMPLETE. Host power TBD.</text>
  <text class="foot" x="75" y="1000">AstraVital concept only · NASA association is contextual research, not endorsement or flight qualification.</text>
</svg>

![Upl<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-labelledby="t d">


oading AstraVital_OpenFront_Kiosk_Dashboard_Concept.svg…]()

