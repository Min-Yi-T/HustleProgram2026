
        # Snippit 1

#x = 10
#y = 0
#result = x / y
#print("Result :" + result)

# Perdict : "I think this will be the zero division error because you can't divide numbers with zero. Underneath this is the correct code btw."

x = 10
y = 0
if y != 0:
    print(x / y)
else:
    print("Cannot divide by zero.")


# Snippit 2

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

# Perdict : "I think this will be the off by one error. it will not put in the first number and it will want to keep on counting."

# Snippit 3

def calculate_area(radius):
    area = 3.14 * radius ** 2 
    return area 

radius = 5 
print(calculate_area(radius)) 

# Perdict : "I perdict that snippit 3 is a syntax error because it just seems to have forgotten the : and the tab spaces to make it into a whole function."

# Snippet 4 

def is_even(number): 
    if number % 2 == 0 :
        return True 
    else:
        return False 
print(is_even(4)) 
print(is_even(7)) 

# Perdict : "I perdict that is is another syntax error that has forgotten the tab spaces."

# Snippet 5 

for i in range(5):
    print(i) 

# Perdict : "I perdict that they is yet again another syntax error because if again had forgotten the : and the tab space."

# Snippet 6 

def greet(name): 
    return("Hello, " + name)
print(greet("Alice")) 

# Perdict : "I perdict that this is another syntax error because it forgotten the tab space as well as the () on both sides for return."

# Snippet 7 

numbers = [1, 2, 3, 4, 5] 
total = 0 
for number in numbers: 
    total += number 
print("Sum of numbers:", total) 

# Perdict : "I perdict that this is another syntac error since all it forgotten was the tab space on 'total += number'."

# Snippet 8 

def factorial(n): 
 if n == 0: 
    return 1 
 else: 
    return n * factorial(n - 1) 
print(factorial(5)) 

# Perdict : "I perdict that this is probably another syntax error because all you need to change was the + into a -"

# Snippet 9 

name = input("Enter your name: ") 
if name == "Alice" or name == "Bob": 
 print("Hello, " + name + "! Welcome back!") 
else: 
 print("Hello, stranger!") 

# Perdict : "I perdict that this is the incorrect condictional because if you don't put 'name == Bob', it won't count it and will always make the statement False, therefore always saying 'Hello Stranger!'."

# Snippet 10 

def divide_numbers(x, y): 
    if y != 0:
        print(x / y)
    else:
        print("Cannot divide zero")

num1 = 10 
num2 = 0 
print(divide_numbers(num1, num2)) 


