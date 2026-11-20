# Summary for Battery-Free_Sensor_Array_for_Wireless_Multi-Depth.pdf

# Structured Summary

## 1. Core Method
- Developed **analytical models of mutual inductance** and coil **quality factor (Qp)** to calculate the **induced voltage delivered to the sensor**.
- Compared this induced voltage against a **power-up threshold voltage (vth)**.
- Proposed an **analytical optimization framework** for NFC-based magnetic induction, tuning:
  - **Qp** (coil quality factor)
  - **Pt** (transmission power)
  - **Sensor coil radius**
- Validated using an **8-sensor array** in an underground sensing setup.

## 2. Main Conclusions
- Raising the sensor coil’s **Qp from 8 to 32** extended the maximum communication range (used here as a **proxy for received field/power dose**) from **~6 cm to ~11 cm**, with **minimal soil impact**.
- The **downlink range** appears primarily limited by the need to reach the **power-up threshold voltage (vth)**; transmission power and coil parameters largely govern field strength and power transfer efficiency.
- **Optimal parameters** identified: **Qp = 32**, **Pt = 1 W**, **coil radius = 0.05 m**.
- The **8-sensor array** successfully powered all receivers and achieved sufficient uplink voltage at **1.2 m depth**, whereas a **single sensor** only received adequate voltage within the **first three locations**.
- The results indicated **enhanced electromagnetic field penetration** through the array, supporting its use for **wireless dosimetry assessment**.

## 3. Limitations / Future Work
- The provided excerpt does **not explicitly mention** limitations or future work.
- The study uses **communication range as a proxy for received field/power dose** — this may not fully capture actual dosimetric exposure levels.
- Soil influence was noted as having **minimal impact**, but broader environmental or material factors were not deeply explored.
- The single-sensor comparison was limited to the first three locations; longer-depth or more complex field geometries remain untested in this excerpt.