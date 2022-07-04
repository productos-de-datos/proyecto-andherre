def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional

    raise NotImplementedError("Implementar esta función")

    """
   
    import pandas as pd

    price_hourly = pd.read_csv(f'data_lake/cleansed/precios-horarios.csv')
    price_hourly['fecha'] = pd.to_datetime(price_hourly['fecha'])
    price_hourly.set_index('fecha', inplace = True)
    price_month = price_hourly.resample('M').mean()
    price_month_nohour = price_month.drop(['hora'], axis=1)
    price_month_nohour.to_csv(f'data_lake/business/precios-mensuales.csv', header = True, index = True)


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
