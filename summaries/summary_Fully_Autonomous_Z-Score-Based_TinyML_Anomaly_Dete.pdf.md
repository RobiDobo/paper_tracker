# Summary for Fully_Autonomous_Z-Score-Based_TinyML_Anomaly_Dete.pdf

Based on the technical details provided in the paper excerpt, here is the structured summary:

1. **Core Method**: 
   The authors developed a fully autonomous, on-device TinyML anomaly detection system using an STM32-based microcontroller (ARM Cortex-M4) and an ACS712 Hall-effect current sensor. The system captures power side-channel data via high-frequency, interrupt-driven ADC sampling of a 60 Hz AC waveform, aggregates it into 1000-sample blocks for RMS calculation, and extracts 5-dimensional feature vectors (RMS current, mean RMS, standard deviation, slope, and ON-duration). It then evaluates these features in real-time using a lightweight Z-score statistical model.

2. **Main Conclusions**: 
   *Note: As noted in the excerpt, the paper focuses entirely on electrical power consumption anomaly detection rather than radiation dosimetry; therefore, no dosimetry results exist.* 
   Regarding anomaly detection performance, the system achieved flawless results with a Precision and Recall of 1.00. It proved highly efficient for resource-constrained environments, operating with inference latencies of tens of microseconds while maintaining a minimal footprint of approximately 3.3 KB of SRAM and 63 KB of Flash memory.

3. **Limitations / Future Work**: 
   *The provided excerpt does not explicitly detail the limitations or future work mentioned by the authors.*