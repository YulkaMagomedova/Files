# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files

def file_to_dict(file, sep=' | '):
    c = 0
    cook_book = dict()
    dishname = str()
    with open(file, mode='r', encoding='UTF8') as f:
        for line in f:
            if line != '\n':
                if c == 0:
                    dishname = line.replace('\n', '')
                    cook_book.update({dishname: []})
                if c >= 2:
                    tmplist = line.split(sep)
                    cook_book[dishname].append({'ingredient_name': tmplist[0],
                                                'quantity': int(tmplist[1]), 'measure': tmplist[2].replace('\n', '')})
            else:
                c = -1
            c += 1
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    tmplist = []
    tmpdict = {}
    for i in cook_book:
        if dishes.count(i) > 0:
            for j in cook_book[i]:
                for k in tmplist:
                    if k['ingredient_name'] == j['ingredient_name']:
                        tmplist[tmplist.index(k)]['quantity'] += j['quantity']
                        tmplist[tmplist.index(k)]['quantity'] *= person_count
                        break
                else:
                    j['quantity'] *= person_count
                    tmplist.append(j)
    for i in tmplist:
        ti = i['ingredient_name']
        i.pop('ingredient_name')
        tmpdict.update({ti: i})
    return tmpdict


def enumerate_menu(in_dict):
    c = 1
    out_dict = {}
    for i in in_dict:
        out_dict.update({c: i})
        c += 1
    return out_dict


def print_numerated_dict(numdict):
    for k in numdict:
        print(f"{k}. {numdict[k]}")


def make_list(indict):
    d = indict
    out_list = []
    x = -1
    print(f"Список блюд:")
    while len(d) > 0 and x != 0:
        t = enumerate_menu(d)
        print_numerated_dict(t)
        x = int(input(f"Выберите блюдо {1}{f' - {len(d)}' if len(d) > 1 else f''}. Введите 0 для подсчета:\n"))
        if x in t.keys():
            print(f"Добавили: '{list(d.keys())[x - 1]}'.")
            out_list.append(list(d.keys())[x - 1])
            d.pop(list(d.keys())[int(x) - 1])
            if len(d) > 0:
                print(f'\nДобавить следующее блюдо?')
        elif x != 0:
            print("Неверный ввод!\n")
    return out_list


def menu():
    print("Создаем список покупок.\nВыберите блюда.")
    cook_book = file_to_dict('file.txt')
    inlist = make_list(file_to_dict('file.txt'))
    p = int(input("\nНа сколько персон готовить?\n"))
    h = get_shop_list_by_dishes(cook_book, inlist, p)
    print("\nСписок покупок:")
    c = 1
    for i in h:
        print(f'{c}. {i}: {h[i]["quantity"]} {h[i]["measure"]}')
        c += 1


menu()
