mi_variable = "Hola Mundo"
print(mi_variable)
#Lista de numeros
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
#Diccionario

mi_diccionario = { "clave_1" : "valor1", "clave_2" : "valor2", "clave_3" : "valor3" }
print(mi_diccionario)

###################################
vector_de_enteros = [10]*5
print(vector_de_enteros)

vector_flotantes = [3.14]*5
print(vector_flotantes)

diccionario={ "entero" : vector_de_enteros, "flotante" : vector_flotantes}
print(diccionario)
# Python resalta los errores en el codigo para poder corregirlo, ESTAR ATENTO
vector_complejo = [(1 + 2j)] * 5
print(vector_complejo)
#CADENAS
cadena_simple = 'Hola mundo!'
print(cadena_simple)
cadena_doble = ["PYTHON ES PODEROSO", "ME GUSTA"]
print(cadena_doble)

##########################
#Python cuenta desde el cero (indice cero)
#dataframe
#con "pd" llamamos a la librería pandas
import pandas as pd

#crear una tabla de rendimiento de amigos en distintos juegos(dta frame)
datos = {
    'Nombre': ['Juan', 'Robert', 'Frixon', 'Cartman'],
    'Juego 1 (puntos)': [150, 180, 130, 200],
    'Juego 2 (puntos)': [120, 90, 110, 150],
    'Juego 3 (puntos)': [200, 160, 180, 190]
}

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)



