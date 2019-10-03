"""
Una vez que sabemos el max y el min y definimos nuestros intervalos que no tienen porque comenzar en 
el min y finzlizar en el max, podemos continuar con el calculo de la frecuencia para cada intervalo.
Queremos almacenar la tabla de frecuencias como un diccionario, para ello comenzamos creando un 
diccionario con los intervalos como claves del diccionario y las frecuencias como valores del diccionario.  
Inicializamos todas las frecuencias a 0
"""
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = {'0 - 10 MB': 0, '10 - 50 MB': 0, '50 - 100 MB': 0, '100 - 500 MB': 0, '500 MB +': 0}

# Seguidamente recorremos nuestro set de datos con un for
# Almacenamos el tamaño del set en una variable float llamada data_size
# Dividimos los datos en los intervalos con clausulas if y elif incrementando en 1 cada intervalo
# dependiendo si el dato pertenece a el o no

for row in apps_data[1:]:
    data_size = float(row[2])

    if data_size <= 10000000:
        data_sizes['0 - 10 MB'] += 1

    elif 10000000 < data_size <= 50000000:
        data_sizes['10 - 50 MB'] += 1

    elif 50000000 < data_size <= 100000000:
        data_sizes['50 - 100 MB'] += 1

    elif 100000000 < data_size <= 500000000:
        data_sizes['100 - 500 MB'] += 1

    elif data_size > 500000000:
        data_sizes['500 MB +'] += 1

print(data_sizes)

"""
Ejercicio

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

tot_ratings = []
for row in apps_data[1:]:
    rating = int(row[5])
    tot_ratings.append(rating)
    
ratings_min = min(tot_ratings)    
ratings_max = max(tot_ratings)

data_tot_ratings = {'0 - 10 Rat': 0, '10 - 15 Rat': 0, '15 - 20 Rat': 0, '20 - 25 Rat': 0, '25 Rat +': 0, }

for row in apps_data[1:]:
    tot_rating = int(row[5])
    
    if tot_rating <= 1000000:
        data_tot_ratings['0 - 10 Rat'] += 1
    elif 1000000 < tot_rating <= 1500000:
        data_tot_ratings['10 - 15 Rat'] += 1
    elif 1500000 < tot_rating <= 2000000:
        data_tot_ratings['15 - 20 Rat'] += 1
    elif 2000000 < tot_rating <= 2500000:
        data_tot_ratings['20 - 25 Rat'] += 1
    elif tot_rating > 2500000:
        data_tot_ratings['25 Rat +'] += 1

data_tot_ratings 

Resultado:
{'0 - 10 Rat': 7191,
 '10 - 15 Rat': 2,
 '15 - 20 Rat': 1,
 '20 - 25 Rat': 2,
 '25 Rat +': 1}
"""