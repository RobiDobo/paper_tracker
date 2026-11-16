# Summary for Antennas_in_Walls__Performance_Analysis_of_Microst.pdf

### 1. Core Method

The authors performed a MATLAB-based antenna and propagation-channel analysis for a **150 GHz foam-substrate microstrip patch antenna** embedded in a **5 mm paint layer on drywall**. The antenna had an approximately **1 mm² patch (446 × 412 µm)**; the paint was characterized by **εp = 4.5369** and **np = 2.13**.

They calculated received power for five multipath channels:

- Direct wave (DW)
- Reflected waves at air–paint and paint–drywall interfaces (RW-A, RW-D)
- Lateral waves at those interfaces (LW-A, LW-D)

The link model combined free-space spreading with exponential molecular absorption using frequency-dependent absorption coefficients for drywall, paint, and air; the air coefficient was based on HITRAN data for ten atmospheric gases. The calculations integrated the antenna radiation patterns over the transmit and receive boresight angles, **βT** and **βR**. The antenna simulation produced a **7.07 GHz −10 dB bandwidth (146.03–153.1 GHz)** and **6.03 dBi peak gain at 95°**.

### 2. Main Conclusions

**No dosimetry results were reported.** The study contains no SAR, internal electric-field, tissue-absorption, power-density, or exposure-compliance assessment.

Its propagation/link-budget conclusions were:

- Total received power peaked at **−41.05 dBm** at **0.6 mm burial depth**, with **βT = 67°** and **βR = 123°**.
- At **4.4 mm burial depth**, total received power decreased to **−64.96 dBm**.
- The air–paint lateral-wave component (**LW-A**) was generally dominant, averaging approximately **−76 dB**.
- The direct wave remained essentially constant at **−97.53 dBm**.
- The other multipath components generally fell between approximately **−70 and −118 dBm**.

These values characterize link reception, not energy absorbed by human tissue. They could serve only as indirect inputs to a subsequent exposure assessment; they cannot themselves establish SAR, absorbed dose, or regulatory compliance.

### 3. Limitations / Future Work

The supplied extract does **not** list explicit limitations or future-work recommendations from the authors. The stated scope limitation is that the paper is a channel/link-budget study rather than a dosimetry study: it does not model tissue absorption, E-field distribution, SAR, or safety limits.

An actual exposure assessment would require additional information such as a human-tissue or body model, incident-field distribution, operating duty cycle, averaging interval, and compliance-appropriate SAR or power-density calculations. Those are inferred requirements for dosimetry, **not author-stated future work in the supplied extract**.