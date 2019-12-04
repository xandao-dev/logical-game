#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: xandao6
"""

def remove_3_in_sequence_from_list(my_list, first_index):
    my_list.pop(first_index)
    my_list.pop(first_index)
    my_list.pop(first_index)

def insert_1_in_list(my_list, index, value):
    my_list.insert(index, value)

def print_list_formated(my_list):
    print(' '.join(my_list))

true = 'True'
false = 'False'
op_not = 'not'
op_and = 'and'
op_or = 'or'

booleans = [true, false]
logical_operators = [op_and, op_or]

exp = [true, op_or, false, op_and, true, op_and, true, op_or, true]

print("\nSolve this:")
print_list_formated(exp)
user_answer = input("What's the answer (true/false)? ")
print('\n')

while len(exp) > 1:
    for i in range(len(exp)):
        if i < (len(exp) - 2):
            #OPERADOR OR
            if exp[i] == true and exp[i+1] == op_or and exp[i+2] == true:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, true)
                print_list_formated(exp)
            elif exp[i] == false and exp[i+1] == op_or and exp[i+2] == false:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, false)
                print_list_formated(exp)
            elif exp[i] == true and exp[i+1] == op_or and exp[i+2] == false:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, true)
                print_list_formated(exp)
            elif exp[i] == false and exp[i+1] == op_or and exp[i+2] == true:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, true)
                print_list_formated(exp)
                
            #OPERADOR AND
            elif exp[i] == true and exp[i+1] == op_and and exp[i+2] == true:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, true)
                print_list_formated(exp)
            elif exp[i] == false and exp[i+1] == op_and and exp[i+2] == false:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, false)
                print_list_formated(exp)
            elif exp[i] == true and exp[i+1] == op_and and exp[i+2] == false:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, false)
                print_list_formated(exp)
            elif exp[i] == false and exp[i+1] == op_and and exp[i+2] == true:
                remove_3_in_sequence_from_list(exp, i)
                insert_1_in_list(exp, i, false)
                print_list_formated(exp)
if (exp[0] == true and user_answer == 'true') or \
   (exp[0] == false and user_answer == 'false'):
    print("\nYou're right! Congratulations!!! \U0001F44F")
else:
    print("\nYou're wrong! Maybe next time!!! \U0001F62B")
