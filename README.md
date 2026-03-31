# F1 Performance Analytics System

## Overview
End-to-end data analytics system for Formula 1 race performance using FastF1 API.

## Features
- Data ingestion (FastF1 API)
- Data pipeline with caching
- Race pace analysis
- Tire degradation analysis
- Interactive dashboard (Streamlit)

## Tech Stack
- Python
- Pandas
- FastF1
- Streamlit
- Matplotlib / Seaborn

## Run Locally

```bash
pip install -r requirements.txt
python -m pipelines.run_pipeline
streamlit run dashboard/app.py

Project Structure:

f1-performance-analytics/
├── src/
├── pipelines/
├── dashboard/
├── data/

Output
Race pace ranking
Lap time distribution
Tire degradation insights