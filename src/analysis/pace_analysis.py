def race_pace(df):
    return df.groupby('Driver')['lap_time_sec'].mean().sort_values()

def driver_consistency(df):
    return df.groupby('Driver')['lap_time_sec'].std().sort_values()