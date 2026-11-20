# Summary for Demo_Abstract__Pible__Battery-Free_Mote_for_Perpet.pdf

**1. Core Method**
The authors designed and implemented **Pible**, a battery-free Bluetooth Low Energy (BLE) sensor node that achieves perpetual operation through intelligent energy harvesting and adaptive power management. The core technical contributions are:
*   **Hardware Architecture:** A COTS-based platform utilizing a Panasonic 1F/5.5V supercapacitor for energy storage and an AM1454 solar harvester (characterized at 46.5 µA @ 1.5 V under 300 lux indoor lighting).
*   **Voltage-Based QoS Lookup Table (Table 1):** A static mapping mechanism that translates the supercapacitor’s instantaneous storage voltage directly into discrete sensing and advertising duty cycles (rates).
*   **Predictive Power Management Algorithm (Algorithm 1):** A real-time firmware algorithm that dynamically adapts the sensing frequency by analyzing trends in harvested light intensity and voltage trajectories, rather than reacting solely to instantaneous voltage. This maximizes both node lifetime and application-level Quality of Service (QoS).

**2. Main Conclusions**
*   **No Dosimetry Results:** The provided text explicitly states the paper describes an **energy-harvesting architecture and BLE sensor node, not dosimetry**. There are no radiation, light-dose, or chemical exposure measurement results presented.
*   **Actual Key Results (Energy Harvesting/QoS):** The system demonstrates successful **perpetual operation in varying indoor lighting conditions** using commercial off-the-shelf components. The predictive algorithm effectively manages the trade-offs between sensing frequency, advertising rate, and energy availability, outperforming static voltage-threshold approaches by anticipating energy income to sustain higher application QoS.

**3. Limitations / Future Work**
*   **Not Mentioned in Source Text:** The provided extract does not contain a "Limitations" or "Future Work" section. It focuses solely on the architecture description (lookup table, algorithm) and the high-level result (perpetual operation trade-offs demonstrated with specific hardware specs).