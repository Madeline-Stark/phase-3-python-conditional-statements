#!/usr/bin/env python3
#import ipdb
def admin_login(username, password):
    # your code here
    if username.upper() == "ADMIN" and  password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    # If the username is "admin" or "ADMIN" and the password is "12345", 
    # return "Access granted". 
    # Otherwise, return "Access denied".
    

def hows_the_weather(temperature):
    # your code here
    # If the temperature is below 40, 
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    # return "It's brisk out there!". 
    # If the temperature is between 40 and 65, 
    # return "It's a little chilly out there!". 
    # If the temperature is above 85, return "It's too dang hot out there!". 
    # Otherwise, return "It's perfect out there!"
    

def fizzbuzz(num):
    # your code here
    if not num % 3 and not num % 5: #not because if returns 0, that means it's divisible
    # cleaner: if not num % 15:
        return "FizzBuzz"
    elif not num % 3:
        return "Fizz"
    elif not num % 5:
        return "Buzz"
    else:
        return num
    # For multiples of three, 
    # return "Fizz" instead of the number. 
    # For the multiples of five, return "Buzz". 
    # For numbers which are multiples of both three and five, return "FizzBuzz". 
    # For all other numbers, just return the number itself.
    

def calculator(operation, num1, num2):
    #  If the operation is one of the following: +, -, *, or /, 
    # return the value of calling the operation on the two numbers. 
    # Otherwise, output a message saying "Invalid operation!" and return None.
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
         print("Invalid operation!")
         return None
