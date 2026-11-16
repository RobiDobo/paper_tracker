# Summary for ZoomSpec__A_Physics-Guided_Coarse-to-Fine_Framewor.pdf

Based on the technical details provided, here is the structured summary of the **ZoomSpec** framework:

### 1. Core Method
The authors developed **ZoomSpec**, a physics-guided, coarse-to-fine deep learning framework designed for wideband spectrum sensing and radio signal detection. The core methodology involves:
*   **Log-Space STFT (LS-STFT):** Replaces standard linear spectrograms with a log-space representation to ensure constant relative frequency resolution, significantly enhancing the visibility of narrowband signals.
*   **Adaptive Heterodyne Low-Pass (AHLP) Module:** A physics-guided DSP operator that performs center-frequency alignment, bandwidth-matched filtering, and signal decimation on I/Q data.
*   **Dual-Domain Pipeline:** A two-stage detection process where an initial coarse detection (using YOLOv11n) triggers the AHLP module to extract and "purify" specific signal candidates for final high-precision classification.

### 2. Main Conclusions
*   **Superior Performance:** The framework achieved a state-of-the-art **78.1 mAP@0.5:0.95** on the SpaceNet dataset.
*   **Narrowband Recall:** The use of log-space spectral representations led to a significant improvement in narrowband signal recall, increasing from **31% to 89%**.
*   **Efficiency:** By fusing I/Q data with LS-STFT spectral features, the framework effectively minimizes background interference and optimizes the detection of weak signals, demonstrating that computational resources are better spent on log-space representations rather than standard linear processing.

### 3. Limitations / Future Work
*   **Non-Applicability to Dosimetry:** The authors explicitly clarify that the study is focused on **radio spectrum monitoring and signal detection**, not non-ionizing radiation dosimetry (e.g., measuring power density or Specific Absorption Rates/SAR). 
*   **Scope Constraints:** The paper does not provide dosimetry-specific data or metrics. Consequently, there are no reported results regarding human EMF exposure or health-related safety assessments.
*   **Gaps:** While the text highlights the success of the dual-domain architecture in signal recognition, it acknowledges that the framework is purpose-built for spectral situational awareness, implying that its application to other domains (like dosimetry) would require a fundamentally different approach or additional experimental validation not present in the current study.