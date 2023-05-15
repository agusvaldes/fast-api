# Sistema de Recomendación de Películas

Este proyecto es un sistema de recomendación de películas basado en la similitud de contenido. Toma datos de películas, como su sinopsis, géneros, director, y actores, para identificar las películas similares a la que un usuario elige.

## Preprocesamiento de Datos

Los datos utilizados en este proyecto provienen de un archivo CSV que contiene información de películas. La columna de descripción de cada película (overview) se procesa utilizando técnicas de procesamiento de lenguaje natural para obtener características que describan cada película.

El archivo CSV se procesa de la siguiente manera:

* Se leen los datos del archivo CSV.
* Se limpian y procesan los datos. Por ejemplo, se extrajeron los nombres de las colecciones de películas de la columna 'belongs_to_collection' utilizando una expresión regular.
* Se extraen las características importantes de las películas, como la descripción, los actores, los directores y los géneros.
* Se combinan estas características en una sola cadena de texto, que luego se convierte en una matriz de recuentos utilizando CountVectorizer.

## Recomendación de Películas

El sistema de recomendación se basa en un modelo de K-vecinos más cercanos (K-Nearest Neighbors, KNN). Este modelo utiliza la matriz de recuentos generada en el paso anterior para encontrar las películas más similares a la que un usuario elige.

Originalmente, el sistema de recomendación se basaba en un enfoque de similitud de coseno, donde calculábamos la similitud de coseno entre todas las parejas de películas. Sin embargo, esta aproximación resultó ser muy costosa en términos de memoria y rendimiento, ya que la matriz de similitudes era demasiado grande para manejarla eficientemente.

Para resolver este problema, cambiamos a un modelo KNN, que es más eficiente en términos de uso de memoria y rendimiento. En lugar de calcular y almacenar las similitudes de todas las parejas de películas, el modelo KNN permite identificar las películas más similares a una película dada de manera más eficiente, sin tener que almacenar todas las similitudes.

## Funciones Adicionales

Además de la función principal de recomendación de películas, el proyecto también incluye varias funciones adicionales para interactuar con los datos de las películas. Estas funciones permiten:

- Obtener la cantidad de películas estrenadas en un mes específico.
- Obtener la cantidad de películas producidas en un país específico.
- Obtener la cantidad de películas que pertenecen a una franquicia específica.
- Obtener información detallada de una película específica, incluyendo

## Links

* Repositorio (Github): https://github.com/agusvaldes/fast-api
* Deploy del Proyecto (Render): https://agustinvaldes-machine-learning-henry.onrender.com/docs#/
* Video (Youtube): 