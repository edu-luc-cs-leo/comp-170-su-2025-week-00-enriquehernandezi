#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is an invalid name in python, because it starts with a number and it must always begin with a letter.
3. age, is a valid name in python as it counts as a descriptive name that meets all requirements.
4. total_amount, is a valid name in python, because it is snake case using the _ instead of spaces.
5. while, is an invalid name in python, because it is a reserved word.
6. Student, is a valid name in python as it counts as a descriptive name that meets all requirements and is allowed to start with a uppercase.
7. my-variable, is an invalid name in python, because it contains a special character that isn't an underscore.
8. for, is an invalid name in python, because it is a reserved word.
9. _temp, is an valid name in python, because it starts with an underscore.
10. value#, is an invalid name in python, because it contains a special character.
Your solution goes here


"""
# Problem 2
"""
1. calculate_total, is a valid name in python, because it is snake case.
2. 3rd_function, is an invalid name in python, becuase it starts with a number instead of a letter.
3. print_values, is a valid name in python, because it is a snake case.
4. find-item, is an invalid name in python, because it contains special characters.
5. def, is an invalid name in python, because it is a reserved string.
6. updateProfile, is a valid name in python, as it is not spaced and can contain upper and lowercase letters.
7. my_function, is a valid name in python, because it is a snake case.
8. try, is a valid name in python, as it completes all requirements and does not violate the rules (might be invalid since it sounds like a reserved word).
9. init_data, is a valid name in python, because it is a snake case.
10. value@function, is an invalid name in python, because it contains special characters.
Your solution goes here


"""
# Problem 3
"""
1. True and False, is an valid and would return to False since its comapring True and False.
2. 5 > 3 or "apple" < "banana", is valid, and would produce 'True' since 5 is bigger than 3 and 'apple' comes before 'banana' alphabetically.
3. not 10 <= 20, is valid, and would produce 'False' since 20 is not bigger or equal to not 10.
4. True or 5 = 4, is invalid, because it should have a ==.
5. "apple" != "orange" and 5, is valid and would produce 5 since True is True and apple is not equal to orange.
6. 3 < 5 not True, is invalid, you need a 'and' before 'not'.
7. False == (3 > 4), is valid and would return True since False is equal to a false statement (3>4).
8. 10 <= "10", is not valid because 10 is treated as an integer and "10" is treated as a string.
9. True or not False, is valid and would return True.
10. 5 and or 4, is invalid because there is supposed to be something after and.




Your solution goes here


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
