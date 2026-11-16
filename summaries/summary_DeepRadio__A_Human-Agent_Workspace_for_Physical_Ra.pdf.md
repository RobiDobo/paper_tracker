# Summary for DeepRadio__A_Human-Agent_Workspace_for_Physical_Ra.pdf

**Scope note:** All six extracted parts state the same thing — this paper contains *no* non-ionizing-radiation dosimetry. It is a systems/HCI paper. So the dosimetry-specific answers are "none," and I summarize what the paper actually reports so the record stays accurate.

**1. Core Method (what they did)**
- Built DeepRadio, a human–agent workspace embedded in GNU Radio Companion for SDR development.
- Ran a formative study identifying three interaction breakdowns: silent assumption propagation; execution misinterpreted as communication success; hidden physical actions.
- Designed: radio-specification management; dynamic workflow orchestration (stage graphs, completion contracts); a claim–evidence verification framework; rule-based mixed-initiative control (Deny/Confirm/Propose/Allow); bounded RF operation with pre-transmission checks (transmission disabled by default).
- Evaluated: 7 tasks × 10 runs on PlutoSDR with GPT-5.6-Sol → 95.7% task success, 8.39 ± 4.06 min mean completion; user study (n=20) with a BLE task verified over the air via smartphone (LightBlue): 19/20 vs 10/20, McNemar p = .004; median 14.6 vs 34.2 min.

**2. Main Conclusions (dosimetry results)**
- **None.** No E-field, power density, SAR, frequency, exposure geometry, or dose metrics appear anywhere in the excerpts.
- The only RF-related "results" are procedural safety outcomes: 100% constraint adherence; in all 10 hardware-configuration runs the workflow stopped at the transmission checkpoint with no `start_flowgraph` event.

**3. Limitations / Future Work**
- The provided excerpts contain no author-stated limitations, because dosimetry is entirely out of scope for this paper.
- The dosimetry-relevant gap is therefore total: no exposure assessment, measurement method, or compliance analysis is reported. The excerpts note that if such content exists, it would be in sections not provided — but every section supplied explicitly states there is none.
- I can't invent gaps the authors didn't state; if you need dosimetry extraction, a different paper (or the missing middle sections) would be required.