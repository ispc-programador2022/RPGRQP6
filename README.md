# RPGRQP6
## Proyecto GAMA

## INFORME Proyecto RPGRQP6

El presente proyecto fue realizado con la idea de extraer datos de los principales Granos y sus rindes a nivel Nacional en Argentina, 
debido a la gran diversidad de datos sobre los mismos se decidio relevar los rendimientos por hectarea y estimaciones de produccion para
el proximo año. Los datos fueron guardados en una base de datos para posteriormente ser consultado en una aplicacion realizada con python
y herramientas de la misma como pandas, reorganizandose para poder visualizarlos de una manera ordenada.
Creemos relevantes estos datos para la mejora en el rendimiento del cultivo la directa implicancia en la economia nacional y una mejora sostenida,
en la rotacion del cultivo como asi la afectacion de variables accesorias como el clima.

Al consultar la aplicacion, podemos observar:

TRIGO 
Entre los periodos 2021/2022 y 2022/2023 existe una variacion del -14.5% del area sembrada, con una disminucion del rinde por hectarea sembrada -33.4%, 
y una disminucion final en este periodo en relacion al periodo anterior de -48.7%

MAIZ
Entre los periodos 2021/2022 y 2022/2023 existe una variacion del -8.6%% del area sembrada, con un rinde mayor del maiz por sobre el trigo respecto a las hectareas sembradas, con una produccion notablemente mayor.

SOJA
Entre los periodos 2021/2022 y 2022/2023 existe una variacion del 6.2% del area sembrada, con un rinde en el peridodo 2021/2022 menor al trigo y al maiz, aun habiendose sembrado una mayor area, pero resultando en una produccion mayor, al maiz y menor al trigo, esto puede estarse viendo afectados por otras variables que no se han tenido en cuenta en el presente estudio, seria muy interesante agregar otros datos como el tipo de semilla utilizada, diferenciacion por provincia, estado de la tierra, afectaciones climatologicas historicas bajo fenomenos del niño/niña.



> Al clonar este repo, hay tener instalado las siguiente librerias:

- Pandas
- Sqlite3
- requests
- Beautiful Soup

####Se ejecuta el archivo **app.py**

Si se quiere imprimir las tablas, hay que ejecutar el **guardar_csv.py** siguiendo las indicaciones que hay en el mismo.

<sup>El archivo *test.py* es solo una prueba todo en uno, tambien se puede ejecutar solo.</sup>
