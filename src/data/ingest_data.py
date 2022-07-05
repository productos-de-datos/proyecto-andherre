"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
En este módulo se descargan los datos externos y se almacenan en la carpeta landing del data lake

>>> ingest_data()

"""

import urllib.request

def ingest_data():
    """
    Realiza la ingesta de datos
    """
    # raise NotImplementedError("Implementar esta función")
    get_urls()
    get_files()

def get_urls():
    with open('urls.txt','w') as f:

        for year in range(1995,2022):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
            if year not in [2016,2017]:
                url = url + str(year)+'.xlsx?raw=true'
                f.write(url)
                f.write('\n')
            else:
                url = url + str(year)+'.xls?raw=true'    
                f.write(url)
                f.write('\n')

def get_files():
    #cwd=os.getcwd()
    landing= 'data_lake/landing/'
    #landing='./data_lake/landing/'
    with open('./urls.txt','r') as f:
        for i in f.readlines():
            urllib.request.urlretrieve(i,landing+i.split('/')[-1].split('?')[0])

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()

