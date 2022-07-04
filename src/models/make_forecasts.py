
"""Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.
    raise NotImplementedError("Implementar esta función")

    """
def test_train_datasets_1(data_frame, porcentaje):
    n = round(len(data_frame)*porcentaje)
    data_train = data_frame[:-n]
    data_test  = data_frame[-n:]
    return data_train, data_test
    
def make_forecasts():

    import pandas as pd
    import os
    import pickle

    daily_prices = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    daily_prices['fecha'] = pd.to_datetime(daily_prices['fecha'], format='%Y-%m-%d')
    daily_prices['dia_mes'] = pd.to_numeric(daily_prices['dia_mes'])
    daily_prices = daily_prices.set_index('fecha')
    daily_prices = daily_prices.asfreq('D')
    daily_prices = daily_prices.sort_index()
    daily_prices.index = pd.DatetimeIndex(daily_prices.index).to_period('D')

    data_train, data_test = test_train_datasets_1(daily_prices, 0.3)

    with open('src/models/precios-diarios.pkl', 'rb') as file:
        estimador = pickle.load(file)

    #estimador =  pickle.load('src/models/precios-diarios.pkl', 'rb')
    
    steps = len(data_test)

    projected_price = estimador.forecast(steps, exog = data_test[['dia_mes']])

    predictions =  pd.DataFrame(projected_price)

    data_pred = pd.concat([data_test.loc[:, ['precio']], predictions], axis=1, join = 'inner')
    data_pred = data_pred.reset_index()
    data_pred.columns = ['fecha', 'precio_promedio_real', 'precio_promedio_pred']

    data_pred.to_csv('data_lake/business/forecasts/precios-diarios.csv', index = False)

if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod() 

