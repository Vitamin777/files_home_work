# Task_2

from pprint import pprint
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

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    dict_ingridients = {}
    for dish in dishes:
        list_ingridients = cook_book.get(dish)
        for ingridients in list_ingridients:
            dict_value = ingridients.copy()
            name_ingridient = dict_value.pop('ingredient_name')
            if name_ingridient not in dict_ingridients.keys():
                quantity_ingridient = dict_value.pop('quantity')
                dict_value.update(quantity=quantity_ingridient * person_count)
                dict_value_1 = {name_ingridient: dict_value}
                dict_ingridients.update(dict_value_1)
            else:
                # if the ingredients in the dishes are repeated
                dict_value_2 = dict_ingridients.get(name_ingridient)
                quantity2 = dict_value_2.get('quantity')
                quantity_ingridient = dict_value.pop('quantity')
                dict_value.update(quantity=quantity_ingridient * person_count+quantity2)
                dict_value_1 = {name_ingridient: dict_value}
                dict_ingridients.update(dict_value_1)
    return dict_ingridients

cook_book = files_to_dict(file_name)
dict_ingridients=get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
pprint(dict_ingridients)
print('\n')
dict_ingridients=get_shop_list_by_dishes(cook_book, ['Омлет', 'Омлет'], 1)
pprint(dict_ingridients)
print('\n')
dict_ingridients=get_shop_list_by_dishes(cook_book, ['Омлет' ], 2)
pprint(dict_ingridients)


