# Summary for Device-Referred_Channel_Sounding_With_Commodity_Wi.pdf

**1. Core Method**  
- Captured per‑subcarrier channel state information (CSI) from IEEE 802.11 beacon frames using off‑the‑shelf Wi‑Fi receivers.  
- Applied five correction steps to the raw CSI:  
  1. Sub‑carrier mapping,  
  2. Receive‑chain ordering,  
  3. Per‑packet timing/phase alignment,  
  4. RSSI‑based gain referencing,  
  5. Window‑response removal.  
- Produced device‑referred channel estimates that can be used for propagation‑parameter extraction and exposure‑relevant statistics.

**2. Main Conclusions (Dosimetry‑relevant Findings)**  
- **Delay spread:** τrms values ranged from **24 ns to 96 ns** across 5 GHz and 6 GHz bands.  
- **RSSI:** Measured signal levels spanned **‑70 dBm to ‑25 dBm**.  
- **Rician K‑factor:** Varied from **‑10 dB up to > 16 dB**, indicating both low‑ and high‑clustering environments.  
- **Temporal correlation:** Correlation coefficient |ρ(102.4 ms)| dropped from **≈0.85 (standing)** to **≈0.15 (walking)**, demonstrating that mobility markedly decorrelates the channel over a beacon interval.  
- With all five corrections applied, the **median τrms bias** was **–6 % to +14 %**, confirming that the method yields accurate channel sounding suitable for **dosimetric exposure assessment** (e.g., estimating absorbed power or specific absorption rate from the measured CSI/RSSI).

**3. Limitations / Future Work (Gaps Identified by the Authors)**  
- The paper **does not provide explicit non‑ionizing‑radiation dosimetry metrics** (SAR, power density, absorbed dose, exposure limits); only propagation/sensing parameters are reported.  
- **Mapping CSI/RSSI to SAR/power‑density** remains an open challenge; dedicated hardware or calibrated models are needed.  
- Limited **mobility and site diversity**: only six indoor sites and two motion states (standing/walking) were examined.  
- **Bandwidth and antenna configuration effects** (e.g., different channel widths, MIMO setups) have not been systematically investigated.  
- No **validation against a calibrated dosimetry instrument** (e.g., a SAR measurement system) was presented; future work should compare the derived exposure estimates with ground‑truth measurements.  
- The approach assumes **beacon‑only measurements**; incorporating data frames or continuous traffic could improve accuracy under varying traffic loads.