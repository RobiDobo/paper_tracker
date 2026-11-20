# Summary for Performance_Analysis_of_a_Dual-Polarised_Bowtie_An.pdf

Based on the extracted technical details from the paper, here is the structured summary:

### 1. Core Method: What did they do?
* **Antenna Setup & Measurements:** Utilized a dual-polarised bowtie antenna (operating in the 80–320 MHz range) and rotated it in 15° steps to measure linear polarisation responses. 
* **Data Acquisition & Analysis:** Recorded power values across orthogonal elements using an RTL-SDR receiver. Fitted Malus's law ($P = A \cos^2(\theta - \phi) + B$) to the data using an Iteratively Reweighted Least Squares (IRLS) algorithm to determine source polarisation angles, Cross-Polarisation Discrimination (XPD), and independent linear polarisation components.
* **Simulations:** Performed simulations using 4nec2 software over a perfect ground plane at 200 MHz.
* **Filtering:** Evaluated S-parameters to characterize a notch filter for radio frequency interference (RFI) attenuation.

### 2. Main Conclusions: What were the key dosimetry results?
* *Note:* The provided text explicitly states that **there are no technical methods, data, or results regarding non-ionizing radiation dosimetry** in the paper (as the bibliographic references primarily cover antenna design, electromagnetics, software-defined radio, and numerical methods). 
* **Antenna Performance Conclusions:** 
  * Simulations showed a broad main lobe directed toward the zenith with a peak total gain of ~11.6 dBi and nulls lying ~17.6 dB below the peak at 10° elevation.
  * The orthogonal bowtie configuration successfully produced predictable figure-of-eight power variation patterns, with orthogonal linear polarisations closely following a Malus-law model ($R^2 > 0.85$).
  * XPD values hovered around or below 20 dB, indicating moderate channel leakage.
  * The notch filter exhibited strong RFI attenuation exceeding 20 dB across the 81–103 MHz frequency band.
  * Overall, the system is well-suited for low-cost undergraduate radio astronomy and polarisation-rotation measurements.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
* *Based on the provided text:* The summary highlights moderate channel leakage (indicated by XPD values around or below 20 dB), but the provided excerpts do not explicitly detail broader limitations or future work proposed by the authors.