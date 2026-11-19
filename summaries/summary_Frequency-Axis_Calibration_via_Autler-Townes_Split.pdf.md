# Summary for Frequency-Axis_Calibration_via_Autler-Townes_Split.pdf

Based on the provided technical details from the paper "Frequency-Axis_Calibration_via_Autler-Townes_Split.pdf", here is the structured summary:

### 1. Core Method: What did they do?
* **Rydberg Atom-Based Calibration:** Developed a frequency-axis and radio-frequency (rf) field calibration method using electromagnetically induced transparency (EIT) and Autler-Townes (AT) splitting in a room-temperature rubidium vapor cell (targeting the $54D_{5/2}$ to $55P_{3/2}$ Rydberg transition at ~13.4 GHz).
* **Experimental Sweeps:** Collected extensive data ($N = 6,475$ reference traces) by varying nominal rf power from -23 dBm to -5 dBm (-8 dBm in specific trials) and rf detuning from -50 MHz to 120 MHz.
* **Modeling and Fitting:** Utilized a two-level semi-classical dressed-state model combined with weighted nonlinear least-squares regression (WNLSR) to analyze the avoided-crossing behavior of the AT-split features, fitting uncalibrated peak separations $S(\delta, P)$ as a function of detuning ($\delta$) and power ($P$) to extract scaling and calibration factors without needing narrow-line cavities.

### 2. Main Conclusions: What were the key dosimetry results?
* **High Accuracy:** The proposed AT-splitting calibration method agreed with the traditional fine-structure peak separation calibration benchmark (using $54D_{5/2}$ and $54D_{3/2}$ states separated by 73.18 MHz) to within **1.11% or better**.
* **Calibration Factor:** Yielded a mean normalized calibration factor ($C/\bar{C}_{fs}$) of **$0.9935 \pm 0.0026$** using all available data, demonstrating sub-percent variation.
* **Robustness:** The method proved robust against experimental deviations from the expected rf power dependence and imperfections in the rf power response, with fitting uncertainty estimated at 0.13% and a total estimated percent uncertainty of 0.59% when accounting for model variations.

### 3. Limitations / Future Work: What are the gaps mentioned in the text?
* **Systematic Underestimation:** The extracted calibration factor showed a small, persistent systematic underestimation from unity.
* **Experimental Deviations:** The study noted and accounted for substantial experimental deviations from the known/ideal rf power dependence ($P^n$) and sources of error such as calibration variation noise (CVN) and Gaussian curve-fitting uncertainties, which require precise mathematical compensation via WNLSR. *(Note: Beyond these noted experimental imperfections and sources of error, specific future work directions are not detailed in the provided text snippet).*