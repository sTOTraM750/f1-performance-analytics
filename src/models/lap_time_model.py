from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd


def prepare_features(df):
    df = df.copy()

    # Encode categorical features
    df['Compound'] = df['Compound'].astype('category').cat.codes
    df['Driver'] = df['Driver'].astype('category').cat.codes

    X = df[['LapNumber', 'Stint', 'Compound', 'Driver']]
    y = df['lap_time_sec']

    return X, y


def train_model(df):
    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    error = mean_absolute_error(y_test, predictions)

    return model, error