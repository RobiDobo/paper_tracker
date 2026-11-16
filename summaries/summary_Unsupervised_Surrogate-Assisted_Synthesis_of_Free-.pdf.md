# Summary for Unsupervised_Surrogate-Assisted_Synthesis_of_Free-.pdf

**1. Core Method**  
- Developed a surrogate‑assisted, variable‑fidelity framework for generating and optimizing free‑form antenna topologies.  
- Uses quasi‑random shape creation, uniform scaling via regression (Eq. 3), and a trust‑region optimization (Eqs. 6‑8) that requires only a few high‑fidelity EM simulations per iteration.  

**2. Main Conclusions**  
- The surrogate model can shift resonance frequencies with minimal computational cost, enabling candidate designs that satisfy the in‑band response threshold (Fig. 2).  
- Achieves 16–20 % bandwidth in the 5–7 GHz IoT band, dual‑lobe radiation patterns, and good agreement between simulated and measured performance.  
- Average design cost: ~695 high‑fidelity EM simulations (~21 CPU hours) per antenna.  
- **No dosimetry results** (SAR, absorbed power, power‑density, exposure, etc.) are reported in this excerpt.  

**3. Limitations / Future Work**  
- The current work focuses solely on antenna performance (bandwidth, gain, pattern, fabrication tolerance) and does not address non‑ionizing radiation safety metrics.  
- Future work should incorporate dosimetry evaluation (e.g., SAR, absorbed‑power) into the optimization loop to ensure compliance with safety standards.  
- Additional limitations include reliance on low‑fidelity EM models and the need for more robust handling of fabrication tolerances and Monte‑Carlo yield uncertainty.