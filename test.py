from bs4 import BeautifulSoup
import requests
import sqlite3


##########################################
def cargar_datos_proyecciones():

    html_text = requests.get('https://www.bcr.com.ar/es/mercados/gea/estimaciones-nacionales-de-produccion/estimaciones').text
    #print(html_text) #response 200
    soup = BeautifulSoup(html_text, 'lxml')
    estimaciones = soup.find('div', class_ = 'table-estimaciones-responsive')

    #me trae todas las tablas de cada cultivo
    #cultivos = estimaciones.find_all('table', class_ = 'bcr-estimaciones')

    #Tabla del Trigo
    trigo = estimaciones.find('table', class_ = 'bcr-estimaciones trigo color')

    listado_header = []
    cabecera_trigo = trigo.thead.find_all('th')
    for head in cabecera_trigo:
        listado_header.append(head.text)

    listado_ultimo_anio = []
    ultimo_anio = trigo.tbody.find_all('tr')[0]
    data1 = ultimo_anio.find_all('td')
    for d in data1:
        listado_ultimo_anio.append(d.text)

    listado_anio_anterior = []
    ultimo_anio = trigo.tbody.find_all('tr')[1]
    data2 = ultimo_anio.find_all('td')
    for d2 in data2:
        listado_anio_anterior.append(d2.text)

    trigo_ultimo_anio = (listado_header[0], listado_ultimo_anio[0], listado_ultimo_anio[1].replace('MILLONES HA', ' MILLONES HA'), listado_ultimo_anio[2].replace('QQ/HA', ' QQ/HA'), listado_ultimo_anio[3].replace('MILLONES TN', ' MILLONES TN'))
    trigo_anio_anterior = (listado_header[0], listado_anio_anterior[0], listado_anio_anterior[1].replace('MILLONES HA', ' MILLONES HA'), listado_anio_anterior[2].replace('QQ/HA', ' QQ/HA'), listado_anio_anterior[3].replace('MILLONES TN', ' MILLONES TN'))

    #print(trigo_anio_anterior)

    #Tabla del maiz
    maiz = estimaciones.find('table', class_ = 'bcr-estimaciones maiz color')

    listado_header_m = []
    cabecera_maiz = maiz.thead.find_all('th')
    for head in cabecera_maiz:
        listado_header_m.append(head.text)

    listado_ultimo_anio_m = []
    ultimo_anio_m = maiz.tbody.find_all('tr')[0]
    data = ultimo_anio_m.find_all('td')
    for d in data:
        listado_ultimo_anio_m.append(d.text)

    listado_anio_anterior_m = []
    ultimo_anio_m = maiz.tbody.find_all('tr')[1]
    data2 = ultimo_anio_m.find_all('td')
    for d2 in data2:
        listado_anio_anterior_m.append(d2.text)

    maiz_ultimo_anio = (listado_header_m[0], listado_ultimo_anio_m[0], listado_ultimo_anio_m[1].replace('MILLONES HA', ' MILLONES HA'), listado_ultimo_anio_m[2].replace('QQ/HA', ' QQ/HA'), listado_ultimo_anio_m[3].replace('MILLONES TN', ' MILLONES TN'))
    maiz_anio_anterior = (listado_header_m[0], listado_anio_anterior_m[0], listado_anio_anterior_m[1].replace('MILLONES HA', ' MILLONES HA'), listado_anio_anterior_m[2].replace('QQ/HA', ' QQ/HA'), listado_anio_anterior_m[3].replace('MILLONES TN', ' MILLONES TN'))

    ###### Tabla de la Soja
    soja = estimaciones.find('table', class_ = 'bcr-estimaciones soja color')

    listado_header_s = []
    cabecera_soja = soja.thead.find_all('th')
    for head in cabecera_soja:
        listado_header_s.append(head.text)

    listado_ultimo_anio_s = []
    ultimo_anio_s = soja.tbody.find_all('tr')[0]
    data = ultimo_anio_s.find_all('td')
    for d in data:
        listado_ultimo_anio_s.append(d.text)

    listado_anio_anterior_s = []
    ultimo_anio_s = soja.tbody.find_all('tr')[1]
    data2 = ultimo_anio_s.find_all('td')
    for d2 in data2:
        listado_anio_anterior_s.append(d2.text)

    soja_ultimo_anio = (listado_header_s[0], listado_ultimo_anio_s[0], listado_ultimo_anio_s[1].replace('MILLONES HA', ' MILLONES HA'), listado_ultimo_anio_s[2].replace('QQ/HA', ' QQ/HA'), listado_ultimo_anio_s[3].replace('MILLONES TN', ' MILLONES TN'))
    soja_anio_anterior = (listado_header_s[0], listado_anio_anterior_s[0], listado_anio_anterior_s[1].replace('MILLONES HA', ' MILLONES HA'), listado_anio_anterior_s[2].replace('QQ/HA', ' QQ/HA'), listado_anio_anterior_s[3].replace('MILLONES TN', ' MILLONES TN'))

    #######################################
    ##BASE DE DATOS
    conexion = sqlite3.connect("agricultura_test.db")
    #Para crear una tabla, creamos una variable de tipo cursor
    cursor = conexion.cursor()

    #chequeamos si existe la tabla
    print('Verificamos si la tabla ya existe')
    listTables = cursor.execute("select 'proyecciones_test' from sqlite_master where type='table'").fetchall()

    if listTables == []:
        print('...Creando tabla')
        #Creamos la tabla proyecciones
        cursor.execute(f"CREATE TABLE proyecciones_test (cultivo VARCHAR(100), periodo VARCHAR(100), {listado_header[1]} VARCHAR(100), {listado_header[2]} VARCHAR(100), {listado_header[3]} VARCHAR(100))")

    else:
        print('Tabla encontrada')

    # Ingresar y leer varios registros al mismo tiempo
    cultivos_gral = [
        trigo_ultimo_anio,
        trigo_anio_anterior,
        maiz_ultimo_anio,
        maiz_anio_anterior,
        soja_ultimo_anio,
        soja_anio_anterior
    ]
    cursor.executemany("INSERT INTO proyecciones_test VALUES (?,?,?,?,?)", cultivos_gral)

    #Guardo los cambios
    conexion.commit()

    conexion.close()

def eliminar_datos_proyecciones():
        #### Borramos las filas de la tabla
        conexion = sqlite3.connect("agricultura_test.db")
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM proyecciones_test')
        print('Se han eliminado', cursor.rowcount, 'filas de la tabla.')
        conexion.commit()
        conexion.close()

def consultar_trigo():
        conexion = sqlite3.connect("agricultura_test.db")
        cursor = conexion.cursor()
        ##  print fila especifica
        cursor.execute('select * from proyecciones_test where (cultivo=:t)', {'t':'Trigo'})
        busqueda = cursor.fetchall()
        for i in busqueda:
            print(i)
        conexion.close()


##########################################3


while True:
    cargar_datos_proyecciones()
    #####
    print('Ingresa la opción deseada: ')
    print("""
    \t 1 - Ver proyecciones de la producción de granos en el último año
    \t 2 - Ver proyecciones del trigo y su variacion
    \t 3 - Ver proyecciones del maiz y su variacion
    \t 4 - Ver proyecciones de la soja y su variacion
    """)
    opcion = input('>')

    if opcion == '1':

        conexion = sqlite3.connect("agricultura_test.db")
        cursor = conexion.cursor()
        # haceoms consulta a la bd
        for row in cursor.execute('select * from proyecciones_test'):
            print(row)
        eliminar_datos_proyecciones()
    
    elif opcion == '2':
        consultar_trigo()
        eliminar_datos_proyecciones()
    else:
        print('Hasta luego!')
        eliminar_datos_proyecciones()
        break


