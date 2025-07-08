import pandas as pd
import numpy as np

def remove_outliers(df, z_thresh=3):
    from scipy.stats import zscore

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_clean = df.copy()

    if not numeric_cols.empty:
        z_scores = np.abs(zscore(df_clean[numeric_cols], nan_policy='omit'))
        mask = (z_scores < z_thresh).all(axis=1)
        df_clean = df_clean[mask]
    
    return df_clean
