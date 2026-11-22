# Summary for Time-resolved_sensing_of_electromagnetic_fields_wi.pdf

Based on the provided technical details from the paper, here is the structured summary:

### 1. Core Method: What did they do?
* **Quantum Sensing Architecture:** Utilized a single-electron Fabry-Perot interferometer (FPI) operating in the weak-backscattering regime within a GaAs/AlGaAs two-dimensional electron gas (at a dilution refrigerator temperature of 30 mK, with an electronic temperature of 25 mK).
* **Signal Generation & Probe:** Injected single-electron quantum wavepackets (specifically Leviton wavepackets with durations $\tau_e \simeq 35\text{--}150\text{ ps}$) to detect fast time-dependent AC voltages and electromagnetic fields applied to a plunger gate.
* **Theoretical & Analytical Framework:** Applied a time-dependent single-particle scattering approach, edge-magnetoplasmon scattering theory (bosonization formalism), and convolution models to map interference currents and phase modulations.
* **Calibration:** Calibrated charge lever arms ($\alpha = 1.81 \times 10^{-4}\text{ V}$) and excess shot noise ($\Delta S = 2eI_{\text{in}}$) using cryogenic tank circuits and lock-in amplification. Square-wave gate drives were calibrated via transmission-flattening points, factoring in pulse deformation with an exponential rise time ($\tau_r = 140\text{ ps}$).

### 2. Main Conclusions: What were the key dosimetry results?
* **High-Resolution Field Sensing:** Successfully demonstrated simultaneous probing of electromagnetic field amplitudes (via the phase shift of the interference pattern) and field fluctuations (via reductions in interference contrast).
* **Sensitivity Metrics:** Achieved a voltage sensitivity/resolution in the tens of microvolts range ($\sim$50 µV), corresponding to the detection of a few microwave photons, and evaluated zero-point voltage fluctuations induced by single photons ($V_{1\mathrm{ph}} \approx 4\text{ }\mu\text{V}$ in a 50 $\Omega$ characteristic impedance line).
* **Temporal Resolution:** Reached a temporal resolution down to a few tens of picoseconds.
* **Quantum Nature of Detection:** Reductions in interference contrast successfully demonstrated the quantum nature of the detection process, reflecting phase spreading driven by the quantum position fluctuations of single electrons.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
*(Note: While the provided text segments do not explicitly feature a dedicated "future work" or "limitations" section, the technical parameters highlight the physical constraints of the current system):*
* **Resolution Constraints:** The temporal resolution is fundamentally limited by the electronic wavepacket width ($\tau_e \approx 35\text{--}113\text{ ps}$) and the rise time of the applied square voltage pulses ($\tau_r = 140\text{ ps}$). 
* **Interaction Effects:** The necessity to account for edge-magnetoplasmon scattering, Coulomb interactions, and pulse deformations indicates that stray capacitance and many-body interactions in ballistic quantum Hall setups constrain ideal time-resolved measurements, requiring complex bosonization and convolution models to accurately interpret data.