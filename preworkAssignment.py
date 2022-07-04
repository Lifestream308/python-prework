# Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
user_name = input("What is your name? ")
def hello_name(user_name):
    print(f"Nice to meet you, {user_name}.")
hello_name(user_name)

# Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for number in range(1, 101):
        if number % 2 == 1:
            print(number)
    return
first_odds()

# Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. 
a_list = [3, 1, 9, 5]
def max_num_in_list(a_list):
    max_number = 0
    for number in a_list:
        if max_number < number:
            max_number = number
    print(max_number)
max_num_in_list(a_list)

# Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
a_year = 400
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0: 
            if a_year % 400 == 0:
                return True
            else: 
                return False
        return True
    else:
        return False
print(is_leap_year(a_year))

# Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
b_list = [1, 2, 3, 4, 8]
def is_consecutive(b_list):
    consecutive = b_list[0]
    for number in b_list:
        if consecutive == number:
            consecutive += 1
        else: 
            return False
    return True
print(is_consecutive(b_list))