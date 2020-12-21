#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Написать программу, которая считывает английский текст из файла и выводит его на экран,
# заменив каждую первую букву слов, начинающихся с гласной буквы, на прописную.

if __name__ == '__main__':
    with open('eng.txt', 'r') as f:
        eng = f.read()
    sentences = eng.split(" ")
    A = ["A", "E", "I", "O", "U", "Y"]
    eng_1 = ' '
    for sentence in sentences:

        if sentence[0] == "A":
            sentence = sentence.replace('A', 'a')

        if sentence[0] == "E":
            sentence = sentence.replace('E', 'e')

        if sentence[0] == "I":
            sentence = sentence.replace('I', 'i')

        if sentence[0] == "O":
            sentence = sentence.replace('O', 'o')

        if sentence[0] == "U":
            sentence = sentence.replace('U', 'u')

        if sentence[0] == "Y":
            sentence = sentence.replace('Y', 'y')

        print(sentence)
