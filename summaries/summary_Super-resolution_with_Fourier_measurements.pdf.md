# Summary for Super-resolution_with_Fourier_measurements.pdf

Based on the provided technical details from the paper, here is the structured summary:

### 1. Core Method
* **Measurement & Analysis Framework:** The study utilizes classical Fisher Information (FI) calculations, Cramér-Rao bounds, and Fourier-plane intensity measurements (assuming shot noise-limited Poisson statistics) to quantify the precision of sub-Rayleigh source separation.
* **Techniques:** It incorporates phase-sensitive modal projections—such as Hermite-Gauss mode sorting—without altering canonical imaging setups, enabling the evaluation of sub-Rayleigh spatial and temporal separations for point sources.

### 2. Main Conclusions (Note on Dosimetry)
* *Note on Dosimetry:* As explicitly stated in the provided text, the paper focuses entirely on quantum optics, sub-diffraction imaging, and spatial super-resolution metrology; **it contains no technical methods, data, or results related to non-ionizing radiation dosimetry.** 
* **Super-Resolution Performance (Optics):** By measuring intensity in the Fourier plane, the system successfully evades "Rayleigh’s curse." It yields a non-zero Fisher information in the sub-Rayleigh limit for complex coherence ($\phi \neq \{0, \pi\}$), thereby outperforming direct image-plane imaging.
* **Scaling & Robustness:** For coherent multi-source constellations, the Fisher Information scales linearly with the number of sources ($N$), demonstrating that Fourier-plane measurements saturate quantum Cramér-Rao bounds while maintaining optimal performance and immunity against static/dynamic object-scene misalignments or centroid jitters.

### 3. Limitations / Future Work
* *From the Provided Text:* The provided text does not explicitly detail specific limitations or future work gaps mentioned by the authors, as the excerpts focus strictly on the successful derivation and performance metrics of the Fourier-plane Fisher information framework.