#!/usr/bin/python3
def print_lastdigit(number):
    number = abs(number) % 10
    print(number, end="")
    return number
