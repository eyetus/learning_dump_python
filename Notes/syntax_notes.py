######################
# Python Syntax Notes #
######################

# ========================================================================
# Functions
# ========================================================================

def say_hi(name, age):
    print("Hello " + name + "You are " + str(age))


say_hi("Mike", 35)
say_hi("Steve", 70)


# ------------------------------------------------------------------------

def cube(num):
    return num * num * num


print(cube(3))


# ------------------------------------------------------------------------

def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")
    print("Welcome")


greet_user("John", "Smith")
greet_user(first_name="Ivan", last_name="Tony")


# ------------------------------------------------------------------------

def square(number):
    return number * number


print(square(3))


# ------------------------------------------------------------------------

#args
def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))


#kwargs
def hello(**kwargs):
    print (f"Hello {kwargs['first']} {kwargs['last']}")

hello(first='Rich', middle='Dude', last='Edwards')

# Or

def hello(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')

hello(title='Mr', first='Rich', middle='Dude', last='Edwards')
print()
hello(colour='red', colour2='blue', colour3='green', colour4='yellow')

# Output
'''
Hello Mr Rich Dude Edwards 
Hello red blue green yellow
'''

# ------------------------------------------------------------------------

def func_emoji(message):
    words = message.split(" ")
    emoji_map = {
        ":)": "🙂",
        ":(": "😞",
        "xD": "😆",
        "rofl": "🤣"
    }
    output = ""
    for word in words:
        output += emoji_map.get(word, word) + " "
    return output


message = input("> ")
print(func_emoji(message))


# ------------------------------------------------------------------------

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))


# ------------------------------------------------------------------------

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# ========================================================================
# If Statements
# ========================================================================

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not all")

# ------------------------------------------------------------------------

name = input("Enter your name: ")

if len(name) < 3:
    print("Error: Name must be at least 3 characters")
elif len(name) > 10:
    print("Name must be a maximum of 10 characters")
else:
    print("Valid name")

# ------------------------------------------------------------------------

first = "Rich"
last = ""

if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

# ------------------------------------------------------------------------

weight = int(input("Weight: "))
unit = input("(L)lbs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")

# ------------------------------------------------------------------------

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

    
# 'if' - using expression instead of statement:

print(
    "Your name is as long or longer than the average first name in the United States"
) if len(name) >= 6 else print(
    "Your name is shorter than the average first name in the United States"
)


message = (
    "The first letter in your name is among the five most common"
    if name[0].lower() in ["a", "j", "m", "e", "l"]
    else "The first letter of your name is not among the five most common"
)


for letter in name:
    print(
        f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else 'is a consonant'}"
    )


# ========================================================================
# While Loop
# ========================================================================

name = ""
while len(name) == 0:
    name = input("Input your name: ")

print("Hello " +name)

name = None
while not name:
    name = input("Input your name: ")

print("Hello " + name)

# ------------------------------------------------------------------------

i = 1
while i <= 5:
    print(i)
    print('*' * i)
    i += 1
print("Done")

# ------------------------------------------------------------------------

while True:
    name = input('Enter you name: ')
    if name != '':
        break

# ------------------------------------------------------------------------

count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1

# ------------------------------------------------------------------------

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess number: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Sorry you failed!")

# ------------------------------------------------------------------------

secret_letter = "X"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input("Guess the letter: ")
    guess_count += 1
    if guess.upper() == secret_letter:
        print("You win!")
        break
else:
    print("You failed!")

# ------------------------------------------------------------------------

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses!")
else:
    print("You win!")

# ------------------------------------------------------------------------

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped....")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print('Goodbye!')
        break
    else:
        print("Sorry I don't understand that!")


# ========================================================================
# For Loop
# ========================================================================

for item in 'Python':
    print(item)

# ------------------------------------------------------------------------

for list in ['Rich', 'Georgie', 'Liam']:
    print(list)

# ------------------------------------------------------------------------

for number in [1, 2, 3, 4, 5]:
    print(number)

# ------------------------------------------------------------------------

for numbers in range(10):
    print(numbers)

# ------------------------------------------------------------------------

import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")

# ------------------------------------------------------------------------

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# ------------------------------------------------------------------------

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# ------------------------------------------------------------------------

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# ------------------------------------------------------------------------

numbers = [8, 8, 7, 8, 9, 9, 5, 4, 4, 1, 1, 2, 3, 3, 10]
final = []
for item in numbers:
    if item not in final:
        final.append(item)
final.sort()
print(final)

# ------------------------------------------------------------------------

digitmap = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone: ")
output = ""

for number in phone:
    output += digitmap.get(number, '!') + " "
print(output)

# ------------------------------------------------------------------------

message = input("> ")
words = message.split(" ")
emoji_map = {
    ":)": "🙂",
    ":(": "😞",
    "xD": "😆",
    "rofl": "🤣"
}
output = ""
for word in words:
    output += emoji_map.get(word, word) + " "
print(output)


# ========================================================================
# Nested For Loop
# ========================================================================

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

# ------------------------------------------------------------------------

rows = int(input("How many rows?: "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# ------------------------------------------------------------------------

phone_number = '123-456-789'

for i in phone_number:
    if i == '-':
        continue
    print(i, end='')

# ------------------------------------------------------------------------

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)


# ========================================================================
# Lists
# ========================================================================

names = ['Rich', 'Georgina', 'Liam']

names.append('Steven')
names.remove('Steven')
names.pop()
names.insert(0, 'Mum')
names.sort()
names.clear()


# ========================================================================
# 2D Lists
# ========================================================================

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [0]
]

print(number_grid[0][0])

# ------------------------------------------------------------------------

drinks = ['coffee', 'soda', 'tea']
dinner = ['pizza', 'hamburger', 'hotdog']
dessert = ['cake', 'ice cream']

food = [drinks, dinner, dessert]

print(food[0])
print(food[0][2])


# ========================================================================
# Tuples
# ========================================================================

student = ('John', 21, 'Male')

student.count('John')
student.index('Male')


# ========================================================================
# Set
# ========================================================================

dictionary = {'Rich', 'Georgina', 'Liam', 'Dog'}
dictionary2 = {'Dad', 'Mum', 'Son', 'Dog'}
main_dict = dictionary.union(dictionary2)

dictionary.add('Steven')
dictionary.remove('Steven')
dictionary.clear()
dictionary.update(dictionary2)

print(dictionary.difference(dictionary2)) # shows what is missing
print(dictionary.intersection(dictionary2)) # shows what they both have


# ========================================================================
# Dictionary
# ========================================================================

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

monthConversions.update({"Month_Initials": "Month"})
monthConversions.pop("Month_Initials")
monthConversions.clear()

print(monthConversions["Jan"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Hello", "'Hello' not in dictionary!"))
print(monthConversions.keys())
print(monthConversions.values())
print(monthConversions.items())

for key, value in monthConversions.items():
    print(key, value)


# ------------------------------------------------------------------------

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
}

print(customer.get("age"))
print(customer.get("email", "Default response"))  # will return ‘None’ if key doesn’t exist
print(customer["name"])
customer["birthdate"] = "1st Jan 1980"

# ------------------------------------------------------------------------

list_of_points = [(1, 2), (2, 3), (4, 5)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

# ------------------------------------------------------------------------

ages = {
    'kevin': 59,
    'bob': 40,
    "kayla": 21
}

for name, age in ages.items():
    print(f"Person named: {name}")
    print(f"Age of: {age}")

# ------------------------------------------------------------------------

digitmap = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone: ")
output = ""

for number in phone:
    output += digitmap.get(number, "!") + " "
print(output)

# ------------------------------------------------------------------------

message = input("> ")
words = message.split(" ")
emoji_map = {
    ":)": "🙂",
    ":(": "😞",
    "xD": "😆",
    "rofl": "🤣"
}
output = ""
for word in words:
    output += emoji_map.get(word, word) + " "
print(output)


# ========================================================================
# Exceptions
# ========================================================================

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Can't device by Zero!")
    print('Error: ', e)
except ValueError as e:
    print('Enter only numbers!')
    print('Error: ', e)
except Exception as e:
    print('Something went wrong!')
    print('Error: ', e)
else:
    print(result)
finally:
    print('Done!')


# ========================================================================
# Classes
# ========================================================================

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# ------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)


# ------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


p1 = Person("John", 36)
p1.myfunc()


# ------------------------------------------------------------------------

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probabtion = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


student1 = Student("Jim", "Business", 3.5, False)
student2 = Student("Pam", "Art", 2.5, True)
print(f"Student name: {student1.name}")
print(f"On honor roll?: {student1.on_honor_roll()}")
print(student2.major)
print(student2.on_honor_roll())


# ========================================================================
# Inheritance
# ========================================================================

# Inheritance (using Person parent class to create Student inheriting properties/methods from parent)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass  # do not add any other properties/methods to inhereted class)


x = Student("Mike", "Olsen")
x.printname()


# ------------------------------------------------------------------------

class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()

# ========================================================================
# Interacting with files
# ========================================================================

# Reading files
test_file = open('test_file.txt', 'r')
test_file.read()
test_file.seek(0)
test_file.read()

for line in test_file:
    print(line, end="")

test_file.close()

# ------------------------------------------------------------------------

employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee, end="")
employee_file.close()

# ------------------------------------------------------------------------

# Writing to files

# Open new file for reading & writing ('w' = truncates file first, '+' = r/w
old_file = open('old_file.txt', 'r')
new_file = open('new_file.txt', 'r+')

# Read from another file and add to new file (then close)
new_file.write(old_file.read())
new_file.close()
old_file.close()

# Append to end of txt file 'a' (with = auto close file)
with open('file.txt', 'a') as f:
    f.write("Something")

# or
f = open("file.txt", 'a')
with f:
    f.write("Something")

# ------------------------------------------------------------------------

employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")
employee_file.close()

employee_file1 = open("employees1.txt", "w")

employee_file.write("\nStart of new file")
employee_file.close()

# ========================================================================
# Parsing command-line parameters
# ========================================================================

import argparse

# Build the parser using argparse class/functions
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v')
action = version, version = '%(prog)s 1.0'

# Parse agrs to variable 'args'
args = parser.parse_args()

# Opens filename.txt, reads and reverses lines & strings (if --limit arg provided also)
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])

# Same but using try/except:
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
finally:
    print('FIN!')

# List comprehension (searching for word/snippet in words file)

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words file')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)

# or using comprehension to iterate list
print([word.strip() for word in words if snippet in word.lower()])


##########################################################################
# Example Programs
##########################################################################

# BMI Calculator, using functions for user input and calculations with if statements. Executed with while loop calling functions

def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    unit = input("Are your mearsurements in metric or imperial units? ").lower().strip()
    return (height, weight, unit)


def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print(f"Your BMI is {bmi}")


while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight, unit='imperial', height=height)
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")

# ------------------------------------------------------------------------

# Stopwatch using 'time' package

# Importing 'time' module:

import time

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

# wait for user to stop timer
input("Press 'Enter' to stop timer")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")

# importing only the required functions from 'time' package:

from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# wait for user to stop timer
input("Press 'Enter' to stop timer")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")

# ------------------------------------------------------------------------

# Receipts file generation and processing using 'random', 'json', 'os' & 'shutil'

# Creating files with random key/values in JSON format using random.functions

import random
import json
import os

count = int(os.getev("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)

# Create new directory with 'os'
# get filenames with glob and add to 'receipts'
# Iterate through 'receipts' adding 'content' dict values to subtotal
# using shutil to move files to new directory and print total

import random
import json
import os
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")


# ------------------------------------------------------------------------

# Multiple choice quiz

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print(f"You got {str(score)}/{str(len(questions))} correct")


question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

run_test(questions)
