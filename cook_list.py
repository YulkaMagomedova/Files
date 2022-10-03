# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def file_to_dict(file, sep=' | '):
    counter = 0
    cook_book = dict()
    dish_name = str()
    with open(file, mode='r', encoding='UTF8') as opened_file:
        for line in opened_file:
            if line != '\n':
                if counter == 0:
                    dish_name = line.replace('\n', '')
                    cook_book.update({dish_name: []})
                if counter >= 2:
                    tmp_list = line.split(sep)
                    cook_book[dish_name].append({'ingredient_name': tmp_list[0],
                                                'quantity': int(tmp_list[1]), 'measure': tmp_list[2].replace('\n', '')})
            else:
                counter = -1
            counter += 1
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    tmp_list = []
    out_dict = {}
    for dish in cook_book:
        if dishes.count(dish) > 0:
            for ingredient in cook_book[dish]:
                for tmp_ingredient in tmp_list:
                    if tmp_ingredient['ingredient_name'] == ingredient['ingredient_name']:
                        tmp_list[tmp_list.index(tmp_ingredient)]['quantity'] += ingredient['quantity']
                        tmp_list[tmp_list.index(tmp_ingredient)]['quantity'] *= person_count
                        break
                else:
                    ingredient['quantity'] *= person_count
                    tmp_list.append(ingredient)
    for ingredient in tmp_list:
        engridient_name = ingredient['ingredient_name']
        ingredient.pop('ingredient_name')
        out_dict.update({engridient_name: ingredient})
    return out_dict


def enumerate_menu(in_dict):
    counter = 1
    out_dict = {}
    for dish in in_dict:
        out_dict.update({counter: dish})
        counter += 1
    return out_dict


def print_numerated_dict(numerated_dict):
    for number in numerated_dict:
        print(f"{number}. {numerated_dict[number]}")


def make_list(in_dict):
    out_list = []
    dish_number = -1
    print("Создаем список покупок.\nВыберите блюда.")
    print(f"Список блюд:")
    while len(in_dict) > 0 and dish_number != 0:
        numerated_dict = enumerate_menu(in_dict)
        print_numerated_dict(numerated_dict)
        print(f"Выберите блюдо {1}{f' - {len(in_dict)}' if len(in_dict) > 1 else f''}. Введите 0 для подсчета:\n")
        read_number = input()
        dish_number = int(read_number) if read_number.isdigit() else -1
        if dish_number in numerated_dict.keys():
            print(f"Добавили: '{list(in_dict.keys())[dish_number - 1]}'.")
            out_list.append(list(in_dict.keys())[dish_number - 1])
            in_dict.pop(list(in_dict.keys())[int(dish_number) - 1])
            if len(in_dict) > 0:
                print(f'\nДобавить следующее блюдо?')
        elif dish_number != 0:
            print("Неверный ввод!\n")
    return out_list


def get_person_number():
    person_number = -1
    print("\nНа сколько персон готовить?\n")
    while person_number == -1:
        read_number = input()
        if read_number.isdigit() and int(read_number) > 0:
            person_number = int(read_number)
        else:
            print(f"Неверный ввод!\nВведите целое положительное число.\nНа сколько персон готовить?:")
    return person_number


def print_shopping_list(in_list):
    print("\nСписок покупок:")
    counter = 1
    for ingredient in in_list:
        print(f'{counter}. {ingredient}: {in_list[ingredient]["quantity"]} '
              f'{in_list[ingredient]["measure"]}')
        counter += 1


def menu():
    cook_book = file_to_dict('file.txt')
    ingredient_list = make_list(file_to_dict('file.txt'))
    person_number = get_person_number()
    ingredient_list = get_shop_list_by_dishes(cook_book, ingredient_list, person_number)
    print_shopping_list(ingredient_list)


menu()
