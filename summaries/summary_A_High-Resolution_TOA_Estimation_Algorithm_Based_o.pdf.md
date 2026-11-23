# Summary for A_High-Resolution_TOA_Estimation_Algorithm_Based_o.pdf

**Final Structured Summary**

1. **Core Method**  
   - The paper describes a high-resolution time-of-arrival (ToA) estimation approach using coherent multi-band least-squares formulation, point-spread function (PSF) modeling, and Cramér-Rao bound (CRB) analysis.  
   - It proposes a two-stage particle swarm optimization (TSPSO) delay estimator: a coarse reference-subband grid search followed by continuous-domain PSO optimization.  
   - It also evaluates PSO-assisted sparse-recovery frameworks (PSO-OMP, PSO-RELAX) on 1,600 channel frequency response (CFR) snapshots from 50 measurement records.  
   - The study examines tradeoffs between effective bandwidth (B_eff) and peak-to-sidelobe ratio (PSLR), including effects of subband bandwidth and frequency gaps.

2. **Main Conclusions**  
   - The method achieved near-CRB accuracy in single-path scenarios and validated multipath delay estimation.  
   - Key technical findings include: grid-quantization error ≤ 1/(2Mb∆f), PSLR improvements up to 5.4 dB with Maximum-PSLR layouts, and an inverse relationship between B_eff and PSLR.  
   - **However, there were no key dosimetry results.** The paper does not report any radiation dose, exposure, field strength, specific absorption rate (SAR), or dosimetric validation. The human-reflection delay estimation mentioned was related to time localization in nanoseconds, not radiation dose quantification.

3. **Limitations / Future Work**  
   - The provided section contains no dosimetry-related methods, data, or results.  
   - The authors did not mention specific dosimetry limitations or future work in the excerpt; the main gap is the absence of any dosimetric content or validation.  
   - Future work would likely need to connect the high-resolution ToA/delay estimation methods to actual non-ionizing radiation dosimetry, exposure assessment, or SAR metrics.