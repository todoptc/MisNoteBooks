opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+': 0 , '9+': 0, '12+': 0 , '17+': 0 }

for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
        
print(content_ratings)