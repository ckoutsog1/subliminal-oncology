import pandas as pd
import numpy as np
import neurokit2 as nk
import matplotlib.pyplot as plt

class SubliminalChaosEngine:
    """
    Core Engine for Project Subliminal Oncology.
    Detecting the 'Chaos-to-Rigidity' transition in the Autonomic Nervous System.
    """
    def __init__(self, sampling_rate=1000):
        self.sampling_rate = sampling_rate

    def calculate_vagal_rigidity(self, rr_intervals):
        """
        Calculates Sample Entropy (SampEn) to identify pathological rigidity.
        Healthy = High Entropy (Chaos)
        Oncogenic Drift = Low Entropy (Rigidity)
        """
        # Calculate HRV indices using NeuroKit2
        hrv_indices = nk.hrv_nonlinear(rr_intervals, sampling_rate=self.sampling_rate)
        
        # Extract Sample Entropy (SampEn)
        samp_en = hrv_indices['HRV_SampEn'][0]
        
        # Define the 'Rigidity Threshold' based on paper specs
        # Note: Values below 1.1 in longitudinal decay suggest 'Oncogenic Drift'
        is_rigid = samp_en < 1.1
        
        return samp_en, is_rigid

    def calculate_vagal_slope(self, longitudinal_entropy_data):
        """
        The Vagal Slope (Δξ): The rate of entropy decay over time.
        A persistent negative slope over 10 cycles triggers the 'Subliminal Alert'.
        """
        # Linear regression to find the decay rate (The Slope)
        x = np.arange(len(longitudinal_entropy_data))
        y = np.array(longitudinal_entropy_data)
        slope, intercept = np.polyfit(x, y, 1)
        
        return slope

# Example Usage for Monday Launch:
if __name__ == "__main__":
    # Simulated R-R intervals (In a real scenario, this comes from the Smart Bra ECG)
    # simulated_data = [800, 810, 795, 805, ...] 
    
    print("Subliminal Oncology: Chaos Engine Initialized.")
    print("Status: Awaiting Clinical Data for Vagal Slope Validation.")
