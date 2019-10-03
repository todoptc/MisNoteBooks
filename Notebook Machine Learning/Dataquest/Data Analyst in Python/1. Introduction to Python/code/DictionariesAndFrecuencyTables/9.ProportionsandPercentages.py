# La proporcion de x en un total es el numero de x/total
# Su porcentaje es la proporcion * 100

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for row in apps_data[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1

genre_counting
#El genero que mas se repite es Games        