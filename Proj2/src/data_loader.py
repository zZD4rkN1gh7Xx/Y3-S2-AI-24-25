import pandas as pd

def load_data(path):
    df = pd.read_csv(path, sep=';') 
    df.columns = df.columns.str.strip()
    return df
