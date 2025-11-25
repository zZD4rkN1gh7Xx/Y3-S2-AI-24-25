from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd

def encode_target(df, target_col='Target'):
    le = LabelEncoder()
    df[target_col] = le.fit_transform(df[target_col])
    return df

def encode_categoricals(df, exclude_cols=['Target']):
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        if col not in exclude_cols:
            df[col] = le.fit_transform(df[col])
    return df

def normalize_data(df, target_col='Target'):
    scaler = MinMaxScaler()
    features = df.drop(columns=[target_col])
    features_scaled = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)
    features_scaled[target_col] = df[target_col].values  # reanexar target sem normalizar
    return features_scaled