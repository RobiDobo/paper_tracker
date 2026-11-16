# Summary for Beyond_the_Grid__Continuous_Dictionary_Pursuit_for.pdf

**Important caveat first:** None of the four excerpts contain any non-ionizing radiation dosimetry content — no SAR, power density, field strength, exposure limits, or dose metrics. I can't report "key dosimetry results" because there are none, and I won't invent them. Below is what the excerpts actually support.

**1. Core Method**
Continuous Dictionary Pursuit (CDP): decomposes 1-D time series into sparse sums of parametric atoms (sinusoids, trends, exponentials, Gaussians, step/square/sawtooth, modulated), formulated as an ℓ₀-regularized nonlinear least-squares problem with atom budget *K* as the sparsity control. Atom parameters are optimized continuously (L-BFGS, FFT-based spectral priors, sharpness annealing for discontinuous waveforms) to eliminate grid-mismatch error. Evaluated on synthetic recovery plus LTSF benchmarks against MSTL, SSA, OMP, NOMP, SFW, MCA, Analysis K-SVD, Prophet, N-BEATS.

**2. Main Conclusions (dosimetry)**
None — no dosimetric quantities or exposure measurements appear. The paper's actual conclusions: ~1% generative-parameter recovery on stationary synthetic signals; best sparsity–accuracy trade-off among nine baselines (median test error 0.65 vs. 0.97 NOMP / 0.87 SFW at K=2); wins in the sparse regime; beats the grid-frozen ablation (MCA); lowest inference cost (10⁻³–10⁻² s/query).

**3. Limitations / Future Work**
None explicitly stated in the excerpts. What the excerpts themselves show: NOMP/SFW overtake CDP at large *K* on pure-sinusoid dictionaries; all validation is on synthetic/benchmark series, not EM-field or exposure data. Dosimetric relevance would arise only if CDP were applied to measured exposure/field time series — which was not done.

Also flag: the excerpts are internally inconsistent (e.g., "AtomS4D neural architecture + SHAP" in Part 3 vs. "reduces to closed-form equations" in Part 4), suggesting possible document mix-up. If you expected an RF/EMF dosimetry paper, please resend the correct file.