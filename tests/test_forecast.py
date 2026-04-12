import pandas as pd
from baseline import baseline_forecast
from scenario import apply_scenario
from anomaly import detect_anomalies


def test_baseline():
    df = pd.DataFrame({"y": [10, 20, 30]})
    assert baseline_forecast(df) == 20


def test_scenario():
    df = pd.DataFrame({
        "ds": ["2023-01-01", "2023-01-02"],
        "yhat": [100, 200],
        "yhat_lower": [90, 180],
        "yhat_upper": [110, 220]
    })

    result = apply_scenario(df, 10, "growth")
    assert result['yhat'].iloc[0] == 110


def test_anomaly():
    df = pd.DataFrame({
        "ds": ["2023-01-01"],
        "y": [500]
    })

    forecast = pd.DataFrame({
        "ds": ["2023-01-01"],
        "yhat": [100],
        "yhat_lower": [90],
        "yhat_upper": [110]
    })

    anomalies = detect_anomalies(df, forecast)
    assert len(anomalies) == 1

def test_validation():
    df = pd.DataFrame({
        "ds": pd.date_range(start="2023-01-01", periods=20),
        "y": range(20)
    })
    from validation import validate_model
    assert validate_model(df) >= 0