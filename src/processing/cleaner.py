import pandas as pd

def clean_laps(df):
    df = df.dropna(subset=['LapTime']).copy()

    df['LapTime'] = pd.to_timedelta(df['LapTime'])
    df['lap_time_sec'] = df['LapTime'].dt.total_seconds()

    # 🚨 REMOVE OUTLIERS (VERY IMPORTANT)
    df = df[df['lap_time_sec'] < df['lap_time_sec'].quantile(0.95)]

    return df[['Driver', 'LapNumber', 'lap_time_sec', 'Compound', 'Stint']]