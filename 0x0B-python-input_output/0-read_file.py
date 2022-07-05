#!/usr/bin/python3

''' Write a function that reads a text file (UTF8) and prints it to stdout '''


def read_file(filename=""):
    ''' Define a text reading function '''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
