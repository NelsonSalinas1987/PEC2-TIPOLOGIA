# PEC2-TIPOLOGIA DE DATOS - WEB SCRAPING

En esta práctica se elabora un caso práctico orientado a aprender a identificar los datos relevantes por un proyecto analítico y usar las herramientas de extracción de datos.

### Recursos
1. Técnica: Web Scraping
2. Herramienta: Python
3. Análisis de información: R

### Integrantes
1. BOTIJA SANZ JAVIER
2. SALINAS VARAS NELSON

## 1.- Contexto
En la bolsa de valores existen grandes mercados para la inversión y movimientos de capital, por ejemplo el mercado de divisas donde se cotizan las relaciones del precio de la moneda de cada país, otra opción son las cotizaciones por acciones de empresas tales como por ejemplo Netflix, Facebook y otros, tambien existe el mercado de las materias primas; y es alli donde se enfocará el desarrollo de este análisis. El mercado de materia prima es una de las opciones de inversión a largo plazo (futuro) que puede representar beneficios sustanciales para la ganancia de dinero, pero para invertir se debe de apoyar con el respectivo análisis interno como externo dentro de los mercados internacionales.

#### Un ejemplo de este tipo de inversión es el siguiente:
1. Si el precio del maiz baja y la empresa que hace uso de esta materia prima puede mantener el mismo precio de produccion o en su efecto darle un mayor valor en el mercado, sin lugar a duda, existirá un beneficio, por el contrario si sube la materia prima y no puede alzar los costos, sus margenes se reducen por lo que el precio en bolsa baja.

El desarrollo de este trabajo se basa dentro del marco de analísis de informacion de cotizaciones historicas (4 meses) de comodities o materias primas tales como el arroz, soja, aceite de soja, cacao, café, algodon, azucar, oro, petroleo, gas natural, plata y gasolina con el fin de poder predecir en un periodo de tiempo los resultados probables que puedan existir para así tener una mejor visión en la toma de decisiones para la inversión a largo plazo. La web donde se obtendran los datos es Yahoo Finanzas https://es.finance.yahoo.com/. Para poder desarrollar el proyecto se dara pie al uso del websraping para la extracción de información de forma automática con el fin de obtener los datos más rapidamente y que el usuario o consumidor sea dueño de su propio análisis, mucho más alla de las interpretaciones que tienen otros analistas. Se toma en consideración el respeto y buen uso del scraping con el fin de evitar abuso o consumo excesivo de la pagina web, sin sobresaturar las peticiones web.

Se dará uso del lenguaje R, para poder establecer el modelo de regresion lineal simple para el analisis de predicciones, por fines educativos se tomará en consideración el analisis para los principales commodities:
1. Petróleo
2. Café

Los demas commodities que se encuentran en el dataset, tendran una representación con series temporales.

## 2.- Dataset
Su nombre se destaca como valores históricos de commodities en la bolsa de valores.

## 3.- Descripción del Dataset
El dataset comprende valores históricos para cada commoditie con la finalidad que sea utilizado por el lenguaje R, para fines de analisis con herramientas de predicción de datos, se toma en consideracion el valor de precio de cierre del mercado.

## 4.- Representación gráfica
Se dará uso del lenguaje R para el analisis de series temporales y predicción de modelos con regresión lineal simple.

## 5.- Contenido
El dataset comprende de varias columnas tales como:
1. Name: Hace referencia a las materias primas que fueron extraidas de la base de informacion de Yahoo Finanzas.
2. Date: Esta variable refleja el movimiento en el tiempo de cada materia prima, muy útil para la representación de series temporales.
3. Open: Comprende el valor de apertura que tuvo en el mercado de valores.
4. Max: Hace referencia al valor máximo del precio.
5. Min: Hace referencia al valor mínimo del precio.
6. Close: Representa el precio con el que cerro en el mercado.
7. AdjClose: Indica el precio de cierre ajustado.
8. Volume: Representa la fuerza que tuvo el precio en un determinado tiempo, muy util para determina si es alcista o bajista.

El periodo de tiempo en el que se recopilo la información es desde 05/11/2021 al 31/03/2021, lo que corresponde aproximandame 4 meses. Para la recopilación de los datos se uso las técnicas de web scraping, ademas como complementos en Python se integro Selenium y el driver de Google Chrome.

## 6.- Agradecimientos
Damos gracias a Yahoo Finanzas por darnos la oportunidad de poder extraer de forma automática los datos de las materias primas para el desarrollo de este trabajo. Es válido destacar que los mismos datos pueden ser obtenidos por otras fuentes según las necesidades del analista. Además debido a los constantes cambios tecnológicos, ya la inteligencia artificial en base al analisis de datos predictivos, está tomando lugar dentro del mercado bursátil.

## 7.- Inspiración
En vista a las previas investigaciones realizadas sobre los mercados bursatiles, ya se puede tener mayor confianza en que el desarrollo de la inteligencia artificial y análisis datos, puede generar un apoyo mas concreto al tomar una decisión para la inversión en bolsa, tomando como cita lo siguiente: "Según estimaciones de Nearshore Delivery Solutions, hasta un 30% de las decisiones financieras podrían llegar a tomarse con esta tecnología." Citado de: https://pulsosocial.com/2018/02/14/la-inteligencia-artificial-ya-puede-predecir-comportamiento-la-bolsa/, esto sin lugar a duda genera un impacto dentro del mundo de la bolsa de valores y genera una aportación sustancial a los procesos de automatización como es el scraping.

## 8.- Licencia
El tipo de licencia seleccionado es Released Under CC0: Public Domain License.

### Motivos:
Se considera necesario el aporte de otras personas que puedan crear mayor conocimiento en base a lo ya analizado, con el fin de motivar al desarrollo de mejores analisis y la distribución del conocimiento entre los interesados.

## 9.- Código
Se adjunta el codigo en lenguaje Python y R.

## 10.- DOI Dataset
