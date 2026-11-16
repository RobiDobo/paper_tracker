# Summary for Bespoke_Co-processor_for_Energy-Efficient_Health_M.pdf

**Important caveat:** The provided excerpts contain **no non-ionizing radiation dosimetry content** (no SAR, power density, field strength, frequency bands, or dose quantities). The paper is a hardware/ML design paper. Here is the summary mapped to your requested structure, with the dosimetry fields explicitly marked empty:

**1. Core Method**
- Bespoke fixed-coefficient MAC co-processor integrated with a RISC-V (SERV) core on flexible IGZO TFT technology (Pragmatic).
- MLP weights realized as constant selections; mapping/scheduling formulated as a constrained-programming (CP-SAT) decomposition problem (Algorithm 1) minimizing inference latency under a multiplier budget and per-cycle capacity.
- 4-bit operands; Monte Carlo constant sampling; evaluated on ten healthcare MLP datasets (WESAD, DriveDB, StressInNurses, SPD, Arrhythmia, ECG5000, Dermatology, HAR, AffectiveRoad) with 4–5-bit quantized weights/activations.

**2. Main Conclusions (dosimetry results)**
- **None.** No dosimetry or EM-exposure results are reported; nothing to extract on the radiation side.
- Reported (non-dosimetric) results: ≤0.75% accuracy loss vs. FP32; inference <1 s (avg. 0.73 s); ~2.42 mm², ~1.5 mW, ~0.48 mJ/inference; ~2.35× speedup / ~2.15× energy reduction vs. SOTA; 1972× faster and ~53.5% lower energy than prior Flex-RV.

**3. Limitations / Future Work**
- None stated in the provided excerpts. The only gap identifiable from the extraction notes is that EM-exposure/SAR characterization of such wearable transmitters is **out of scope entirely** — it would require a different section or reference.

If you intended a dosimetry-focused paper or a specific dosimetry section, please share that text and I'll re-extract.