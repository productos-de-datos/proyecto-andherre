"""
Módulo de preparación de datos para pronóstico.
-------------------------------------------------------------------------------
En este módulo se toma el archivo precios-diarios.csv y se obtiene una columna de clasificación según el día,
esto con la finalidad de tener datos separados (días anteriores y días posteriores) para posteriormente
hacer modelación y pronosticar.

>>> make_features()

"""

import pandas as pd


def make_features():
    """Prepara datos para pronóstico.
    Debido a que es una serie de tiempo no es necesario crear mas caracteristicas
    """
    try :
        dfp = pd.read_csv("data_lake/business/precios-diarios.csv")

        dfp.to_csv('data_lake/business/features/precios-diarios.csv',index=False)

        return dfp

    except : # pylint: disable=W0702
        return None

if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()