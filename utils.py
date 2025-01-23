import pandas as pd
import numpy as np

# Create synthetic data
np.random.seed(42)
data = {
    "Machine_ID": np.arange(1, 101),
    "Temperature": np.random.uniform(60, 100, 100),
    "Run_Time": np.random.uniform(50, 300, 100),
    "Downtime_Flag": np.random.choice([0, 1], size=100, p=[0.7, 0.3])  # 0 = No, 1 = Yes
}

df = pd.DataFrame(data)
df.to_csv("sample_dataset.csv", index=False)
