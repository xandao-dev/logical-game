#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = '1.1'
__author__ = 'Alexandre Calil Martins Fonseca'

import random

true = 'True'
false = 'False'
op_not = 'not'
op_and = 'and'
op_or = 'or'


def main():
    random.seed()
    level = int(input("Choose a level (integer number): "))
    expression = generate_expression(level)
    print("\nSolve:")
    print_list_formated(expression)
    user_answer = input("What's the answer (true/false)? ")
    print('\n')

    print_list_formated(expression)

    verify_operator_NOT_loop(expression)

    while len(expression) > 1:
        for i in range(len(expression)):
            if i < (len(expression) - 2):
                found_or = verify_operator_OR(i, expression)
                if found_or == True:
                    print_list_formated(expression)
            if i < (len(expression) - 2):
                found_and = verify_operator_AND(i, expression)
                if found_and == True:
                    print_list_formated(expression)
    print_game_result(user_answer, expression)


def generate_expression(level):
    if level % 2 == 0:
        level += 1

    expression = []
    booleans = [false, true]
    logical_operators = [[op_and, op_or], [op_not]]

    for i in range(level):  # Even Number
        if i % 2 == 0:
            expression.append(random.choice(booleans))
        else:
            expression.append(random.choice(logical_operators[0]))
            if random.choice(logical_operators[1]+[None]) != None:
                expression.append(logical_operators[1][0])
    return expression


def remove_from_list(my_list, first_index, quantity_to_remove):
    for _ in range(quantity_to_remove):
        my_list.pop(first_index)


def insert_in_list(my_list, index, value, quantity_to_insert):
    for _ in range(quantity_to_insert):
        my_list.insert(index, value)


def print_list_formated(my_list):
    print(' '.join(my_list))


def verify_operator_NOT_loop(expression):
    while True:
        for i in range(len(expression)):
            if i < (len(expression) - 1):
                found_not = verify_operator_NOT(i, expression)
                if found_not == True:
                    print_list_formated(expression)
        if not op_not in expression:
            break


def verify_operator_NOT(position, expression):
    if expression[position] == op_not and expression[position+1] == true:
        remove_from_list(expression, position, 2)
        insert_in_list(expression, position, false, 1)
        return True
    elif expression[position] == op_not and expression[position+1] == false:
        remove_from_list(expression, position, 2)
        insert_in_list(expression, position, true, 1)
        return True
    else:
        return False


def verify_operator_OR(position, expression):
    if expression[position] == true and expression[position+1] == op_or and expression[position+2] == true:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, true, 1)
        return True
    elif expression[position] == false and expression[position+1] == op_or and expression[position+2] == false:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, false, 1)
        return True
    elif expression[position] == true and expression[position+1] == op_or and expression[position+2] == false:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, true, 1)
        return True
    elif expression[position] == false and expression[position+1] == op_or and expression[position+2] == true:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, true, 1)
        return True
    else:
        return False


def verify_operator_AND(position, expression):
    if expression[position] == true and expression[position+1] == op_and and expression[position+2] == true:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, true, 1)
        return True
    elif expression[position] == false and expression[position+1] == op_and and expression[position+2] == false:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, false, 1)
        return True
    elif expression[position] == true and expression[position+1] == op_and and expression[position+2] == false:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, false, 1)
        return True
    elif expression[position] == false and expression[position+1] == op_and and expression[position+2] == true:
        remove_from_list(expression, position, 3)
        insert_in_list(expression, position, false, 1)
        return True
    else:
        return False


def print_game_result(user_answer, expression):
    if (expression[0] == true and user_answer == 'true') or \
            (expression[0] == false and user_answer == 'false'):
        print("\nYou're right! Congratulations!!! \U0001F44F")
    else:
        print("\nYou're wrong! Maybe next time!!! \U0001F62B")


if __name__ == "__main__":
    main()
