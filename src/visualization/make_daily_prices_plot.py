def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    raise NotImplementedError("Implementar esta función")
    """
   
    import pandas as pd
    import matplotlib.pyplot as plt

    daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv')
    daily_prices['fecha'] = pd.to_datetime(daily_prices['fecha'])
    x = daily_prices.fecha
    y = daily_prices.precio
    plt.figure(figsize=(16, 8))
    plt.plot(x, y, 'g', label='Promedios Diarios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en bolsa')
    plt.title('Promedios Diarios')
    plt.grid()
    plt.legend()
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')

if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()