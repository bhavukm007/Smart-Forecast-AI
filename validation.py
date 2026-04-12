from sklearn.metrics import mean_absolute_percentage_error
from prophet import Prophet

def validate_model(df):
    df = df.sort_values('ds')  
    split = int(len(df) * 0.7)

    train = df[:split]
    test = df[split:]

    model = Prophet(changepoint_prior_scale=0.1)  
    model.fit(train)

    future = model.make_future_dataframe(periods=len(test))
    forecast = model.predict(future)

    preds = forecast['yhat'][-len(test):].values
    actual = test['y'].values

    mape = mean_absolute_percentage_error(actual, preds) * 100

    return round(mape, 2)