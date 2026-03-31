import fastf1
import os


cache_dir = os.path.join(os.getcwd(), "data", "raw", "cache")
os.makedirs(cache_dir, exist_ok=True)

fastf1.Cache.enable_cache(cache_dir)

def fetch_and_store(year: int, race: str):
    session = fastf1.get_session(year, race, 'R')
    session.load()

    laps = session.laps

    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{year}_{race}_laps.csv"

    laps.to_csv(file_path, index=False)

    print(f"Data saved to {file_path}")

    return file_path