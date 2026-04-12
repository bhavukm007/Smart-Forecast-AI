def baseline_forecast(df):
    rolling_avg = df['y'].rolling(window=3).mean()

    if rolling_avg.isna().all():
        return df['y'].mean()

    return rolling_avg.iloc[-1]