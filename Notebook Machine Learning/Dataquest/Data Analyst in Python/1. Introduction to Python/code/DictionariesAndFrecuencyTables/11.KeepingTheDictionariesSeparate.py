content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    proportions = content_ratings[key] / total_number_of_apps
    percentages = proportions * 100
    c_ratings_proportions[key] = proportions
    c_ratings_percentages[key] = percentages

print(content_ratings)
print(c_ratings_proportions)
print(c_ratings_percentages)
