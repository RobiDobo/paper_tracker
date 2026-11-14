# Summary for Rethinking_Temporal_Models_for_TinyML__LSTM_versus.pdf

**Note first:** per the extracted details, this paper has **no dosimetry content**, so the summary below reflects what is (and isn't) present.

**1. Core Method**
- TinyML benchmark study comparing **1D-CNN vs. LSTM** architectures for time-series classification.
- Tasks/datasets: human activity recognition from IMU data; ECG arrhythmia/ischemia classification from MIT-BIH and PTB.
- Deployment target: **ESP32**, evaluated under **Float32 vs. INT8 quantization**.
- Metrics reported: accuracy, RAM/Flash footprint, inference latency (e.g., 1D-CNN ≈95% accuracy, 19.85 KB RAM, 27.6 ms inference).

**2. Main Conclusions (dosimetry results)**
- **None.** There are no dosimetric results: no RF/ELF/optical field measurements, no exposure metrics (SAR, power density, induced electric field, dose-rate), no dosimetric phantoms or simulations, and no biological or exposure-assessment endpoints.
- The only conclusions supported by the extract are ML-systems findings (accuracy/memory/latency trade-offs, quantization effects), not dosimetry.

**3. Limitations / Future Work**
- The extract **does not include the authors' stated limitations or future work**, so none can be reported without inventing them.
- The only potential dosimetry link — that the low-latency, low-memory 1D-CNN could suit on-device processing in personal EMF exposure meters — is explicitly **not mentioned or evaluated by the authors**; it is an external inference, not an author-identified gap or future direction.

**Bottom line:** This source cannot support dosimetry-specific conclusions; it is a model-architecture/quantization benchmark for edge deployment only.