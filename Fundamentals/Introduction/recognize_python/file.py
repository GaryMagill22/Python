num1 = 42 # variable decloration, integer
num2 = 2.3 # variable decloration, float
boolean = True # boolean type variable, True
string = 'Hello World' # length = 11
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # single line comment.

"""
multi line comment
multi line comment
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # data type dictionary, False = boolean, 37 is number(int)
fruit = ('blueberry', 'strawberry', 'banana') # list of strings
print(type(fruit)) # asking python what data type (fruit) is
print(pizza_toppings[1]) # print "sausage" through dot notation
pizza_toppings.append('Mushrooms') #adds "mushrooms" to the list
print(person['name']) # prints John from person list
person['name'] = 'George' # changing name from "John" to "George"
person['eye_color'] = 'blue' # adds new key value pair ( since doesnt exist already in list)
print(fruit[2]) # prints "banana" to terminal

if num1 > 45: # num1 = 42 (not greater than 45)
    print("It's greater") # wont run this code - not greater than 45
else:
    print("It's lower") # prints this line because num1 is less than 45.

if len(string) < 5: # length of variable "string" = 11
    print("It's a short word!") # wont run this line 
elif len(string) > 15: # wont print this line ( 11 is not greater than 15)
    print("It's a long word!")
else:
    print("Just right!") # will print "Just right!" to terminal. 

for x in range(5):  # for loop that stops at 5 and starts at 0
    print(x) # 0 1 2 3 4 
for x in range(2,5): # for loop that starts at 2 and ends at 5
    print(x) # 2 3 4 
for x in range(2,10,3): # for loop starts at 2 and ends at 9 incrementing by 3 each time
    print(x) # 2 5 8
x = 0 # while loop where x starts at 0.
while(x < 5):  # while x is less than 5 run this code (line 41)
    print(x) # 0 1 2 3 4 
    x += 1 # (x = x + 1) - increments x



pizza_toppings.pop()  # pops off "mushrooms" from list 
pizza_toppings.pop(1) # pops off "sausage" from list

print(person) # prints person and all key value pairs to terminal
person.pop('eye_color') # removes eye color from list
print(person) # prints person without the eye_color variable we just removed

for topping in pizza_toppings: # for loop using pizza_toppings list
    if topping == 'Pepperoni': # first tpping is "peperoni"
        continue
    print('After 1st if statement') # prints this three times until it gets to "olives" then breaks out of the code 
    if topping == 'Olives':
        break

def print_hello_ten_times(): # function called "print_hello_ten_times"
    for num in range(10): # for loop starting at 0 going to 9
        print('Hello') # prints "Hello"

print_hello_ten_times() # function envoked - prints "Hello" 9 times (0-9) 

def print_hello_x_times(x): # sets parameter x
    for num in range(x): # for loop going until get 4
        print('Hello')

# giving argument of "4" to the function and calling it
print_hello_x_times(4) # print 'Hello" four times

def print_hello_x_or_ten_times(x = 10): # function named print_hello_x_or_ten_times
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # envoked with no arguments. prints "hello" 9 times.
print_hello_x_or_ten_times(4) # envokes with argument 4. prints 'Hello' 3 times.


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)