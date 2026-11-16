# Summary for When_Magnitude_Suffices__Reconstructing_Time-Domai.pdf

Based on the provided technical details from the paper, here is the structured summary:

### 1. Core Method
* **Experimental Setup:** Utilized a vector network analyzer (VNA) and a spectrum analyzer with a tracking generator (SA) to acquire 2.0–3.0 GHz microwave S-parameters ($S_{11}$ and $S_{21}$) in an opposed two-antenna thoracic phantom setup.
* **Phantom & Permittivity Control:** Employed a controlled torso phantom with a homogeneous dielectric surrounding medium and water-ethanol-filled PLA lung compartments, varying the lung's real relative permittivity ($\varepsilon'$ from 78.0 to 47.8 across eleven states).
* **Data Processing & Machine Learning:** Applied time-domain gating (via inverse fast Fourier transform) and the Calinski-Harabasz statistic to isolate specific propagation paths. Trained a fully-connected neural network with a custom loss function (combining mean-squared error and an auxiliary ordinal/rank term) to reconstruct dielectric states, performing per-device reference corrections, VNA reference grid utilization, and gate selection.

### 2. Main Conclusions
* **Magnitude Sufficiency:** Magnitude-only SA measurements successfully replaced phase-dependent VNA measurements, avoiding the high errors linked to explicit phase reconstruction or non-causal minimum-phase assumptions.
* **Reconstruction Accuracy:** 
  * For $S_{11}$ (reflection) reconstruction, the model achieved a shape error of $0.047 \text{ dB}^2$ using VNA inputs and $0.082 \text{ dB}^2$ ($0.08 \text{ dB}^2$) using SA inputs.
  * For $S_{21}$ (transmission) reconstruction, it achieved $0.061 \text{ dB}^2$ (VNA) and $0.082 \text{ dB}^2$ (SA), successfully preserving the clustering of dielectric states.
* **Magnitude-Phase Dependency:** Reflection measurements ($S_{11}$) exhibited a much stronger magnitude-phase dependency (cross-validated $R^2$ up to 0.97) and lower reconstruction errors compared to transmission measurements ($S_{21}$), which suffered from complex propagation geometries and weaker state-ordering preservation.

### 3. Limitations / Future Work
* The evaluation is restricted to a single physical configuration on a simplified phantom.
* Generalization across diverse geometries, *in vivo* conditions, and exact quantitative physiological levels remains unverified.