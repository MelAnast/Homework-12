# print("Hello, World")

# x = 5
# y = 3.14
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# name = "Johny"
# message = "Hello"
# print(name)
# print(message)
# print(type(name))

# this_Is_String = "This is string"
# print(this_Is_String)
# print(type(this_Is_String))
# this_Is_String = "This is not string"
# print(this_Is_String)
# print(type(this_Is_String))

# change class two examples
# a_number = 99
# print(a_number)
# print(type(a_number))
# change_num_to_str = str (a_number)
# print(change_num_to_str)
# print(type(change_num_to_str))
# float_numb = 3.1
# print(float_numb)
# print(type(float_numb))
# int_num = int (float_numb)
# print(int_num)
# print(type(int_num))

# lists
# numbers = [1, 3, 5, 7, 8]
# names = ["Ali", "Bal", "Cal", "Dal"]
# mixed_list = [1, "Nan", 2.2]
# print(numbers)
# print(names)
# print(mixed_list)
# print(len(numbers))
# print(len(names))
# print(len(mixed_list))
# print(numbers[0])
# print(names[3])
# print(names[2])
# adding values in lists
# numbers.append(6)
# print(numbers)

# tuples - kind of lists, can't add values after creation

# set - include only unique values
# numbers = {1, 2, 3, 4, 5, 7}
# print(numbers)
# list_with_random_numb = [1, 2, 3, 1, 3, 2, 1, 3, 2, 5, 3, 2, 1]
# set_from_list = set(list_with_random_numb)
# print(list_with_random_numb)
# print(set_from_list)

# dictionary - key for variables
# person = {"name": "Lohn", "age": 35, "gend": "male"}
# print(person["name"])
# animal = {"name": "Pony", "age": 3, "gend": "female"}
# print(animal["gend"])

# boolians begin from "is"
# is_true = True
# is_false = False
# print(is_true)
# print(is_false)

# none
# list_with_none = [1, 2, 3, None]
# print(list_with_none)
# print(list_with_none[3])

# arifmetika
# x = 6
# y = 2
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)
# print("x"+"y")
# sum_1 = 1+2
# print(sum_1)
# sum_2 = "1"+"2"
# print(sum_2)
# sum_3 = "Nas" + "tya"
# print(sum_3)

# and, or, not
# x = True
# y = False
# res_1 = x and y False
# res_2 = x or y True
# res_3 = not x False

# value = input("Enter smth: ")
# print(value)
# print(type(value))
#
# if int (value) >100:
#     print("Yes")
# if int (value) >100:
#     print("Yes")
# else:
#     print("No")

# if value.isdigit():
#     if int(value) > 100:
#         print("Yes")
#     else:
#         print("No")
# else:
#     print("Not a number")

# if value.isdigit():
#     if int(value) > 100:
#         print("Yes")
#     elif int(value) == 100:
#         print("No")
#     elif int(value) < 100:
#         print("Maybe")
# else:
#     print("Not a number")

# f-string
# user_name = input("Enter your name: ")
# if user_name == "John":
#     print("Hello, John!")
# elif user_name == "Jack":
#     print("Hello, Jack!")
# else:
#     print(f"Hello, {user_name}!")
#
# is_logged_in = True
# if is_logged_in:
#     print("Logged in")
# else:
#     print("Not logged in")

# cycles
init_value = 1
while init_value <=10:
    print(init_value)
    init_value = init_value + 2
#     the same is init_value +=1
print("the end")
