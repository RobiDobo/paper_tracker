# Summary for Design_Multiband_Monopole_and_Microstrip_Patch_Ant.pdf

**1. Core Method**  
The authors designed, simulated (via Ansoft HFSS), fabricated, and experimentally validated a dual-band monopole antenna integrated with a microstrip patch for GSM (890–960 MHz) and DCS (1710–1880 MHz) operation. The antenna employs a wrapped low-profile monopole geometry specifically intended to direct radiation away from the user’s head. Performance was characterized using simulated and measured return loss (S₁₁), VSWR (unmatched ≤2, matched 1.5 at 980 MHz), and far-field radiation patterns, with network-analyzer measurements confirming simulation results.

**2. Main Conclusions (Dosimetry Context)**  
**No quantitative dosimetry results are presented.** The paper does not report Specific Absorption Rate (SAR) values, tissue-specific absorption data, or power density measurements. SAR is referenced only qualitatively as a design motivation: the wrapped low-profile monopole structure is intended to reduce radiation toward the user’s head compared to conventional monopoles. The key demonstrated results are purely RF performance metrics (return loss: 13.9 dB at 980 MHz / 20.3 dB at 1.71 GHz; VSWR; radiation patterns).

**3. Limitations / Future Work**  
*   **Absence of Dosimetric Validation:** The primary gap is the lack of any SAR simulation or measurement (e.g., using SAM phantoms or anatomical models) to verify the qualitative claim of reduced head exposure.  
*   **No Human-Body Interaction Analysis:** Antenna performance (impedance, efficiency, pattern) was characterized in free space; the detuning effect and near-field interaction with a head/hand phantom were not assessed.  
*   **Bandwidth/Matching Constraints:** The unmatched VSWR ≤2 suggests potential matching network losses or bandwidth limitations not fully explored in the context of body-worn use cases.