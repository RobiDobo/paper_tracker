# Summary for Energy_Measurement_and_Optimization_of_TinyML_in_R.pdf

Based on the provided details, here is the structured summary of the paper:

### 1. Core Method
The authors conducted a **systematic mapping study** to analyze the state of energy-aware research in TinyML on resource-constrained devices. By synthesizing data from 25 selected studies (2020–2026), they categorized research based on:
*   **Measurement Methodologies:** Direct hardware measurement (e.g., power profilers like PPK2), analytical estimation, inference-time assessment, and simulation/modeling.
*   **Optimization Strategies:** Techniques such as model compression (quantization and pruning), hardware-aware design, communication protocols, and data processing strategies.
*   **Performance Metrics:** Analysis of how variables like latency, memory footprint, and model accuracy correlate with energy consumption (specifically energy-per-inference).

### 2. Main Conclusions
*   **Lack of Standardization:** There is a significant lack of standardized procedures for measuring and reporting energy consumption in TinyML, which hinders the reproducibility and direct comparison of results across different platforms.
*   **Measurement Trends:** Direct physical measurement is the most common methodology, yet findings are often presented inconsistently (e.g., reporting total energy vs. average power vs. energy-per-inference).
*   **Technical Influencers:** Energy consumption is heavily dictated by the interaction between model architecture, numerical precision, input data characteristics, and communication overhead.

### 3. Limitations / Future Work
*   **Heterogeneity of Reporting:** The current inconsistency in reporting metrics obscures the true impact of hardware-algorithm interactions.
*   **Need for Benchmarking:** The authors recommend the adoption of **normalized metrics**—specifically **energy-per-inference**—to better evaluate the trade-off between performance and battery autonomy.
*   **Experimental Design:** There is a need for unified benchmarks and more isolated, rigorous experimental designs to clarify the energy trade-offs inherent in different model optimization strategies.

***

**Note on Dosimetry:** As specified in the source text provided, this paper focuses exclusively on computational energy consumption for embedded systems and contains **no technical methods, data, or results related to non-ionizing radiation dosimetry.**