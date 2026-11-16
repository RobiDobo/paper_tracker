# Summary for Do_Electromagnetic_Side-Channel_Attacks_Threaten_E.pdf

Based on the provided extracted technical details, here is the structured summary:

### 1. Core Method
The researchers evaluated the feasibility of electromagnetic side-channel (TEMPEST) attacks on video interfaces (VGA/HDMI) of electronic voting equipment. 
* **Setup:** They used an Ettus USRP B200 Software-Defined Radio (SDR) paired with a digital TV antenna tuned to harmonic frequencies of the display's pixel clock rate ($f_p$).
* **Scenarios:** Two operational distances were tested—Scenario 1 placed the SDR roughly 1 meter away behind a masonry wall, and Scenario 2 simulated close proximity (under 0.5 meters) using display resolutions of $1280 \times 768@60$ ($f_p = 74.25\text{ MHz}$) and $1920 \times 1080@60$ ($f_p = 148.5\text{ MHz}$).
* **Processing:** Raw radio samples from the 3rd, 6th, and 7th harmonics (sampled at $54\text{ MHz}$) were processed and resynchronized using the GNU Radio `gr-tempest` module to attempt visual reconstruction of candidate numbers displayed on the target monitor.

### 2. Main Conclusions
* **Dosimetry / Measurement Results:** The provided text explicitly notes that *no specific non-ionizing radiation dosimetry metrics* (such as Specific Absorption Rate or absolute field strength measurements) were evaluated. 
* **Attack Efficacy:** The primary finding is that visual reconstruction of sensitive display data (candidate numbers) is experimentally feasible via electromagnetic leakage. Efficacy is strongly tied to physical proximity, succeeding both at distances under 0.5 meters and through a masonry wall at a distance of approximately 1 meter.

### 3. Limitations / Future Work
*(Note: Based strictly on the provided text, the authors identified that attack efficacy is strongly tied to physical proximity, but specific gaps, limitations, or future work proposals regarding the setup were not detailed in the excerpt.)*