# Importamos las librerías
import pandas as pd 
import numpy as np
from fastapi import FastAPI

# Indicamos título y descripción de la API
app = FastAPI(title='Proyecto individual nro 1: Recomendacion de peliculas',
            description='API de datos y recomendaciones de películas')

#http://127.0.0.1:8000/


# Función para que el la API tome el dataframe
@app.get('/')
async def read_root():
    return {'¡Saludos! Estás en la API de recomendación de películas. Para obtener información adicional, visita la ruta /docs'}
    
@app.on_event('startup')
async def startup():
    global df
    df = pd.read_csv('movies_final.csv') 

# Función para reconocer el servidor local

@app.get('/')
async def index():
    return {'Te encuentras en la API de recomedación de peliculas, dirigite a /docs'}

@app.get('/about/')
async def about():
    return {'Proyecto individual Nº1: Recomendacion de peliculas'}


# Función de películas por mes

@app.get('/peliculas_mes/({mes})')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes 
    (nombre del mes, en str, ejemplo 'enero') historicamente
    ''' 
    mes = mes.lower()
    meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12}

    mes_numero = meses[mes]

    # Convertir la columna "fecha" a un objeto de tipo fecha
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Tratamos la excepciòn
    try:
        month_filtered = df[df['release_date'].dt.month == mes_numero]
    except (ValueError, KeyError, TypeError):
        return None

    # Filtramos valores duplicados del dataframe y calculamos
    month_unique = month_filtered.drop_duplicates(subset='id')
    respuesta = month_unique.shape[0]

    return {'mes':mes, 'cantidad de peliculas':respuesta}


# Función de películas por día

@app.get('/peliculas_dia/({dia})')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se 
    estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente
    '''
    # Creamos diccionario para normalizar
    days = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'}

    day = days[dia.lower()]

    # Filtramos los duplicados del dataframe y calculamos
    lista_peliculas_day = df[df['release_date'].dt.day_name() == day].drop_duplicates(subset='id')
    respuesta = lista_peliculas_day.shape[0]

    return {'dia': dia, 'cantidad de peliculas': respuesta}

@app.get('/franquicia/({franquicia})')
def franquicia(franquicia):
    # Convertimos la entrada del usuario a minúsculas
    franquicia = franquicia.lower()

    # Filtramos el DataFrame para quedarnos solo con las peliculas que pertenecen a la franquicia ingresada
    # Convertimos los datos de la columna a minúsculas antes de hacer la comparación
    peliculas_franquicia = df[df['collection'].str.lower() == franquicia].drop_duplicates(subset='id')

    # Calculamos la cantidad de peliculas de la franquicia
    cantidad = len(peliculas_franquicia)

    # Calculamos la ganancia total sumando 'revenue'
    ganancia_total = peliculas_franquicia['revenue'].sum()

    # Calculamos el promedio total dividiendo la ganancia total por la cantidad de películas
    ganancia_promedio = ganancia_total / cantidad if cantidad > 0 else 0

    return {'franquicia': franquicia, 'cantidad de peliculas': cantidad, 'ganancia total': ganancia_total, 'ganancia promedio': ganancia_promedio}



# Función películas por país

@app.get('/peliculas_pais/({pais})')
def peliculas_pais(pais:str):
    '''
    Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo
    '''
    
    # Filtramos el dataframe y contamos filas
    movies_filtered = df[(df['country'].str.lower() == pais.lower())]
    movies_unique = movies_filtered.drop_duplicates(subset='id')    
    respuesta = movies_unique.shape[0]
    
    return {'pais':pais, 'cantidad de peliculas':respuesta}


# Función métricas por productora

@app.get('/productoras/({productora})')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron
    ''' 

    productora = productora.lower()

    # Filtramos el dataframe
    # Convertimos los datos de la columna a minusculas antes de hacer la comparación
    lista_peliculas_productoras = df[df['company'].str.lower() == productora].drop_duplicates(subset='id')

    # Calculamos
    cantidad_peliculas_prod = (lista_peliculas_productoras).shape[0]
    revenue_prod = lista_peliculas_productoras['revenue'].sum()

    return {'productora': productora, 'ganancia_total': revenue_prod, 'cantidad': cantidad_peliculas_prod}


# Función métricas por película

@app.get('/retorno/({pelicula})')
def retorno(pelicula):
    # Convertimos la entrada del usuario a minúsculas
    pelicula = pelicula.lower()

    # Filtramos el DataFrame
    # Convertimos los datos de la columna a minúsculas antes de hacer la comparación
    info_pelicula = df[df['title'].str.lower() == pelicula].drop_duplicates(subset='title')

    pelicula_nombre = info_pelicula['title'].iloc[0]
    inversion_pelicula = str(info_pelicula['budget'].iloc[0])
    ganancia_pelicula = str(info_pelicula['revenue'].iloc[0])
    retorno_pelicula = str(info_pelicula['return'].iloc[0])
    year_pelicula = str(info_pelicula['release_year'].iloc[0])

    return {'pelicula': pelicula_nombre, 'inversion': inversion_pelicula, 'ganancia': ganancia_pelicula, 'retorno': retorno_pelicula, 'año': year_pelicula}
# ,,,,,,,,SAD,ASD
