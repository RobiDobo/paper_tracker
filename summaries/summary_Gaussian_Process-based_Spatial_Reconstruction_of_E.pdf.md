# Summary for Gaussian_Process-based_Spatial_Reconstruction_of_E.pdf

Based on the extracted technical details from the paper, here is a structured summary of the study:

### 1. Core Method
* **Algorithm:** Implemented a **Gaussian Process (GP) regression** model for the spatial reconstruction of electromagnetic (EM) fields.
* **Physics-Informed Approach:** Enhanced the GP framework by incorporating a **physics-informed mean function** proportional to the inverse-square distance decay from the EM source, replacing a standard zero-mean assumption.
* **Covariance & Optimization:** Utilized a **2-D Matérn covariance function ($\nu = 3/2$)** (which outperformed the Squared Exponential covariance function) to model spatial correlation. Hyperparameters (length-scales, signal variance, and noise variance) were optimized using **Maximum A Posteriori (MAP) estimation** via marginal likelihood maximization.
* **Data & Simulation:** Generated training datasets consisting of **2,401 spatial observation points** on a $49 \times 49$ grid within a simulated $25\,\text{m}^2$ room at $900\,\text{MHz}$ (incorporating up to three wave reflections) using the **SIMUEM3D** tool. Real-time communication utilized the **Open Sound Control (OSC)** protocol.
* **Sensor Sparsity:** Evaluated the reconstruction of unobserved field intensities using sparse sensor networks (specifically testing 9, 30, 30, and 100 observation points/sensors corrupted by independent Gaussian noise).

### 2. Main Conclusions
* **Performance of Physics-Informed Priors:** The physics-informed mean function significantly outperformed the zero-mean assumption, achieving a lower **Normalized Mean Square Error (NMSE of 0.3763 vs. 0.4780)** and higher correlation using data from only **9 sensors**.
* **Impact of Sensor Density:** Increasing sensor density dramatically improved spatial reconstruction accuracy. Expanding from 9 sensors to **100 observation points** reduced the NMSE to **0.1177**.
* **Uncertainty Quantification:** The GP framework successfully provided both the best estimate (posterior predictive mean) and estimation uncertainty metrics (posterior covariance) for unobserved test locations across the room.
* **Kernel Suitability:** The Matérn covariance function proved superior to the Squared Exponential covariance function in handling high-dimensional spatial inputs for EM field reconstruction.

### 3. Limitations / Future Work
*(Note: Explicit future work or limitation statements are not detailed in the provided text excerpts, other than the inherent trade-off between sensor sparsity/low-complexity algorithms and the necessity of higher sensor densities (e.g., 100+ points) to achieve lower error rates like an NMSE of 0.1177.)*