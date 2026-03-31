def compute_undercut(df):
    results = []

    drivers = df['Driver'].unique()

    for driver in drivers:
        driver_df = df[df['Driver'] == driver].copy()

        # detect pit laps (stint change)
        driver_df['pit'] = driver_df['Stint'].diff() != 0
        pit_laps = driver_df[driver_df['pit'] == True]

        for _, pit in pit_laps.iterrows():
            lap = pit['LapNumber']

            before = driver_df[driver_df['LapNumber'].between(lap-3, lap-1)]
            after = driver_df[driver_df['LapNumber'].between(lap+1, lap+3)]

            if len(before) > 0 and len(after) > 0:
                before_avg = before['lap_time_sec'].mean()
                after_avg = after['lap_time_sec'].mean()

                gain = before_avg - after_avg

                results.append({
                    'Driver': driver,
                    'PitLap': lap,
                    'BeforePitAvg': before_avg,
                    'AfterPitAvg': after_avg,
                    'UndercutGain': gain
                })

    return results