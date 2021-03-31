# libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
from datetime import datetime
import pandas as pd


def scraping_symbol(driver, prices, symbol, name):
    # introducimos el símbolo
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               "input[name='yfin-usr-qry']"))) \
        .send_keys(symbol)
    # pulsamos el botón a buscar
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               'button#search-button'))) \
        .click()
    # seleccionamos datos históricos
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                               '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/section/div/ul/li[3]/a'))) \
        .click()
    # pulsamos en fechas
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
    #                                       '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div'))) \
    #    .click()
    # pulsamos en "max" para obtener
    # todas las fechas posibles
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
    #                                       '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[4]/button'))) \
    #    .click()
    # pulsamos en aplicar
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
    #                                       '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/button'))) \
    #    .click()
    # esperamos a que se cargue la tabla de precios
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[2]/table')))
    # recuperamos la tabla
    tabla_precios = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[2]/table')
    tabla_precios = tabla_precios.text
    # recorremos la lista
    for l in tabla_precios.split('\n')[1:-1]:
        fields = l.split(' ')
        save_price(prices, name, fields)


# función para actualizar o crear
# fila en el dataframe de precios
def save_price(prices, name, fields):
    fecha = fields[0] + '/' + meses[fields[1]] + '/' + fields[2]
    linea = prices.loc[(prices['name'] == name) & (prices['date'] == fecha)]
    #if (linea.empty() == True):
    #    linea = len(prices)
    prices.loc[len(prices)] = [name, fecha, fields[3], fields[4], fields[5], fields[6], fields[7], fields[8]]


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
        print('inicio' + row.symbol)
        scraping_symbol(driver, prices, row.symbol, row.name)

    prices.to_csv('historical_prices.csv', index=False)

    driver.quit()

meses = {'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04', 'may': '05', 'jun': '06',
         'jul': '07', 'ago': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'}

if __name__ == '__main__':
    start()