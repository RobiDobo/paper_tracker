# Summary for picoRing__battery-free_rings_for_subtle_thumb-to-i.pdf

Based on the technical details provided, here is the structured summary for **picoRing**:

### 1. Core Method
The researchers developed **picoRing**, a battery-free wearable interface that utilizes **Passive Inductive Telemetry (PIT) at 27 MHz** to enable communication between a ring and a wristband. The system relies on a weak inductive field, with design optimizations—such as a 5 cm-diameter wristband coil—that successfully extended the stable communication range to 13 cm. The system is designed for subtle thumb-to-finger interactions (press, slide, joystick, and scroll).

### 2. Main Conclusions
*   **Performance Stability:** The system is robust against common environmental and physiological interference. Dosimetry evaluations confirmed that human hand interference has a negligible impact on the Signal-to-Noise Ratio (SNR).
*   **Reliability:** The system remains stable during finger bending (30–70°) and is unaffected by proximity to metallic objects.
*   **Interaction Accuracy:** Recognition accuracy is highly dependent on SNR. The system maintained an average SNR above 10 dB. Specifically, the "press" input achieved 99.7% accuracy at 11–13 dB SNR, which dropped to 93.3% as the SNR approached the 10 dB threshold.

### 3. Limitations / Future Work
*   *Note:* The provided text focuses primarily on the technical implementation and performance validation of the telemetry system. It does not explicitly list specific "future work" or "limitations" sections. However, the data implies a **sensitivity threshold**—as SNR drops toward 10 dB, recognition accuracy significantly degrades—suggesting that maintaining a high SNR remains a critical design constraint for future scaling or miniaturization of the hardware.