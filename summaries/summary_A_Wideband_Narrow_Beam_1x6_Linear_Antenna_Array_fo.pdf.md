# Summary for A_Wideband_Narrow_Beam_1x6_Linear_Antenna_Array_fo.pdf

## Important caveat up front

The excerpt you provided contains **no dosimetry content whatsoever**. It is an antenna design/RF characterization paper (28 GHz, 1×6 patch array). Any "dosimetry results" or "author-stated gaps" would have to be invented, so I have not done that. Below is the structured summary with what is actually supported, clearly separated from what is absent.

---

### 1. Core Method — what they actually did
- **Device:** compact 1×6 linear microstrip patch array, **series-fed** through 0.1 mm transmission lines.
- **Substrate:** Rogers RO3003, εr = 3.0, thickness 1.574 mm; element spacing 1.9 mm (≈0.18 λ₀ at 28 GHz — a very compact, strongly coupled layout).
- **Analysis tool:** time-domain EM solver (full-wave), **open (free-space) boundary conditions**, i.e., no phantom, no tissue, no human model in the simulation domain.
- **Reported metrics:** S-parameters/return loss (quoted as "<10 dB" — sign convention ambiguous, presumably S11 < −10 dB), VSWR, impedance bandwidth, gain/directivity, radiation patterns, surface current distribution.

### 2. Main Conclusions — dosimetry results
- **None. There are no dosimetry results.** No SAR, no absorbed power, no incident power density, no duty-cycle/averaging analysis, no biological-tissue modeling, and no comparison against ICNIRP/FCC/IEEE exposure limits.
- The only conclusions present are antenna-level: wideband operation with high directivity and narrow beamwidth around 28 GHz.
- "Wearable/biomedical" appears only as an application motivation (and in reference titles), not as a quantified exposure assessment.

### 3. Limitations / Future Work
- **Author-stated limitations:** none appear in this excerpt, so I cannot attribute any to them.
- **Gaps identifiable from the excerpt (my assessment, not the authors'):**
  - No SAR/absorbed-power computation → device safety cannot be evaluated from this paper.
  - Free-space open boundaries only; no tissue-equivalent phantom or realistic body proximity model (a wearable/near-body claim without this is unsupported).
  - No exposure-limit compliance check (ICNIRP 2020/FCC OET-65, IEEE C95.1), no power-density or whole-body/localized averaging.
  - No measurement validation reported in this section (simulation-only S-parameters/patterns); mutual-coupling effects of the 1.9 mm spacing not discussed in the excerpt.
  - Needed for dosimetry: FDTD/FEKO-style SAR simulation with voxel or SAM phantom, input-power normalization, 1 g/10 g averaging, and incident power-density estimation.

---

**To give you a genuine dosimetry summary,** please paste the actual Part 3 text (or the SAR/exposure section). If the paper simply has no such section, then the correct answer to questions 2 and 3 is "not addressed," and any dosimetry claim about this work would be unsupported by the source.