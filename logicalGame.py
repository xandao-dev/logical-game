#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: xandao6
"""

true = 'True'
false = 'False'
op_not = 'not'
op_and = 'and'
op_or = 'or'

booleans = [true, false]
logical_operators = [op_and, op_or]

expression = [true, op_or, false, op_and, true, op_and, true, op_or, true]


def main():
    print("\nSolve this:")
    print_list_formated(expression)
    user_answer = input("What's the answer (true/false)? ")
    print('\n')

    while len(expression) > 1:
        for i in range(len(expression)):
            if i < (len(expression) - 2):
                finded_or = verify_operator_OR(i)
                if finded_or == True:
                    print_list_formated(expression)
            if i < (len(expression) - 2):
                finded_and = verify_operator_AND(i)
                if finded_and == True:
                    print_list_formated(expression)
    print_game_result(user_answer)
                
    


def remove_3_in_sequence_from_list(my_list, first_index):
    my_list.pop(first_index)
    my_list.pop(first_index)
    my_list.pop(first_index)


def insert_1_in_list(my_list, index, value):
    my_list.insert(index, value)


def print_list_formated(my_list):
    print(' '.join(my_list))


def verify_operator_OR(position):
    # OPERADOR OR
    if expression[position] == true and expression[position+1] == op_or and expression[position+2] == true:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, true)
        return True
    elif expression[position] == false and expression[position+1] == op_or and expression[position+2] == false:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, false)
        return True
    elif expression[position] == true and expression[position+1] == op_or and expression[position+2] == false:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, true)
        return True
    elif expression[position] == false and expression[position+1] == op_or and expression[position+2] == true:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, true)
        return True
    else: 
        return False


def verify_operator_AND(position):
    # OPERADOR AND
    if expression[position] == true and expression[position+1] == op_and and expression[position+2] == true:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, true)
        return True
    elif expression[position] == false and expression[position+1] == op_and and expression[position+2] == false:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, false)
        return True
    elif expression[position] == true and expression[position+1] == op_and and expression[position+2] == false:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, false)
        return True
    elif expression[position] == false and expression[position+1] == op_and and expression[position+2] == true:
        remove_3_in_sequence_from_list(expression, position)
        insert_1_in_list(expression, position, false)
        return True
    else :
        return False


def print_game_result(user_answer):
    if (expression[0] == true and user_answer == 'true') or \
            (expression[0] == false and user_answer == 'false'):
        print("\nYou're right! Congratulations!!! \U0001F44F")
    else:
        print("\nYou're wrong! Maybe next time!!! \U0001F62B")


if __name__ == "__main__":
    main()
