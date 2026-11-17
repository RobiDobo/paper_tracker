# Summary for PRISM-AMC__Replay-Free_Continual_Learning_for_Auto.pdf

Based on the technical details provided, here is the structured summary of the document:

### 1. Core Method
The paper introduces **PRISM-AMC**, a replay-free continual learning framework designed for Automatic Modulation Classification (AMC). The method focuses on mitigating "catastrophic forgetting" in neural networks—where a model loses performance on previously learned tasks when trained on new ones—without the need to store or "replay" previous training data. 
*   **Technical Approach:** The authors utilize a 1-D Convolutional Neural Network (CNN) architecture. 
*   **Gradient Management:** The method employs gradient projection memory via Singular Value Decomposition (SVD) of layer activation matrices. This identifies "Core" and "Residual" gradient spaces, ensuring that updates for new tasks are projected into subspaces that do not interfere with the learned parameters of previous tasks.
*   **Uncertainty Estimation:** The framework incorporates Monte Carlo (MC) dropout to quantify epistemic uncertainty, allowing the model to detect Out-of-Distribution (OOD) signals.

### 2. Main Conclusions
*   **Dosimetry Results:** None. As noted in the extraction, the paper contains no dosimetry content, RF exposure metrics, SAR/power-density quantities, or biological dose-response data.
*   **Convergence:** The authors provide theoretical convergence bounds (Theorem 2) for the PRISM-AMC optimizer, demonstrating that the projected gradient norm approaches zero ($O(1/\sqrt{N})$) as the number of iterations ($N$) increases, for a fixed communications signal-to-noise ratio ($\gamma$).
*   **Performance:** In comparative evaluations, the model demonstrated strong OOD-detection capability for specific modulation types (BPSK/PAM4/8PSK/QAM64, with AUROC 0.916–0.971), though performance was significantly lower for other modulation formats (WBFM, GFSK, QAM16, AM-SSB, AM-DSB, with AUROC 0.484–0.540).

### 3. Limitations / Future Work
*   **OOD Detection Sensitivity:** The significant disparity in AUROC performance between different modulation classes suggests that the current MC-dropout approach for uncertainty estimation is not uniformly robust across all signal types.
*   **Computational/Structural Gaps:** While the paper addresses replay-free learning, future work in this domain typically involves optimizing the efficiency of the SVD-based gradient projection as network depth increases, and extending the framework to handle non-stationary wireless environments where signal conditions fluctuate more dynamically than those presented in the MIGOU and DeepSig 2018.01A datasets.