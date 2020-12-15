#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Написать программу, которая считывает английский текст из файла и выводит его на экран,
# заменив каждую первую букву слов, начинающихся с гласной буквы, на прописную.

if __name__ == '__main__':
    with open('eng.txt', 'r') as f:
        eng = f.read()

        eng = eng.replace('A', 'a')
        eng = eng.replace('E', 'e')
        eng = eng.replace('I', 'i')
        eng = eng.replace('O', 'o')
        eng = eng.replace('U', 'u')
        eng = eng.replace('Y', 'y')
    print(eng)