content_ratings = {}
ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

for c_rating in ratings:
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
    print(content_ratings)

print('Final Dictionary: ' + max(content_ratings))

#Para AppleStore.csv

#opened_file = open('AppleStore.csv')
#from csv import reader
#read_file = reader(opened_file)
#apps_data = list(read_file)
#
#content_ratings = {}
#
#for row in apps_data[1:]:
    #c_rating = row[10]
    #if c_rating in content_ratings:
        #content_ratings[c_rating] += 1
    #else:
        #content_ratings[c_rating] = 1
#print(content_ratings)