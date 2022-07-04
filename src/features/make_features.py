def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    if __name__ == "__main__":
        import doctest
    make_features()
    doctest.testmod()

    if __name__ == "__main__":
    import doctest

    doctest.testmod()
    raise NotImplementedError("Implementar esta función")
    """
    
    import pandas as pd

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'])
    precios_diarios['dia_mes'] = precios_diarios['fecha'].dt.day
    precios_diarios['dia_mes_binario'] = (precios_diarios['dia_mes']>20).astype(int)
    precios_diarios.to_csv('data_lake/business/features/precios_diarios.csv', index = False)


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()



