# Sistema de Recomendación de Películas

Este proyecto es un sistema de recomendación de películas basado en la similitud de contenido. Toma la información de películas, para identificar películas similares a la que un usuario elige.
Este proyecto lo dividí en dos notebooks, el primero consiste en la [Transformacion de los datos y las funciones](https://github.com/agusvaldes/fast-api/blob/main/proyecto1_recomendacion_peliculas.ipynb) y el segundo notebook en el [Análisis exploratorio de los datos y el Machine learning](https://github.com/agusvaldes/fast-api/blob/main/eda_y_ml.ipynb)

## Preprocesamiento de Datos

[Transformaciones de los datos](https://github.com/agusvaldes/fast-api/blob/main/proyecto1_recomendacion_peliculas.ipynb)
Los datos utilizados en este proyecto provienen de un archivo CSV que contiene información de películas. [Dataset](https://github.com/agusvaldes/fast-api/blob/main/movies_dataset.csv)
* El df tenia columnas anidadas como 'belong_to_collection', 'genres', 'production_companies', 'production_countries' y 'spoken languages'. Se procedio a desanidar estas columnas para trabajar más facilmente con los datos. Fue un proceso en el que se tomó los valores de los diccionarios, se los almacenó en una nueva columna y luego, se realizó un split para que en cada registro hubieran valores unicos.
* Modifiqué los valores nulos de los campos 'revenue' y 'budget'
* El formato de la columna 'release_date' se modificó a AAAA-mm-dd.También cree la columna 'release_year' extrayendo el año de 'release_date'.
* Creamos la columna de retorno = revenue/budget.
* Eliminamos columnas innecesarias.

[Dataset modificado](https://github.com/agusvaldes/fast-api/blob/main/movies_final.csv)

Una de las tareas más importantes fue la creación de una nueva columna llamada "combined_features", esta columna combina varias características en una sola cadena de texto, que luego se convierte en una matriz de recuentos utilizando CountVectorizer.

## Recomendación de Películas

[Sistema de recomendación](https://github.com/agusvaldes/fast-api/blob/main/eda_y_ml.ipynb)
El sistema de recomendación se basa en un modelo de K-vecinos más cercanos (K-Nearest Neighbors, KNN). Este modelo utiliza la matriz de recuentos generada en el paso anterior para encontrar las películas más similares a la que un usuario elige.

Originalmente, el sistema de recomendación se basaba en un enfoque de similitud de coseno, donde calculábamos la similitud de coseno entre todas las parejas de películas. Sin embargo, esta aproximación resultó ser muy costosa en términos de memoria y rendimiento, ya que la matriz de similitudes era demasiado grande para manejarla eficientemente.

Para resolver este problema, cambiamos a un modelo de K-vecinos más cercanos, que es más eficiente en términos de uso de memoria y rendimiento. En lugar de calcular y almacenar las similitudes de todas las parejas de películas, el modelo KNN permite identificar las películas más similares a una película dada de manera más eficiente, sin tener que almacenar todas las similitudes.

## Funciones Adicionales

Además de la función principal de recomendación de películas, el proyecto también incluye varias funciones adicionales para interactuar con los datos de las películas. Estas funciones permiten:

- Obtener la cantidad de películas estrenadas en un mes específico.
- Obtener la cantidad de películas estrenadas en un dia de la semana en específico.
- Obtener la cantidad de películas producidas en un país específico.
- Obtener la cantidad de películas que pertenecen a una franquicia específica.
- Obtener la cantidad de películas que pertenecen a una productora específica.
- Obtener información detallada de una película específica, incluyendo la inversion, la ganancia, el retorno y el año.

## Links

* Repositorio (Github): https://github.com/agusvaldes/fast-api
* Deploy del Proyecto (Render): https://agustinvaldes-machine-learning-henry.onrender.com/docs#/
* Video (Youtube): https://youtu.be/kTbUL2wV8Wg
