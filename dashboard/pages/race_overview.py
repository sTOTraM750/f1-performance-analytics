import streamlit as st
from src.visualization.plots import plot_race_pace, plot_distribution

def render(df):
    st.subheader("📊 Lap Time Distribution")

    fig1 = plot_distribution(df)
    st.pyplot(fig1)

    st.subheader("🏁 Race Pace Ranking (Visual)")

    pace = df.groupby("Driver")["lap_time_sec"].mean().sort_values()

    fig2 = plot_race_pace(pace)
    st.pyplot(fig2)