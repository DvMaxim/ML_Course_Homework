# Файл с выполнением заданий первой домашней работы

import random

print("\nTask_1", "\n--------------------")

nums = (1, 2, 3, 4)
print("Second num: ", nums[1])

print("\nTask_2", "\n--------------------")

user_str = input("Input str: ")
print("String length: ", len(user_str))

print("\nTask_3", "\n--------------------")

student = {"name": "Maks",
           "age": 22,
           "course": "ML"}
for key in student.keys():
    print(f"{key}: {student[key]}")

print("\nTask_4", "\n--------------------")

nums_list = list(range(1, 11))
print(nums_list)

print("\nTask_5", "\n--------------------")


def sum_list(nums):
    return sum(nums)


print("Сумма списка из четвертого задания: ", sum_list(nums_list))

print("\nTask_6", "\n--------------------")

nums_set = {random.randint(1, 100) for _ in range(5)}
print("Original set: ", nums_set)
nums_set.add(random.randint(1, 100))
print("Updated set: ", nums_set)

print("\nTask_7", "\n--------------------")

while True:
    try:
        user_num = int(input("Input number: "))
        break
    except ValueError as e:
        print("ValueError: ", e)
        print()
    except Exception as e:
        print("Exception: ", e)
        print()

print("The square of the input number: ", pow(user_num, 2))

print("\nTask_8", "\n--------------------")

fruits = {"apple": "red",
          "orange": "orange",
          "banana": "yellow",
          "plum": "purple",
          "pear": "green"}

print(fruits.values())

print("\nTask_9", "\n--------------------")


def reverse_str(user_str):
    return user_str[::-1]


input_str = input("Input string: ")
print("Your string in reverse: ", reverse_str(input_str))

print("\nTask_10", "\n--------------------")

str_list = ["str_1", "str_2", "str_3", "str_4", "str_5"]
print("List before updates: ", str_list)
str_list.pop(2)
new_str = "Hello World"
str_list.insert(2, new_str)
print("List after updates: ", str_list)

print("\nTask_11", "\n--------------------")

diff_types_tuple = (1, {"apple": "red"}, True, [1, 2, 4], 2.67, {1, 2, 4})
for el in diff_types_tuple:
    print(f'Element "{el}": ', type(el))

print("\nTask_12", "\n--------------------")


def multiply_numbers(num_1, num_2):
    return num_1 * num_2


while True:
    try:
        num_1 = int(input("Input first number: "))
        num_2 = int(input("Input second number: "))
        break
    except ValueError as e:
        print("ValueError: ", e)
        print()
    except Exception as e:
        print("Exception: ", e)
        print()

print("The result of multiplication: ", multiply_numbers(num_1, num_2))

print("\nTask_13", "\n--------------------")

book = {"author": "Джордж Оруэлл",
        "name": "1984",
        "publication_date": 1949}

for key in book.keys():
    print(f"{key}: {book[key]}")

print("\nTask_14", "\n--------------------")

towns = {"Minsk", "Moscow", "Grodno", "Brest", "Mogilev"}
print("Set before deleting: ", towns)
while True:
    try:
        deleted_town = input("Input town for delete: ")
        towns.remove(deleted_town)
        print("Set after deleting: ", towns)
        break
    except ValueError as e:
        print("KeyError: ", e)
        print("Please, input correct town name!")
    except Exception as e:
        print("Exception: ", e)
        print()

print("\nTask_15", "\n--------------------")


def find_max_element(user_list):
    return max(user_list)


print("List for test function: ", nums_list)
print("Max element: ", find_max_element(nums_list))

print("\nTask_16", "\n--------------------")

task_16_list = range(1, 21)
print("Our list: ", task_16_list)
even_elements = [el for el in task_16_list if el % 2 == 0]
print("Even elements: ", even_elements)

print("\nTask_17", "\n--------------------")

task_17_str = input("Input str: ").lower()
if task_17_str == reverse_str(task_17_str):
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome!")

print("\nTask_18", "\n--------------------")

task_18_tuple = ("my string", 23, True)
unpacked_str, unpacked_num, unpacked_boolean = task_18_tuple
print("Full tuple: ", task_18_tuple)
print(f"First tuple element: {unpacked_str}.\n"
      f"Second tuple element: {unpacked_num}.\n"
      f"Third tuple element: {unpacked_boolean}.")

print("\nTask_19", "\n--------------------")


def view_student_info(student):
    for key in student.keys():
        print(f"{key}: {student[key]}")


new_student = {"name": "Maksim",
               "age": 22,
               "course": "Math"}

view_student_info(new_student)

print("\nTask_20", "\n--------------------")

task_20_list = [random.randint(1, 100) for _ in range(5)]
print("Full generated list: ", task_20_list)
i = 0
while i < len(task_20_list):
    print(f"{i + 1}-element: ", task_20_list[i])
    i += 1
