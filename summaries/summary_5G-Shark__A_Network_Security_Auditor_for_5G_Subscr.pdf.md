# Summary for 5G-Shark__A_Network_Security_Auditor_for_5G_Subscr.pdf

Based on the extracted technical details from the paper "5G-Shark: A Network Security Auditor for 5G Subscribers," here is the structured summary:

### 1. **Core Method: What did they do?**
* **Hardware & Software Setup:** Developed "5G-Shark," a Software-Defined Radio (SDR) based network security auditor utilizing a USRP X310 hardware setup to impersonate 5G base stations.
* **Exploitation of Cell Reselection:** Exploited device-driven cell reselection procedures, unauthenticated signaling, and 3GPP TS 38.304 signal thresholds (RSRP/RSRQ) in RRC_IDLE and RRC_INACTIVE states to manipulate subscriber connections.
* **RF Manipulation & Attenuation:** Used physical signal attenuation (e.g., aluminium foil/electromagnetic shielding) combined with SDR transmissions to selectively degrade legitimate commercial network signals while maintaining line-of-sight to the rogue base station.
* **Attack Execution:** Adjusted transmission priorities, Tracking Area Codes (TACs), and radio conditions to force mobile devices into connecting to the rogue base station, thereby executing IMSI-catching, identity harvesting (exposing permanent identifiers like IMSI/SUCI in cleartext), and service downgrade attacks in both Non-Standalone (NSA) and Standalone (SA) 5G environments.

### 2. **Main Conclusions: What were the key dosimetry results?**
* **Not Applicable (Dosimetry):** The paper focuses exclusively on telecommunications protocols, cybersecurity, and subscriber privacy vulnerabilities. It contains **no technical methods, numerical data, measurements, or results regarding non-ionizing radiation dosimetry, radiofrequency (RF) power absorption, or Specific Absorption Rate (SAR).**

### 3. **Limitations / Future Work: What are the gaps mentioned by the authors?**
*(Note: While the provided text excerpts focus heavily on the operational methodology and protocol vulnerabilities rather than an explicit "future work" section, the context highlights inherent security gaps in current deployments)*
* **Vulnerable Device-SIM Combinations:** Experiments demonstrated that current implementations of device-SIM combinations fail to adequately protect permanent identifiers, bypassing privacy mechanisms and exposing temporary/permanent identifiers (GUTI/IMSI/SUCI) due to insecure registration reject handling and lack of mutual authentication during early connection stages.
* **Protocol-Design Flaws:** The reliance on unauthenticated signaling and standard-compliant cell reselection criteria (such as trust in broadcasted TACs and signal prioritization) leaves 5G architectures vulnerable to false base station (F-BS) exploitation.