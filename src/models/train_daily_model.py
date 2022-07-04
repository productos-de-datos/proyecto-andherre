
"""Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

    raise NotImplementedError("Implementar esta función")   
    
    Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
    
    """
    

def test_train_datasets_1(data_frame, porcentaje):
    n = round(len(data_frame)*porcentaje)
    data_train = data_frame[:-n]
    data_test  = data_frame[-n:]
    return data_train, data_test


def train_daily_model():
   
    #raise NotImplementedError("Implementar esta función")
    import os
    import pickle
    import pandas as pd
    import statsmodels.api as st

    price_daily = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    price_daily['fecha'] = pd.to_datetime(price_daily['fecha'], format='%Y-%m-%d')
    price_daily['dia_mes'] = pd.to_numeric(price_daily['dia_mes'])
    price_daily = price_daily.set_index('fecha')
    price_daily = price_daily.asfreq('D')
    price_daily = price_daily.sort_index()
    price_daily.index = pd.DatetimeIndex(price_daily.index).to_period('D')

    # Se parten los datos para entrenamiento y prueba
    data_train, data_test = test_train_datasets_1(price_daily, 0.3)

    forecaster = st.tsa.statespace.SARIMAX(
    endog = data_train[['precio']],
    exog = data_train[['dia_mes']],
    enforce_stationarity = False,
    enforce_invertibility = False,
    )

    model = forecaster.fit()
    pickle.dump(model, open('src/models/precios-diarios.pkl', 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()