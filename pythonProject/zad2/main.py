# -*- coding: utf-8 -*-
# !/usr/bin/env  python3

import sys
from package import table, table_name, table_nam

if __name__ == '__main__':
    spisok = []
    new_spisok = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break


        elif command == 'add':
            surname = input("Фамилия: ")
            name = input("Имя: ")
            post = input("знак Зодиака: ")
            day, month, year = input("Дата рождения: ").split(" ")
            datas = f'{year} {month} {day}'
            spisok_new = {
                'surname': surname,
                'name': name,
                'post': post,
                'data': datas,
            }
            spisok.append(spisok_new)

            if len(spisok) > 1:
                spisok.sort(key=lambda item: item.get('data', ''))


        elif command == 'list':
            print(table())
            print(table_name())
            print(table())

            for item_x in table_nam(spisok):
                print(item_x)
            print(table())


        elif command == 'find':
            find = input("Введите знак Зодиака: ")

            for find_item in spisok:
                if find == find_item['post']:
                    new_spisok.append(find_item)

            if len(new_spisok) > 0:
                print(table())
                print(table_name())
                print(table())

                for item_qe in table_nam(new_spisok):
                    print(item_qe)
                print(table())

            else:
                print('Таких пользователей не найдено', file=sys.stderr)


        elif command == 'help':
            print('Список команд:\n')
            print('add - добавить пользователя.')
            print('list - вывести список пользователей.')
            print('find <Знак зодиака> - запросить пользователей по знаку Зодиака.')
            print('help - Справочник.')
            print('exit - Завершить пработу программы.')


        else:
            print(f'Команда <{command}> не существует.', file=sys.stderr)
            print('Введите <help> для просмотра доступных команд')
