def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.
    raise NotImplementedError("Implementar esta función")

    """
    import subprocess
    import os

    subprocess.call(["pip", "install", "openpyxl"])
    subprocess.call(["pip", "install", "xlrd"])

    import pandas as pd

    contents_landing = os.listdir('data_lake/landing')
    initial_year = 1995
    final_year = 2021

    for elemento in range(initial_year, final_year + 1, 1):
        
        archivo = pd.read_excel(f'data_lake/landing/{contents_landing[elemento-initial_year]}', skiprows=3)

        if archivo.columns[0] == 'Fecha':
            if archivo.shape[1] > 25:
                archivo = archivo.iloc[:, 0:25]         
        else:
            archivo = pd.read_excel(f'data_lake/landing/{contents_landing[elemento-1995]}', skiprows=2)
            if archivo.columns[0] == 'Fecha':
                if archivo.shape[1] > 25:
                    archivo = archivo.iloc[:, 0:25]
            else:
                archivo = pd.read_excel(f'data_lake/landing/{contents_landing[elemento-1995]}', skiprows=1)
                if archivo.columns[0] == 'Fecha':
                    if archivo.shape[1] > 25:
                        archivo = archivo.iloc[:, 0:25]
                else:
                    archivo = pd.read_excel(f'data_lake/landing/{contents_landing[elemento-1995]}', skiprows=0)
                    if archivo.columns[0] == 'Fecha':
                        if archivo.shape[1] > 25:
                            archivo = archivo.iloc[:, 0:25]                

        archivo['Fecha'] = pd.to_datetime(archivo['Fecha'])
        archivo.columns = ['Fecha', 'H00', 'H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23']
        archivo.to_csv(f'data_lake/raw/{elemento}.csv', header = True, index = False)

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()