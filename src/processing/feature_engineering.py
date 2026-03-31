def add_features(df):
    fastest = df['lap_time_sec'].min()

    df['delta'] = df['lap_time_sec'] - fastest

    return df