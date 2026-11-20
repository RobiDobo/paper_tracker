# Summary for Motion-Coupled_Sensing__When_the_State_Change_Powe.pdf

Based on the provided technical details from the paper, here is the structured summary:

### 1. Core Method: What did they do?
* **Electromechanical Energy Harvesting:** Developed a batteryless, motion-coupled IoT platform powered by human-actuated hinge motion (evaluated across waste bins, room doors, and office cabinets).
* **Hardware Architecture:** Utilized a 24 V DC motor acting as a generator coupled with a 1:42.6 spur-gear train to amplify low hinge speeds (17.85–27.8 RPM). 
* **Power Management:** Integrated a custom rectifier PCB, a $1000\,\mu\text{F}$, 25 V energy storage capacitor (with an empirical wake-up threshold of 11.5 V), and a buck converter providing a regulated 3 V rail.
* **Sensing and Communication:** Implemented bounded wake–sense–transmit transactions using an active ultrasonic sensor (achieving fill-level sensing) and a LoRa uplink operating via LoRaWAN (20 dBm, 125 kHz bandwidth).

### 2. Main Conclusions: What were the key dosimetry results?
*(Note: As highlighted in the source text, the paper does not focus on non-ionizing radiation dosimetry, SAR, or electromagnetic exposure limits, but rather on electromechanical performance and energy-harvesting reliability.)*
* **Energy Budget:** Each complete wake-sense-transmit cycle requires approximately **61 mJ** of energy, heavily dominated by the LoRa transmission ($\approx 57.5\,\text{mJ}$).
* **Transmission Reliability:** Field testing demonstrated high operational reliability, achieving **99.3%** per-event transmission reliability across 5,945 bin actuations, alongside **92%** and **94%** packet delivery rates for door and cabinet deployments, respectively.
* **Sensing Accuracy:** The ultrasonic fill-level sensing achieved a mean absolute error of **19.08 mm** during field deployments.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
*(Note: While the provided text is primarily focused on the successful empirical and technical metrics of the current implementation, standard mechanical energy harvesting and batteryless IoT platforms of this nature typically face limitations regarding mechanical wear over extended lifecycles, dependency on consistent user-actuation velocity, and the strict constraints of intermittent energy buffers. The provided text extracts do not explicitly detail specific future work gaps beyond the presented field performance statistics.)*