"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
    raise NotImplementedError("Implementar esta función")
    """
   

    import os
    import urllib.request

    initial_year = 1995
    final_year = 2021
    range_year = list(range(initial_year, final_year + 1, 1))

    for anio in range_year:
        try:
            archivo = open(f'data_lake/landing/{anio}.xlsx', 'wb')
            ruta = urllib.request.urlopen(f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{anio}.xlsx?raw=true')
            archivo.write(ruta.read())
            archivo.close()
        except:
            archivo.close()
            os.remove(f'data_lake/landing/{anio}.xlsx')

            archivo = open(f'data_lake/landing/{anio}.xls', 'wb')
            ruta = urllib.request.urlopen(f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{anio}.xls?raw=true')
            archivo.write(ruta.read())
            archivo.close()

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()

