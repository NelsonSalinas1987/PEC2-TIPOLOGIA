# libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
from datetime import datetime
import pandas as pd
import sys

def scraping_symbol(driver, prices, symbol, sname):
    try:
        # reseteamos por si venimos de error
        driver.get('https://es.finance.yahoo.com/materias-primas')
        # introducimos el símbolo
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                   "input#yfin-usr-qry"))) \
            .send_keys(symbol)
        # pulsamos el primer resultado de la lista
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                   'div[role="link"][data-test="srch-sym"]'))) \
            .click()
        # esperamos hasta que el titulo contenga el símbolo buscado
        WebDriverWait(driver, 10).until(EC.title_contains(symbol))

        # seleccionamos datos históricos
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                   '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/section/div/ul/li[3]/a'))) \
            .click()
        # esperamos a que se cargue la tabla de precios
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                   '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[2]/table')))
        # recuperamos la tabla
        tabla_precios = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[2]/table')
        tabla_precios = tabla_precios.text
        # recorremos la lista
        for l in tabla_precios.split('\n')[1:-1]:
            fields = l.split(' ')
            save_price(prices, sname, fields)
    except:
        print(sys.exc_info())


# función para actualizar o crear
# fila en el dataframe de precios
def save_price(prices, n, f):
    fecha = f[0] + '/' + meses[f[1]] + '/' + f[2]
    linea = prices.loc[(prices['name'] == n) & (prices['date'] == fecha)]
    if linea.empty:
        prices.loc[len(prices)] = [n, fecha, s_to_n(f[3]), s_to_n(f[4]), s_to_n(f[5]),
                                   s_to_n(f[6]), s_to_n(f[7]), s_to_n(f[8])]
    else:
        linea['open'] = s_to_n(f[3])
        linea['max'] = s_to_n(f[4])
        linea['min'] = s_to_n(f[5])
        linea['close'] = s_to_n(f[6])
        linea['adjclose'] = s_to_n(f[7])
        linea['volume'] = s_to_n(f[8])


def s_to_n(sfield):
    if sfield == '-':
        return None
    else:
        return sfield.replace('.','').replace(',','.')

def start():
    symbols = pd.read_csv('symbols.csv', header=0)
    fileName = r".\historical_prices.csv"
    fileObj = Path(fileName)
    if fileObj.exists():
        prices = pd.read_csv('historical_prices.csv', header=0)
    else:  # si no existe, creamos el dataframe de cero
        prices = pd.DataFrame(columns=['name', 'date', 'open', 'max', 'min', 'close', 'adjclose', 'volume'])

    # Opciones de navegación
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disabled-extensions')

    # abrimos el navegador del driver
    driver_path = './chromedriver3'
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    # entramos en la página inicial de materias primas
    driver.get('https://es.finance.yahoo.com/materias-primas')
    # aceptamos la cookies
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               'button.btn.primary'))) \
        .click()

    # recorremos los símbolos a guardar
    for index, row in symbols.iterrows():
        print('inicio: ' + row[1] + '->' + row[0])
        scraping_symbol(driver, prices, row[0], row[1])

    prices.to_csv('historical_prices.csv', index=False)

    driver.quit()

meses = {'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04', 'may': '05', 'jun': '06',
         'jul': '07', 'ago': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'}

if __name__ == '__main__':
    start()