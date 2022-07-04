# Question 1 
# user_name = input("What is your name? ")
# def hello_name(user_name):
#     print(f"Nice to meet you, {user_name}.")
# hello_name(user_name)

# Question 2 
# def first_odds():
#     for number in range(1, 101):
#         if number % 2 == 1:
#             print(number)
#     return
# first_odds()

# Question 3 
# a_list = [3, 1, 9, 5]
# def max_num_in_list(a_list):
#     max_number = 0
#     for number in a_list:
#         if max_number < number:
#             max_number = number
#     print(max_number)
# max_num_in_list(a_list)

# Question 4 
# a_year = 400
# def is_leap_year(a_year):
#     if a_year % 4 == 0:
#         if a_year % 100 == 0: 
#             if a_year % 400 == 0:
#                 return True
#             else: 
#                 return False
#         return True
#     else:
#         return False
# print(is_leap_year(a_year))

# Question 5 
# a_list = [1, 2, 3, 4, 8]
# def is_consecutive(a_list):
#     consecutive = a_list[0]
#     for number in a_list:
#         if consecutive == number:
#             consecutive += 1
#         else: 
#             return False
#     return True
# print(is_consecutive(a_list))