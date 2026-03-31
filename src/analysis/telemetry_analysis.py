import fastf1


def get_driver_telemetry(year=2023, race='Bahrain', driver='VER'):
    session = fastf1.get_session(year, race, 'R')
    session.load()

    lap = session.laps.pick_driver(driver).pick_fastest()

    telemetry = lap.get_car_data().add_distance()
    pos = lap.get_pos_data()

    telemetry = telemetry.merge(pos, on='Time')

    return telemetry