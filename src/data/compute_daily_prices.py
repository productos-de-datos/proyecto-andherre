
""""


Módulo de cálculo de precios promedio diarios.
-------------------------------------------------------------------------------
En este módulo se toma el archivo precios-horarios.csv, con la finalidad de obtener
por cada día el precio promedio que tuvo la electricidad en la bolsa nacional.
>>> compute_daily_prices()

compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")

import pandas as pd

def compute_daily_prices():


    price_hourly = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    price_hourly = price_hourly.groupby('fecha').mean()
    price_hourly_nohour = price_hourly.drop(['hora'], axis=1)
    price_hourly_nohour.to_csv(
                                    'data_lake/business/precios-diarios.csv',
                                     header = True, index = True
                                     )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
