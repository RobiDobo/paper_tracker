# Summary for Digital_Methods_to_Quantify_Sensor_Output_Uncertai.pdf

Based on the provided technical details from the paper, here is the structured summary:

### 1. Core Method
* **Hardware & Architecture:** Implemented a real-time, on-device uncertainty-extended processor architecture (`UxHw`) on two RISC-V FPGA platforms (UxHw-FPGA-5k and UxHw-FPGA-17k) to deterministically propagate finite-precision calibration data errors.
* **Sensor Application:** Utilized the Melexis MLX90640 far-infrared sensor array (incorporating 768-pixel raw data, 37 calibration parameters, and dynamic compensation models) to study temperature conversion and Canny edge-detection algorithms.
* **Validation Technique:** Benchmarked on-device hardware tracking against traditional offline Monte Carlo simulations (using 500,000 iterations per pixel/scene) to quantify epistemic uncertainty caused by the quantization and rounding of pre-stored factory calibration parameters.
* **Storage Scenario Evaluation:** Tested alternative calibration-data storage formats (such as IEEE-754 32-bit FP32) to assess their impact on epistemic error reduction.

### 2. Main Conclusions
* **Uncertainty Impact:** Calibration data representation uncertainty caused significant errors in temperature outputs, yielding standard deviations ranging from 0.24 °C (center pixels at 20 °C) to 1.75 °C (corner pixels at 100 °C), maximum absolute errors up to 5.35 °C, and overall averages of 0.44 °C (MAE) and 0.53 °C (Std).
* **Computational Efficiency:** The `UxHw` hardware platforms achieved the same high statistical accuracy as brute-force Monte Carlo methods (Wasserstein distance of 0.0189 °C) while delivering massive speedups of **42.9× to 94.4×**.
* **Algorithm Improvement:** Integrating uncertainty-aware Canny edge detection demonstrated up to **5.3% higher accuracy** by effectively marginalizing calibration artifacts.
* **Storage Format Benefits:** Transitioning to higher-precision storage formats (like IEEE-754 32-bit) successfully reduced epistemic error statistics by up to **99.99%**.

### 3. Limitations / Future Work
*(Note: While the provided text extensively details the methods, data, and performance results, explicit standalone "limitations" or future work sections are not mentioned in the excerpt. However, implicit boundaries of the study include its specific focus on the Melexis MLX90640 thermopile sensor, RISC-V FPGA prototyping platforms, and factory calibration parameter quantization.)*