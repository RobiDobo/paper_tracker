# Summary for Coordinated_Electromagnetic_Side-Channel_Attacks_f.pdf

Based on the provided technical details from the paper, here is the final structured summary:

### 1. Core Method: What did they do?
* **Experimental Setup:** Used an Ettus USRP B200 software-defined radio (SDR) receiver paired with an HDTV antenna placed 45 cm away, separated by a masonry wall, to capture unintentional electromagnetic emissions.
* **Signal Modeling & Resynchronization:** Modeled video leakage using pixel-clock harmonics and pulse-shaping functions ($x(t) = \sum x[n]p(t-nT_p)$). They leveraged public hardware specifications to narrow the frequency search space and resynchronize the intercepted signals.
* **Target Scenario:** Targeted display configurations reproducing the official Brazilian e-voting interface (resolutions of 1280 × 720 pixels at a 60 Hz refresh rate, with a pixel rate near 39.79 MHz). 

### 2. Main Conclusions: What were the key dosimetry/emissions results?
* **Emission Identification:** Successfully identified a compromising electromagnetic emission band centered at the **fifth harmonic (371.25 MHz)** of the pixel rate for the targeted 1280×720@60 display configuration.
* **Reconstruction Feasibility:** Proved that an adversary can successfully intercept and visually reconstruct displayed e-vote frames (through-wall vote reconstruction) in real time to observe voter selections, confirming the high viability of TEMPEST attacks against such systems.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
*(Note: While specific limitations/future work text was not explicitly detailed in the provided excerpt, typical gaps in this domain generally include factors such as the impact of varying physical distances, shielding effectiveness, environmental noise, and the complexity of applying these SDR-based resynchronization techniques dynamically against newer, heavily shielded display interfaces or higher-resolution monitors.)*