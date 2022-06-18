# Task_1

file_name = "recipes.txt"

def files_to_dict(file_name):
    with open(file_name, encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            ingredients = []
            name_position = ['ingredient_name', 'quantity', 'measure']
            for item in range(int(file_obj.readline().strip())):
                ingredient = file_obj.readline()
                ingredient = ingredient.split('|')
                ingredients.append({name_position[0]: ingredient[0].strip(),
                                    name_position[1]: int(ingredient[1].strip()),
                                    name_position[2]: ingredient[2].strip()})
            cook_book[dish] = ingredients
            file_obj.readline()
        return cook_book

print(files_to_dict(file_name))

