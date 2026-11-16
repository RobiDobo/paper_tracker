# Summary for Active_Sensing_with_Meta-Reinforcement_Learning_fo.pdf

1. **Core Method**  
   - Extracted statistical features (mean, standard deviation, RMS, inter‑antenna phase differences) from raw IQ samples.  
   - Encoded these features with a 1‑D CNN to produce a compact observation vector.  
   - Used the vector as input to reinforcement‑learning policies (feed‑forward PPO, recurrent PPO, DQN) with optional LSTM memory to capture spatio‑temporal RF patterns.  
   - Designed a reward function that combines distance‑progress, a step‑penalty, and a terminal success reward to drive source‑seeking behavior under partial observability.

2. **Main Conclusions**  
   - The recurrent PPO agent achieved the highest performance, reaching ~80 % success rate and superior explained variance compared with feed‑forward PPO and DQN baselines.  
   - This demonstrates that meta‑reinforcement learning can enable robust active sensing and interference‑source localization in synthetic indoor propagation environments.  
   - **No dosimetry results** (dose, power‑density, exposure, SAR, etc.) are presented; the paper is purely focused on RL‑based navigation, not on non‑ionizing radiation safety assessment.

3. **Limitations / Future Work**  
   - Evaluation is limited to a synthetic indoor dataset; real‑world validation on diverse environments is missing.  
   - No assessment of safety, exposure, or dosimetric constraints (e.g., SAR, power‑density limits) is included.  
   - The reward design and propagation model are simplified; future work should incorporate more realistic channel models, broader antenna configurations, and possibly safety‑aware reward terms.  
   - Generalization across different scenarios (e.g., outdoor, varying clutter, multiple interferers) remains to be tested, as does the integration of domain‑randomization or meta‑learning to improve robustness.