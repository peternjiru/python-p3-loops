#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count != 0:
        if count == 1:
            print(count)
            print("Happy New Year!")
        else:
            print(count)
        count = count - 1


def square_integers(int_list):
    squared_ints = [num * num for num in int_list]
    return squared_ints


def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num = num + 1
    
fizzbuzz()
