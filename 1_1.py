cook_book = {}
path = "M:\Programs\Python_Git\Files_cooking"
with open('recipes.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip()
    while line:
        dish_name = line
        ingredients_count = int(file.readline().strip())
        ingredients = []

        for _ in range(ingredients_count):
            ingredient, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure})

        cook_book[dish_name] = ingredients
        file.readline()  # read an empty line between recipes
        line = file.readline().strip()

print(cook_book)
