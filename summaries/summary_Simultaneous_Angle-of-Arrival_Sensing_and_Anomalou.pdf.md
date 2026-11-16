# Summary for Simultaneous_Angle-of-Arrival_Sensing_and_Anomalou.pdf

## Preliminary caveat

The source excerpt is an antenna/array engineering and ISAC paper. It contains **no dosimetry content whatsoever** — no SAR, no absorbed-power or power-density mapping, no exposure-limit comparison, no biological/tissue modeling. Items below labelled *(inferred)* are my own reading of what is absent, not statements made by the authors.

---

### 1. Core Method — what they did

- **Problem:** synthesize anomalous reflection from a *finite* patch-antenna array by optimizing the **reactive load impedances** $Z_L$ on each element, while simultaneously extracting the **angle-of-arrival** from the spatial Fourier transform of the load currents (secondary spectral peak → $\theta_i = 30^\circ$ for $\theta_r = 70^\circ$).
- **Setup:** full-wave **CST** simulations at **28 GHz**, lossless Rogers RO4350B ($\varepsilon_r = 3.66$, $h = 0.338$ mm); two apertures:
  - Design-1: 21 elements, $\lambda/2$ spacing, $10.5\lambda \times 0.5\lambda$
  - Design-2: 82 elements, $\lambda/4$ spacing, $10.25\lambda \times 0.5\lambda$
- **Two objectives compared:** maximize the spatial-harmonic current $|b_{IL}(k\sin\theta_r)|$ vs. maximize the bistatic scattering cross section $\sigma(Z_L,\theta_r)$.
- **Metric:** a power-conservation-based reference efficiency using the $\sqrt{\cos\theta_i}\sqrt{\cos\theta_r}$ field-ratio reference (Eq. 9), with suppression of the specular reflection.
- **Reported outputs:** normalized far-field scattered patterns and RCS in dBsm only — field *amplitudes*, not absorbed power.

### 2. Main Conclusions — dosimetry results

**There are none.** No dosimetric quantity is computed or discussed.

What *is* reported (antenna performance, not dosimetry):
- Current-based objective: **89.73 %** ($\lambda/2$) vs **177 %** ($\lambda/4$).
- Far-field/SCS-based objective: **96.65 %** vs **211 %**.
- Efficiencies >100 % are attributed to **superdirective subwavelength spacing**, so they are not "gain" in a physical power sense and must not be read as exposure amplification factors.
- A residual parasitic lobe near $-40^\circ$ ($k_x/k = -0.64$) persists in the $\lambda/2$ case.

Only transferable dosimetric observation *(inferred, not claimed by the authors)*: the structure **redirects** rather than absorbs incident power density (near-complete anomalous deflection, strongly reduced specular scattering). Any SAR/power-density consequence near the array would have to be recomputed from the current/field solutions — the paper does not do this.

### 3. Limitations / Future Work

**The authors' own stated limitations and future work are not present in the supplied excerpt** (references [14]–[29] only), so none can be quoted. Gaps identifiable from the content *(inferred)*:

- No near-field/absorbed-power quantification; no SAR, power-density, or exposure-limit assessment; no phantom or tissue model.
- **Lossless** substrate and passive-lossless loads assumed — real dielectric/conductor loss and hence actual absorption are unaccounted for.
- Single frequency (28 GHz), single angle pair ($\theta_i=30^\circ$, $\theta_r=70^\circ$); no bandwidth, scan-range, or tolerance analysis.
- Superdirective $\lambda/4$ designs imply high $Q$/narrowband operation and sensitivity to element mismatch and mutual coupling — unquantified here.
- Simulation-only validation; no measurement or fabrication data in the excerpt.
- Unexplained parasitic lobe ($-40^\circ$) and the efficiency definition >100 % both need care before any exposure-related interpretation.

**Bottom line:** this paper cannot support any dosimetric conclusion; it can only supply current/field solutions as *input* to a separate dosimetric study.