# Summary for Physics-Augmented_Graph_Transformers_for_Patch-Ant.pdf

## Note on scope

The paper is an **antenna radiation-pattern surrogate/inverse-design study**, not a dosimetry study. It contains no SAR, absorbed-dose, power-density, or exposure-compliance results. Item 2 below therefore reports what the paper *did* conclude, plus the only dosimetry-relevant (indirect) connection.

## 1. Core Method

- **Architecture**: mesh-native Graph GPS (graph transformer) operating directly on the antenna mesh.
- **Physics-Augmented Intermediate Supervision (PAIS)**: auxiliary node-level supervision on complex surface currents **J(r)**, so intermediate representations are tied to physical fields, not just the final pattern.
- **Direction-conditioned decoder** + **differentiable radiation-integral consistency loss** linking predicted currents to far-field patterns.
- **Data**: 80,000 CST full-wave simulations at 5.6 GHz; patch antennas derived from FMNIST/CIFAR masks; 34×34 (θ, φ) far-field patterns plus surface-current ground truth. Evaluated on random, PCA, and zero-shot canonical-geometry splits.
- **Inverse design**: conditional diffusion generating candidates, filtered by the learned surrogate, with top K=5 re-validated in CST (N=500 candidates), compared against nearest-neighbor retrieval and classical discrete optimizers.

## 2. Main Conclusions (dosimetry results: none)

- **No dosimetry quantities were computed or reported** — no SAR, no tissue exposure, no dose metrics. Any dosimetry relevance is indirect: the predicted J(r) and far-field patterns *could* feed near-field/SAR estimation, but that step was not performed.
- Forward surrogate: GPS+PAIS reached **MSE 0.17 / PSNR 19.67 dB** on the main split, and generalized to PCA and zero-shot canonical patches.
- Inverse design on the 100 hardest PCA targets: **MSE 0.77 vs 1.13** (nearest-neighbor), i.e. **32% relative MSE gain**; PSNR **11.12 vs 9.02 dB**; HPBW-IoU **0.77 vs 0.53**. Classical discrete optimizers collapsed (**MSE 2.76–3.30**).

## 3. Limitations / Future Work

Stated by the authors:
- **Single frequency** (5.6 GHz) only — no broadband/multi-frequency validation.
- **Binary geometries** only (no continuous material/geometry parameters).
- Extension to **tissue-exposure / SAR dosimetry is explicitly left to future work**.

Reasonable inferences (not stated verbatim): hard-split degradation (MSE 0.17 → 0.77) shows a residual generalization gap; CST validation is limited to the top K=5 diffusion candidates; no near-field/tissue phantom validation at all.