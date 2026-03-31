def tire_degradation_curve(df):
    return df.groupby(['Driver', 'LapNumber'])['lap_time_sec'].mean().reset_index()