import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from pipelines.run_pipeline import run
from dashboard.pages.race_overview import render
import pandas as pd
from src.analysis.telemetry_analysis import get_driver_telemetry

st.title("F1 Performance Analytics System")

year = st.selectbox("Year", [2022, 2023])
race = st.text_input("Race", "Bahrain")

df, pace, consistency, stint, degradation, pit, undercut, model, error = run(year, race)

st.subheader("Race Pace Ranking")
st.bar_chart(pace)

st.subheader("Driver Consistency")
st.bar_chart(consistency)

st.subheader("Lap Time Trend")
pivot = df.pivot(index='LapNumber', columns='Driver', values='lap_time_sec')
st.line_chart(pivot)

st.dataframe(pace.reset_index())
st.write("DEBUG DATA CHECK")
st.write(df.head())

st.subheader("Stint Performance")
st.dataframe(stint)

st.subheader("Tire Degradation")

pivot_deg = degradation.pivot(index='LapNumber', columns='Driver', values='lap_time_sec')
st.line_chart(pivot_deg)

st.subheader("Pit Stop Laps")

st.dataframe(pit)

st.subheader("Undercut Analysis")

undercut_df = pd.DataFrame(undercut)

st.dataframe(undercut_df)

st.subheader("Lap Time Prediction Model")

st.write(f"Mean Absolute Error: {round(error, 3)} seconds")

st.subheader("Predict Lap Time")

lap = st.slider("Lap Number", 1, 60, 10)
stint_val = st.slider("Stint", 1, 5, 1)
compound = st.selectbox("Compound", ["SOFT", "MEDIUM", "HARD"])
driver = st.selectbox("Driver", df['Driver'].unique())



compound_map = {c: i for i, c in enumerate(df['Compound'].unique())}
driver_map = {d: i for i, d in enumerate(df['Driver'].unique())}

input_data = pd.DataFrame([{
    'LapNumber': lap,
    'Stint': stint_val,
    'Compound': compound_map[compound],
    'Driver': driver_map[driver]
}])

prediction = model.predict(input_data)[0]

st.success(f"Predicted Lap Time: {round(prediction, 3)} sec")

st.subheader("🏎️ Track Telemetry")

driver_tel = st.selectbox("Select Driver (Telemetry)", df['Driver'].unique())

telemetry = get_driver_telemetry(year, race, driver_tel)

st.line_chart(telemetry.set_index('Distance')['Speed'])

driver1 = st.selectbox("Driver 1", df['Driver'].unique())
driver2 = st.selectbox("Driver 2", df['Driver'].unique(), index=1)

tel1 = get_driver_telemetry(year, race, driver1)
tel2 = get_driver_telemetry(year, race, driver2)

st.subheader("⚔️ Speed Comparison")

import pandas as pd

compare = pd.DataFrame({
    driver1: tel1['Speed'].values[:len(tel2)],
    driver2: tel2['Speed'].values[:len(tel2)]
})

st.line_chart(compare)

render(df)