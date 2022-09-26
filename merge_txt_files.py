# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files
import os


def get_txt_files_list():
    files_list = []
    for i in os.listdir():
        if i.count('.txt') > 0 and i != 'result.txt':
            files_list.append(i)
    return files_list


def create_dict(file_name_list=None):
    if file_name_list is None:
        file_name_list = ['1.txt', '2.txt', '3.txt']
    file_dict = {}
    for file in file_name_list:
        with open(file, mode='r', encoding='UTF-8') as f:
            file_dict.update({file: len(f.readlines())})
    return file_dict


def sort_dict(in_dict):
    sorted_dict = {}
    s_dict = sorted(in_dict.values())
    for j in range(len(in_dict)):
        for i in in_dict:
            if in_dict[i] == s_dict[j]:
                sorted_dict.update({i: in_dict[i]})
    return sorted_dict


def make_file(in_dict):
    with open('result.txt', mode='w', encoding='UTF-8') as new_file:
        for i in in_dict:
            with open(i, mode='r', encoding='UTF-8') as f:
                new_file.write(f'{i}\n{in_dict[i]}\n{f.read()}')
                if i != list(in_dict.keys())[-1::][0]:
                    new_file.write('\n')
    print(f'Файл result.txt создан из файлов: ', end='')
    print(*in_dict, sep=', ')


def main():
    k = input("Ищем все файлы в папке со скриптом (1) или используем 1.txt, 2.txt и 3.txt (2):\n")
    while k != '1' and k != '2':
        k = input("Ошибка. Введите 1 или 2:\n")
    if k == '1':
        make_file(sort_dict(create_dict(get_txt_files_list())))
    elif k == '2':
        make_file(sort_dict(create_dict()))


main()
