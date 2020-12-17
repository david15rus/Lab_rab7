#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys

# Условние задания
# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название товара? ")
            shop = input("Название магазина? ")
            coast = int(input("Введите его цену "))

            product = {
                'name': name,
                'shop': shop,
                'coast': coast,
            }

            products.append(product)
            if len(product) > 1:
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                ' | {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Наименование товара",
                    "Название магазина",
                    "Стоимость"
                )
            )
            print(line)

            for idx, product in enumerate(products, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        product.get('name', ''),
                        product.get('shop', ''),
                        product.get('coast', 0)
                    )
                )

            print(line)

        elif command.startswith('select'):
            name_user = input("Введите название интересующего магазина ")

            count = 0
            for product in products:
                if name_user == product.get('shop'):
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(count, product.get('coast', ' '), product.get('name', ' '))
                    )
            if count == 0:
                print("Магазин с таким названием не найден")

        elif command.startswith('load'):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                tree = ET.parse(f)
                root = tree.getroot()

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                doc = ET.Element(f)
                tree = ET.ElementTree(doc)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товары;")
            print("list - вывести список товаров;")
            print("select <магазин> - запросить товары в выбранном магазине")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
