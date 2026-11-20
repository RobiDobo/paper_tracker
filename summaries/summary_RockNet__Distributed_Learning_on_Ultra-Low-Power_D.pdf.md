# Summary for RockNet__Distributed_Learning_on_Ultra-Low-Power_D.pdf

Based on the technical details provided, here is the structured summary of the document:

### 1. Core Method
The authors developed **RockNet**, a distributed learning framework designed to perform time-series classification on resource-constrained, ultra-low-power Cyber-Physical Systems (CPS). The method involves:
*   **Algorithm Distribution:** Distributing the **ROCKET** (Random Convolutional Kernel Transform) algorithm across multiple IoT devices.
*   **Parallelization:** Dividing the feature space transformation across a network of devices to optimize computational load.
*   **Optimization:** Utilizing an efficient multi-hop wireless communication protocol and data quantization to overcome memory and energy constraints on hardware (specifically the nRF52840 microcontroller).

### 2. Main Conclusions
The paper does **not** contain any results related to dosimetry. The key performance findings are strictly related to computational and communication efficiency:
*   **Memory Efficiency:** Achieved a 93% reduction in per-device memory usage.
*   **Latency:** Achieved an 89% reduction in latency.
*   **Energy Consumption:** Realized an 86% reduction in energy consumption when scaled to 20 devices.
*   **Accuracy:** The system maintains state-of-the-art classification accuracy for time-series data despite the distributed, resource-constrained architecture.

### 3. Limitations / Future Work
*   **Non-Dosimetric Focus:** The document focuses exclusively on TinyML, machine learning architectures, and distributed computing; it does not address non-ionizing radiation dosimetry, human exposure assessment, or Specific Absorption Rate (SAR) measurements. 
*   **Data Distribution:** The authors performed an ablation study evaluating the performance of the system under both **i.i.d. (independent and identically distributed)** and **non-i.i.d.** data distribution scenarios, suggesting that the robustness of the model under varied data distributions is a key area of current investigation.