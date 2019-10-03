content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for iteration_variable in content_ratings:
    content_ratings[iteration_variable] /= total_number_of_apps
    content_ratings[iteration_variable] *= 100
    
percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']
percentage_15_allowed1 = 100 - content_ratings['17+']

print('15 years old: ', percentage_15_allowed)
print('15 years old1: ', percentage_15_allowed1)
print('plus than 17 years: ', percentage_17_plus)

""" 
frecuencias: Las veces que se repite un dato en un diccionario
proporciones : Se divide la frecuencia entre el numero total de datos
porcentaje: Se multiplica la proporcion * 100
"""
