def apply_scenario(forecast_df, percent, mode="growth"):
    df = forecast_df.copy()

    if mode == "growth":
        df['yhat'] *= (1 + percent/100)

    elif mode == "conservative":
        df['yhat'] = df['yhat'] * (1 + percent/200)
        df['yhat'] = df['yhat'].rolling(3, min_periods=1).mean()

    elif mode == "shock":
        df['yhat'] *= (1 + percent/100)

        for i in range(0, len(df), 7):
            df.loc[i, 'yhat'] *= 1.2   
        for i in range(3, len(df), 10):
            df.loc[i, 'yhat'] *= 0.85 

        df['yhat_lower'] *= 0.7
        df['yhat_upper'] *= 1.3

    return df