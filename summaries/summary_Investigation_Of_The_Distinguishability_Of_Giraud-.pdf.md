# Summary for Investigation_Of_The_Distinguishability_Of_Giraud-.pdf

Based on the provided text, the study focuses exclusively on cryptographic side-channel analysis (SCA) and hardware security (specifically electromagnetic emissions during elliptic curve cryptography), rather than non-ionizing radiation dosimetry. 

Here is the structured summary based on the actual scope of the provided text:

### 1. Core Method: What did they do?
* **Experimental Setup:** Implemented the Giraud-Verneuil atomic pattern using the NIST P-256 elliptic curve and the FLECC cryptographic library on a Texas Instruments LAUNCHXL-F28379D microcontroller (operating at 100 MHz).
* **EM Data Acquisition:** Captured high-resolution single-trace electromagnetic (EM) emissions during scalar multiplication ($kP$) using a Langer ICS 105 IC scanner, an MFA-R 0.2-75 near-field probe, and a LeCroy WavePro 604HD oscilloscope at a 5 GS/s sampling rate.
* **Signal Processing & Analysis:** Used software breakpoints, NOP instruction loops, and cross-correlation techniques to align sub-traces. Evaluated distinguishability between atomic blocks (Doubling, Addition 1, Addition 2) by systematically identifying and removing extraneous 1-cycle and 5-cycle background clock processes.

### 2. Main Conclusions: What were the key results?
* **Impact of Background Processes:** The presence of extraneous 1-cycle and 5-cycle clock processes introduced desynchronization, phase drift, and visible amplitude gaps that rendered atomic blocks distinguishable in EM traces.
* **Effectiveness of Atomicity:** Removing these background clock cycles successfully synchronized the atomic blocks and eliminated distinguishable gaps in the amplitude threshold tests, demonstrating that atomicity alone is insufficient for complete side-channel security without rigorous control over background microarchitectural clock cycles.
* **Constant-Time Execution:** Confirming constant-time execution behavior, the FLECC library showed that full removal of these microarchitectural shifts renders the atomic pattern resistant to the applied horizontal SCA.

### 3. Limitations / Future Work: What are the gaps mentioned?
*(Note: The provided text excerpts focus heavily on experimental execution, comparative evaluations against prior works like Sigourou et al., and cryptographic side-channel metrics rather than explicitly detailing future work or limitations. However, the findings inherently point to the necessity of accounting for low-level microarchitectural clock variations when designing leakage-resilient cryptographic hardware/software.)*