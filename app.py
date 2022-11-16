import sqlite3
import pandas as pd
import funciones


while True:
    print("*********************************************")
    funciones.cargar_datos_proyecciones()
    funciones.cargar_datos_margenes()
    print("*********************************************\n")
    #####
    print('PROYECCIONES PARA LA PRODUCCION DE GRANOS EN ARGENTINA')
    print("""
\t 1 - Ver proyecciones de los granos en el último año
\t 2 - Ver proyecciones del trigo y su variacion
\t 3 - Ver proyecciones del maiz y su variacion
\t 4 - Ver proyecciones de la soja y su variacion
\t 5 - Ver sus margenes de la fecha de elaboración estimada
\t 6 - Ver cotización del trigo
\t 7 - Ver cotización del maiz
\t 8 - Ver cotización de la soja
\t 0 - Salir
""")
    print('Ingresa la opción deseada: ')
    opcion = input('>')
    print("*\n*\n*\n")

    if opcion == '1':

        conexion = sqlite3.connect("agricultura_test.db")
        cursor = conexion.cursor()
        # haceoms consulta a la bd
        #for row in cursor.execute('select * from proyecciones_test'):
        #    print(row)

        df = pd.read_sql_query('select * from proyecciones_test', conexion)
        # Ver  el resultado de la consulta SQL está
        # almacenado en el DataFrame
        print(">>> Proyecciones de la producción de granos: ")
        print(df.head())
        funciones.eliminar_datos_proyecciones()
        funciones.eliminar_datos_margenes()
    
    elif opcion == '2':
        funciones.consultar_trigo()
        funciones.eliminar_datos_proyecciones()
        funciones.eliminar_datos_margenes()

    elif opcion == '3':
        funciones.consultar_maiz()
        funciones.eliminar_datos_proyecciones()
        funciones.eliminar_datos_margenes()

    elif opcion == '4':
        funciones.consultar_soja()
        funciones.eliminar_datos_proyecciones()
        funciones.eliminar_datos_margenes()
    
    elif opcion == '5':
        
        conexion = sqlite3.connect("agricultura_test.db")
        cursor = conexion.cursor()
        df = pd.read_sql_query('select * from margenes_test', conexion)
        print(">>> Margenes de los granos principales: ")
        print(df.head())
        funciones.eliminar_datos_margenes()
    
    elif opcion == '6':
        print(funciones.cotizacion_trigo())
        funciones.eliminar_datos_margenes()

    elif opcion == '7':
        print(funciones.cotizacion_maiz())
        funciones.eliminar_datos_margenes()

    elif opcion == '8':
        print(funciones.cotizacion_soja())
        funciones.eliminar_datos_margenes()

    else:
        print('Hasta luego!')
        funciones.eliminar_datos_proyecciones()
        funciones.eliminar_datos_margenes()
        break

