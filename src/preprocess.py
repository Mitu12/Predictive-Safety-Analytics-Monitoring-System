import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna("Unknown", inplace=True)
    return df
