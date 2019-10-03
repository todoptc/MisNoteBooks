"""
Cuando tenemos una tabla de frecuencias enorme es dificil de analizar y de ver un patron
por lo que para ello podemos crear intervalos de valores bien definidos y contar la
frecuencia de esos intervalos lo que nos facilitara el segmentar los datos  en grupos
y analizarlos facilmente.  Para crear los intervalos debemos saber el valor min y max de la columna
con los comandos min() y max() podemos saber los valores min y max de cualquier lista de enteros
o flotantes.  Para ello aislaremos la columna de los datos del csv en una lista aparte y hayaremos 
su max y min
"""
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for row in apps_data[1:]:
    size = float(row[2]) #vamos recorriendo la columna y metiendo cada valor en la variable size
    data_sizes.append(size) #añadimos cada valos a la lista
    
min_size = min(data_sizes) # 589824.0
max_size = max(data_sizes) # 4025969664.0
