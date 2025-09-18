# variables (strings - integer - float - bollean)

# Typecasting str(), int(), float(), bool() , type()

# input() "prompts the user to enter data"

# Arithmetic & math : 
#round(3.15) output => 3
#abs(-3) output => 3
#pow(3, 2) output => 9 
#max(3, 5) output => 5
#min(3, 5) output => 3
#import math, math is a class
#math.sqrt(9) output => 3
#math.ceil(2.1) output => 3
#math.floor(2.1) output => 2
#round(3.22222, 2) output => 3.22  || 3.22222:.2f(in fString)

# if statement (if elif else) ("Attention to the order")

# dictionaries print(dict-name.get(key) => print the key value
#dict-name.update() => add a key and its value or update the value of an existen key  == dict-name["key-name"] = "value"
#dict-name.pop(key) => it removes the key and its value  == del dect-name["key-name"]
#dict-name.popitem() => it removes the latest key and its value
#dict-name.clear() => delete all the dict's content
#dict-name.keys() => prent all the dict keys
#dict-name.items() => [(key , value), (key, value)] for key, value in dict-name: print(f"this is the {key} and its {value}"")
#dict-name = original_dict.copy()

# range(start, end, steps)
# enumerate(iterable)
'''
my_set = ['ISSAM', 'Morocco']
for index_num, index_value in enumerate(my_set):
    print(f"this index [{index_num}] is for the value [{index_value}]") 

      output >>> 
      this index [0] is for the value [ISSAM]
      this index [1] is for the value [Morocco]
'''
# zip(iterable) concat the iterable in a table
'''
list_1 = [1, 2, 3, 4]
list_2 = ['A', 'B', 'C', 'D']
list_3 = ['1st letter', '2nd letter', '3rd letter']

for item in zip(list_1, list_2, list_3):
    print(item)
'''
# for else
'''
my_list = ['hi', 'hello', 'name']
i = 0
for each in my_list:
    print(i)
    i += 1
else:
    print("for loop is over")
'''
# while else
'''
i = 0
while i < 5:
    print("Hello")
    i += 1
else:
    print(f"now i = {i}")
'''
# functions
'''
def bill(username, amount, due_date): # parameters
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due to {due_date}")

bill("AK", 523.334433, "01/01") # arguments

'''
# return & positional arguments
'''
def add(x, y):
    return f"The result of x + y is {x + y}"

print(add(10, 20))
'''
# default arguments
'''
def f_1(y, x =0):
    for i in range(x, y):
        print("Hello friend!!!")
f_1(5)

'''
# Keywords arguments
'''
def say_hello(username, language):

    if language == "EN":
        print(f"Hello, {username}")

    elif language == "FR":
        print(f"Bonjour, {username}")

    else:
        print(f"({language}) This language is not supported")

say_hello(language= "EN", username= "ISSAM") # those are keywords arguments


for i in range(11):
    print(i, end=" ") # end it is a keyword argument

else:
    print("Done!!!")

print("1","2","3","4","5" ,sep="-") # sep it is a keyword argument
'''

#Arbitrary arguments
# *args  => when we don't know the arguments number
'''
client_1 = (15, 19, 20, 22)
client_2 = (10, 10 ,10, 100)
def total(*prices):
    The_total = 0
    for price in prices:
        The_total += price
    print(The_total)

total (*client_2)
'''
# **kwargs => the same as *args
#  but **kwargs stores data in a dict instead of a tuple
#  it is for key and its value not like *args for one element
'''
prices = tuple([13, 13, 25, 14])
bill = ['orange', 13, 'kiwi', 13, 'bananas' , 25, 'apples', 14]
keys = bill[0::2]
values = bill[1::2]
dict_bill = dict(zip(keys, values))
def bill_total(*prices, **bill):
    for key, value in dict_bill.items():
        print(f"{key} : {value}")

    total = 0
    for price in prices:
        total += price
    print(f"The total is :${total}")

bill_total(*prices, **dict_bill)
'''
# Update every value in a dict
'''
friends_scores = {'person_1' : 29, 'person_2' : 21, 'person_3' : 15}
score_added = 10

friends_scores = { name: score + score_added for name, score in friends_scores.items()}

print(friends_scores)
'''
# map() function
'''
grams = [10, 12, 100, 30]

def g_to_kg(gram):
    return gram / 1000

kg = list(map(g_to_kg, grams))

print(kg)
'''
# lambda
'''
grams = [10, 12, 100, 30]

kg = list(map(lambda gram :gram / 1000 , grams))

print(kg)
'''
# reduce() function reduces elements of iterable to one value
'''
from functools import reduce

prices = {'name' : 20, 'last' : 30}

def add(x, y):
    return x + y

total = reduce(add, prices.keys())
print(total)
'''

#filter() function => it return all elements that pass a condition

'''
grades = [ 60, 21, 70, 80, 15, 30, 96]

def is_passing(grade):
    return grade >= 60

the_passing_grades = list(filter(lambda grade: grade >= 60, grades))
for item in the_passing_grades:
    print(item)
'''
'''
user_word = input("enter a word: ")
word_dict = {}

for index, letter in enumerate(user_word):
    if letter not in word_dict:
        word_dict[letter] = []
    word_dict[letter].append(index)

print(word_dict)
'''

'''
for item in data:
        

print(f"you have {corect_answer} correct answers")
print(f"you have {wrong_answer} wrong answers")

if wrong_answer > 3:
    print("play again")
else:
    print("you are a real fun of Star Wars!!!")
'''
#split() from string to list
#strip() remove white space frem elemt

# inheritance => allows a class to inherite attributes and methods from another class
# encapsulation =>
'''
    -"Encapsulating is a method to make private attribute inside a class": It's the technique of using __private_attrs.

    -"These data can't be modified outside the class": Direct access like object.__attribute = 10 "Error!!!"

    -"It can be presented just for read by function": This is called a "getter" method 

    -"It could be modified by using methods (functions) under conditions": 
    This is the most important part! This is called a "setter" method 
    You put your conditions (validation logic) inside this method.
'''


class Zoo:
    def __init__ (self, zoo_name):
        self.animals = []
        self.name_of_the_zoo = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            print(f"'{new_animal}' added in the {self.name_of_the_zoo}")
            self.animals.append(new_animal)
        
        else:
            print(f"'{new_animal}' is already in {self.name_of_the_zoo}")
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print(f"{animal_sold} has sold")
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in {self.name_of_the_zoo}")

    def sort_animals(self):
        self.animals.sort()
        self.group = {}
        for animal in self.animals:
            animal_first_letter = animal[0]
            if animal_first_letter not in self.group:
                self.group[animal_first_letter] = animal
            else:
                self.group[animal_first_letter] = [animal]
                self.group[animal_first_letter].append(animal)
    def get_groups(self):
        print(self.group)

new_york_zoo = Zoo("new_york_zoo")

animals = ["Bear", "Ape", "Cougar", "Baboon", "Eel", "Cat", "Emu"]
for animal in animals:
    new_york_zoo.add_animal(animal)

new_york_zoo.get_animals()
new_york_zoo.sell_animal(input("enter the animal you wanna sell: "))
new_york_zoo.sort_animals()
new_york_zoo.get_groups()
