# Задание: https://github.com/netology-code/py-homeworks-basic/tree/master/7.files
#
# Николай, спасибо за желание научить, а не просто зачитать лекцию!
import os


def get_txt_files_list():
    files_list = []
    for file_name in os.listdir():
        if file_name.count('.txt') > 0 and file_name != 'result.txt':
            files_list.append(file_name)
    return files_list


def create_dict(file_name_list=None):
    if file_name_list is None:
        file_name_list = ['1.txt', '2.txt', '3.txt']
    file_dict = {}
    for file in file_name_list:
        try:
            with open(file, mode='r', encoding='UTF-8') as opened_file:
                file_dict.update({file: len(opened_file.readlines())})
        except FileNotFoundError:
            print(f'Ошибка открытия файла: {file}! Файл не найден!')
    return file_dict


def sort_dict(in_dict):
    sorted_dict = {}
    sorted_dict_list = sorted(in_dict.values())
    for counter in range(len(in_dict)):
        for file_name in in_dict:
            if in_dict[file_name] == sorted_dict_list[counter]:
                sorted_dict.update({file_name: in_dict[file_name]})
    return sorted_dict


def make_file(in_dict):
    with open('result.txt', mode='w', encoding='UTF-8') as new_file:
        for file_name in in_dict:
            with open(file_name, mode='r', encoding='UTF-8') as f:
                new_file.write(f'{file_name}\n{in_dict[file_name]}\n{f.read()}')
                if file_name != list(in_dict.keys())[-1::][0]:
                    new_file.write('\n')
    print(f'Файл result.txt создан из файлов: ', end='')
    print(*in_dict, sep=", ")


def main():
    read_input = input("Ищем все файлы в папке со скриптом (1) или используем 1.txt, 2.txt и 3.txt (2):\n")
    while read_input != '1' and read_input != '2':
        read_input = input("Ошибка. Введите 1 или 2:\n")
    if read_input == '1':
        make_file(sort_dict(create_dict(get_txt_files_list())))
    elif read_input == '2':
        make_file(sort_dict(create_dict()))


main()
