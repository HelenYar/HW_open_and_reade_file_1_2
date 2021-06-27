from pprint import pprint

cook_book = {}

with open('recipes.txt', 'r', encoding="utf-8") as file:
    for line in file:
        dish = line.strip('\n')
        quantity = int(file.readline().strip())

        cb = []

        for i in range(quantity):
            ing = file.readline().strip('\n').split('|')
            i_book = {'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]}
            cb.append(i_book)

        emp_str = file.readline().strip()
        cook_book[dish] = cb
print('Cook_book =')
pprint(cook_book, width=150, sort_dicts=False)

shop_list = {}
s_l = {}


def get_shop_list_by_dishes(dishes, person):

        for dish, products in cook_book.items():
            if dishes.count(dish) > 0:
                for prod in products:
                    shop_list.update({prod.get('ingredient_name'): {'quantity':(int(prod.get('quantity'))*person), 'measure': prod.get('measure')}})
        print('')
        pprint(shop_list, width=100, sort_dicts=False)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)