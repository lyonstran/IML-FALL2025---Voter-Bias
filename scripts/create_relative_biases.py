
import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cfb\cfb_master_bias_file.csv')
bias_cols = ['bias1(v, t)', 'bias2(v, t)', 'bias3(v, t)']
percentiles = range(1, 100)

ret = {
    'Percentile' : percentiles,
    "bias1(p)": [np.percentile(df['bias1(v, t)'].dropna(), p) for p in percentiles],
    "bias2(p)": [np.percentile(df['bias2(v, t)'].dropna(), p) for p in percentiles],
    "bias3(p)": [np.percentile(df['bias3(v, t)'].dropna(), p) for p in percentiles],
}
cfb_relative_biases = pd.DataFrame(ret)
cfb_relative_biases.to_csv('cfb_relative_biases.csv')