from src.ingestion.fastf1_client import fetch_and_store
from src.utils.helpers import load_csv
from src.processing.cleaner import clean_laps
from src.processing.feature_engineering import add_features
from src.analysis.pace_analysis import race_pace, driver_consistency
from src.analysis.strategy_analysis import (
    stint_performance,
    tire_degradation,
    pit_stop_impact
)
from src.analysis.undercut_analysis import compute_undercut
from src.models.lap_time_model import train_model





def run(year=2023, race='Bahrain'):

    # Step 1: Fetch
    path = fetch_and_store(year, race)

    # Step 2: Load
    df = load_csv(path)

    # Step 3: Clean
    df = clean_laps(df)

    # Step 4: Features
    df = add_features(df)

    # Step 5: Analysis
    pace = race_pace(df)
    consistency = driver_consistency(df)

    stint = stint_performance(df)
    degradation = tire_degradation(df)
    pit = pit_stop_impact(df)

    undercut = compute_undercut(df)

    model, error = train_model(df)

    return df, pace, consistency, stint, degradation, pit, undercut, model, error 