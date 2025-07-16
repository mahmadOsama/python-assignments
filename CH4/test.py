

# ==============================================================================
# EX 1 - Data Structures
# ==============================================================================

# ------------------------------------------------------------------------------
# Strings
# ------------------------------------------------------------------------------

# 1. Write a function to count the number of vowels in a given string.

def count_vowel(text):
    vowels_str = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels_str:
            count += 1
    return count


user_text = input("Please enter your text: ")
result = count_vowel(user_text)
print("The number of vowels in your text:", result)

# ------------------------------------------------------------------------------

# 2. Write a function that takes a string and returns the same string but with every second letter capitalized.

def make_capsec(text):
    result = ""
    for index, char in enumerate(text):
        if index % 2 == 1:
            result += char.upper()
        else:
            result += char
    return result


user_input = input("Please enter your string: ")
result = make_capsec(user_input)
print("Result:", result)

# ------------------------------------------------------------------------------
# List
# ------------------------------------------------------------------------------

# 3. Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def list_even(x):
    even = []
    for n in x:
        if not n % 2:
            even.append(n)
    return even


numbers = [2, 3, 4, 4, 7, 8, 101, 103, 111, 120, 124]
print(list_even(numbers))

# ------------------------------------------------------------------------------

# 4. Write a function that takes a list and returns a new list with duplicate values removed.

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


numbers = [1, 2, 2, 3, 4, 4, 9, 5, 9, 9, 9, 9, 5]
print(remove_duplicates(numbers))

# ------------------------------------------------------------------------------
# Set
# ------------------------------------------------------------------------------

# 5. Write a function that takes two sets and returns their intersection as a new set.

def set_intersection(set1, set2):
    return set1 & set2


set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
result = set_intersection(set_a, set_b)
print(result)

# ------------------------------------------------------------------------------

# 6. Write a function that takes two sets and returns their union as a new set.

def set_union(set1, set2):
    return set1 | set2


set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
result = set_union(set_a, set_b)
print(result)

# ------------------------------------------------------------------------------
# Tuple
# ------------------------------------------------------------------------------

# 7. Write a function that takes a list of tuples and sorts them based on the second element of each tuple.

def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])


tuples = [('apple', 3), ('banana', 1), ('cherry', 5), ('date', 2)]
result = sort_by_second_element(tuples)
print(result)

# ------------------------------------------------------------------------------

# 8. Write a function that takes a tuple and returns a reversed version of that tuple.

def reverse_tuple(tup):
    return tup[::-1]


original = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(original)
print(reversed_tuple)

# ------------------------------------------------------------------------------
# Dictionary
# ------------------------------------------------------------------------------

# 9. Write a function that takes a dictionary and returns the keys and values as separate lists.

def get_keys_values(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys, values


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys, values = get_keys_values(my_dict)
print("Keys:", keys)
print("Values:", values)

# ------------------------------------------------------------------------------

# 10. Write a function that takes a dictionary and a key, and if the key exists in the dictionary, return its value. If the key does not exist, return a default value.

def get_value_or_default(dictionary, key, default_value=None):
    return dictionary.get(key, default_value)


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(get_value_or_default(my_dict, 'a'))
print(get_value_or_default(my_dict, 'x'))
print(get_value_or_default(my_dict, 'x', 'N/A'))

# ==============================================================================
# EX 2 - Conditional Statements, Loops, and Functions
# ==============================================================================

# Task 1: Write a program that takes two numbers as inputs from the user and prints their sum.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")

# ------------------------------------------------------------------------------

# Task 2: Write a program that takes an integer input from the user. Use a `for` loop to print all numbers from that integer down to 0.

num = int(input("Enter an integer: "))

for i in range(num, -1, -1):
    print(i)

# ------------------------------------------------------------------------------

# Task 3: Write a program that takes an integer input from the user. Use a `while` loop to keep doubling the number until it is greater than 1000, then print the result.

num = int(input("Enter an integer: "))

while num <= 1000:
    num = num * 2

print(f"The result is: {num}")

# ------------------------------------------------------------------------------

# Task 4: Write a function that returns the square of a number

def square(number):
    return number ** 2


num = float(input("Enter a number: "))
result = square(num)
print(f"The square of {num} is: {result}")

# ------------------------------------------------------------------------------

# Task 5: Write a program that takes a number as input from the user. If the number is greater than 10, print "Big number". If the number is less than or equal to 10, print "Small number".

num = float(input("Enter a number: "))

if num > 10:
    print("Big number")
else:
    print("Small number")

# ------------------------------------------------------------------------------

# Task 6: Write a function that takes two numbers as inputs and returns their product. Use this function in a program that takes two inputs from the user and prints the product.

def multiply(num1, num2):
    return num1 * num2


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

product = multiply(number1, number2)
print(f"The product of {number1} and {number2} is: {product}")

# ------------------------------------------------------------------------------

# Task 7: Write a program that uses a `while` loop to take a number as input from the user, subtract 5, and print the result. Continue this until the result is less than 0.

num = float(input("Enter a number: "))

while num >= 0:
    num = num - 5
    print(num)

# ------------------------------------------------------------------------------

# Task 8: Write a program that uses a `for` loop to take an integer input from the user and print the factorial of that number.

num = int(input("Enter an integer: "))

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of {num} is: {factorial}")

# ------------------------------------------------------------------------------

# Task 9: Write a program that takes a number as input from the user. If the number is positive, print "Positive". If the number is negative, print "Negative". If the number is zero, print "Zero".

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# ------------------------------------------------------------------------------

# Task 10: Write a lambda function that takes two numbers as inputs and returns their division as a floating-point number. Use this function in a program that takes two inputs from the user and prints the division.

divide = lambda x, y: x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = divide(num1, num2)
print(f"The division of {num1} by {num2} is: {result}")

# ==============================================================================

# ==============================================================================