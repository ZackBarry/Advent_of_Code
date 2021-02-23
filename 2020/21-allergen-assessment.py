
input = open('2020/21-input.txt').read().splitlines()

input = [x.split(' (contains ') for x in input]

input = [[x[0].split(' '), x[1][:-1].split(', ')] for x in input]

data = {}
all_ingredients = set()
ingredient_freq = {}

for item in input:
    ingredients, allergens = set(item[0]), item[1]
    all_ingredients = all_ingredients.union(ingredients)
    for a in allergens:
        if a in data:
            data[a] = set.intersection(data[a], ingredients)
        else:
            data[a] = ingredients
    for i in ingredients:
        if i in ingredient_freq:
            ingredient_freq[i] += 1
        else:
            ingredient_freq[i] = 1

# part 1

possible_allergens = set.union(*list(data.values()))
appearances = 0

for i in all_ingredients:
    if i not in possible_allergens:
        appearances += ingredient_freq[i]

print(appearances)

# part 2

found = set()
final_data = {}
num_allergens = len(data.keys())

while len(found) < num_allergens:
    for a, i in data.items():
        possible = set.difference(i, found)
        if len(possible) == 1:
            final_data[a] = list(possible)[0]
            found = found.union(possible)

result = ''

for i in sorted(final_data.keys()):
    result += f'{final_data[i]},'


print(result[:-1])
