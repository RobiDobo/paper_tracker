# Summary for Observations_Drift__Structures_Remain__Structural_.pdf

Based on the technical details provided, here is the structured summary of the paper:

### 1. Core Method
The authors propose a self-supervised pretraining framework designed to solve "observation-biased pretraining" in electromagnetic (EM) signal modeling. Instead of relying on standard raw waveform reconstruction—which forces models to learn environment-specific noise and artifacts—the framework implements:
*   **Structural Pretraining with Time Alignment:** Utilizing **RoPE-fs** (Physical-Time-Aware Rotary Positional Encoding) to normalize temporal coordinates, allowing the model to handle heterogeneous sampling rates effectively.
*   **Multi-level Structural Unit Prediction:** Replacing waveform reconstruction with the prediction of discrete "atomic" units (derived via K-Means clustering) and "emergent" structural units (mined via Byte Pair Encoding).
*   **Semantic Robustness Evaluation:** Using cosine similarity analysis to measure the model's ability to maintain semantic identity across different acquisition conditions and signal perturbations.

### 2. Main Conclusions
*   **Mitigation of Bias:** The structural supervision approach successfully reduces the model’s dependence on dataset-specific appearances and temporal mismatches.
*   **Performance Gains:** The methodology significantly improves cross-task transferability and performance in few-shot downstream tasks, such as modulation classification and interference identification.
*   **Robustness:** The integration of RoPE-fs provides superior temporal-scale invariance, allowing the model to generalize better across varying sampling rates compared to baseline reconstruction-based models (e.g., EMind and SpectrumFM).
*   **Dosimetry Note:** The study contains **no results pertaining to non-ionizing radiation dosimetry** (SAR or power density). The "dosimetry" in this context is strictly metaphorical, referring to the "robustness and structural consistency" of the signal representation.

### 3. Limitations / Future Work
*   **Persistent Biases:** The authors acknowledge that despite the proposed improvements, observation-biased representations still persist to some degree in reconstruction-pretrained encoders.
*   **Generalization Gaps:** While the model improves performance under signal perturbations and heterogeneous sampling, there is a noted need for further research into narrowing the gap between simulated pretraining data and complex, real-world field acquisition conditions.
*   **Scope:** Future work may involve expanding the "atomic/emergent" dictionary construction to capture more complex, high-dimensional signal behaviors that might currently be ignored by the K-Means and BPE processes.