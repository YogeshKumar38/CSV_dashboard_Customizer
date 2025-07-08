import pandas as pd
from utils import remove_outliers

def clean_data(df):
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')  # Drop completely empty rows
    df = df.dropna(axis=1, how='all')  # Drop completely empty columns
    df = df.drop_duplicates()
    df = remove_outliers(df)
    return df
