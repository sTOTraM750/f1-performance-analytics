def stint_performance(df):
    return df.groupby(['Driver', 'Stint', 'Compound'])['lap_time_sec'].mean().reset_index()


def tire_degradation(df):
    # trend over laps inside stint
    return df.groupby(['Driver', 'LapNumber'])['lap_time_sec'].mean().reset_index()


def pit_stop_impact(df):
    df['pit'] = df['Stint'].diff() != 0

    pit_laps = df[df['pit'] == True]

    return pit_laps[['Driver', 'LapNumber', 'lap_time_sec']]