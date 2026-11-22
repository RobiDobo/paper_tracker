# Summary for GBSense__A_GHz-Bandwidth_Compressed_Spectrum_Sensi.pdf

Based on the provided technical details from the paper, here is the final structured summary:

### 1. Core Method: What did they do?
* **Architecture & Sampling:** The GBSense system implements a wideband compressed spectrum sensing architecture that replaces traditional analog delay lines and high-speed Nyquist-rate ADCs with a time-interleaved analog-to-digital conversion (TI-ADC) technique. 
* **Hardware & Clocking:** It utilizes a 1-to-8 power splitter, an 8-channel ADC array for periodic non-uniform sampling (PNS), an FPGA for JESD204B data realignment and decimation, and a two-layer PLL network to generate synchronized 50 MHz sampling clocks (achieving a 250 ps minimum clock phase offset resolution).
* **Processing & Formulation:** The system processes RF signals with a 2 GHz bandwidth (1 GHz baseband I/Q) at an average sub-Nyquist sampling rate of 400 MHz (400 MSps). Mathematically, the signal reconstruction is formulated as a multiple measurement vectors (MMV) problem ($X = A\Theta$), utilizing compressed sensing recovery algorithms and a low-power Raspberry Pi processor for real-time processing (~30 ms per frame).

### 2. Main Conclusions: What were the key dosimetry results?
* *Note on Dosimetry:* The provided text **does not contain any dosimetry methods, biological interaction data, or non-ionizing radiation safety results**. 
* **Spectrum Sensing Performance:** The key operational and performance results demonstrate that the GBSense system achieves:
  * **100% accurate spectrum detection** when spectrum occupancy is below 100 MHz.
  * **Over 80% detection accuracy/confidence** for spectrum occupancy up to 200 MHz.
  * An RMS jitter of 269.174 femtoseconds in the clock distribution circuit, yielding an SNR ceiling of approximately 55 dB.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
* *Note on Gaps:* The provided text focuses strictly on the hardware architecture, mathematical formulations, and functional lab test results, and **does not explicitly state specific limitations or future work gaps** within the excerpted details. (The text only notes that the mathematical section does not cover dosimetry or biological interactions, but this is a structural note rather than an author-stated research gap).