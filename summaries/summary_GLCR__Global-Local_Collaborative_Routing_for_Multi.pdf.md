# Summary for GLCR__Global-Local_Collaborative_Routing_for_Multi.pdf

Based on the technical details provided, here is the structured summary:

### 1. Core Method
The authors introduce **GLCR (Global–Local Collaborative Routing)**, a two-stage, energy-efficient routing architecture designed to dispatch electromagnetic signals to specialized experts in a heterogeneous signal processing pool. The method operates as follows:
*   **Global Routing:** A lightweight 1D-CNN (featuring an additive-margin head) performs initial primary classification.
*   **Local Re-evaluation:** A "trigger-and-specialist" mechanism activates when the global router identifies potential "confusion-pair" ambiguities. This specialist uses four physical Digital Signal Processing (DSP) statistics—**noncircularity magnitude, spectral centroid, spectral flatness, and amplitude kurtosis**—processed through a **Histogram-based Gradient Boosting (HGBT)** classifier to resolve misclassifications.
*   **Benchmark:** The framework was validated on **HeteroSignal-7**, a custom benchmark comprising 140,000 samples across seven electromagnetic signal tasks (AMC, SD, WII, RFFI, RWC, and BSS).

### 2. Main Conclusions
*   **Performance:** GLCR achieved a routing accuracy of **96.16%** and a system score of **76.30%**, outperforming 19 baseline models.
*   **Efficiency:** The architecture significantly reduced computational overhead, achieving a **5.9x reduction in system FLOPs** compared to executing all experts, with a low latency of **1.43 ms per sample**.
*   **Utility:** The study demonstrates that a cascaded routing approach allows for the effective orchestration of frozen, task-specific expert models without the need for extensive model retraining.
*   **Note on Dosimetry:** The provided documentation explicitly states that the paper **does not contain information regarding non-ionizing radiation dosimetry** or related experimental results.

### 3. Limitations / Future Work
*   **Research Focus:** The provided text notes that the concluding sections of the paper focus exclusively on future developments for **Automatic Modulation Classification (AMC) routing protocols**. 
*   **Gaps:** While the paper addresses efficient signal routing and expert orchestration, the source material focuses on the intersection of deep learning and signal processing, rather than radiation dosimetry or biological impact studies. Future work is concentrated on refining the routing protocols within the signal processing domain.