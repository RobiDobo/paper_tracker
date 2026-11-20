# Summary for StormWave__An_Open-Source_Portable_SDR_Platform_fo.pdf

Based on the provided technical details, here is the structured summary for the "StormWave" platform:

### 1. Core Method
The authors developed and deployed "StormWave," an open-source, portable Software-Defined Radio (SDR) platform designed specifically for research into RF interference. The system is capable of generating and monitoring signals across a frequency range of 70 MHz to 6 GHz. The experimental methodology focused on evaluating communication link degradation under various interference waveforms (e.g., HORNet, OFDM, OTFS) at gain levels ranging from 5 to 25 dB. System performance was measured using metrics such as throughput, Access Symbol Error Rate (ASER), and Kullback-Leibler Divergence (KLD), with a specific emphasis on the platform's ability to execute sub-microsecond waveform switching.

### 2. Main Conclusions
The research establishes that communication link disruption is highly sensitive to the interaction between the interference waveform and the physical environment. Key findings include:
*   **Environmental Impact:** Link degradation is significantly influenced by multipath propagation and the physical proximity of the interference source to the target link.
*   **Waveform Sensitivity:** Disruption patterns vary based on the specific time-frequency spreading characteristics of the waveforms used.
*   **Operational Capability:** The platform successfully demonstrated high-precision, sub-microsecond waveform switching, proving its viability as a tool for electronic warfare and signal interference testing.
*   *Note on Dosimetry:* The study does not provide results pertaining to non-ionizing radiation dosimetry, SAR, or human exposure assessment.

### 3. Limitations / Future Work
While the provided text focuses on the platform's utility in electronic warfare and network security, the following gaps and implicit considerations can be drawn:
*   **Lack of Safety/Dosimetry Data:** The research does not address technical methods for quantifying biological exposure or compliance with non-ionizing radiation safety standards.
*   **Environment Dependency:** Because link degradation is highly sensitive to multipath and physical surroundings, future work likely requires further validation in more diverse or complex RF environments to ensure consistent performance.
*   **Application Scope:** The platform is currently optimized for signal interference and network security research; further development would be required to adapt the hardware for applications involving human-centric RF safety monitoring or compliance testing.