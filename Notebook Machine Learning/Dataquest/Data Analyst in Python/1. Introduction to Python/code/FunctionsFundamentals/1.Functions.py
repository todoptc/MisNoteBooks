a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

#print(len(a_list))
# Voy a crear la funcion len()

length = 0
for elements in a_list:
    length += 1

print(length)

# Voy a crear la funcion sum()
print(sum(a_list))

suma = 0
for elements in a_list:
    suma += elements

print(suma)