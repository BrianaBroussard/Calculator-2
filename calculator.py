"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Enter your equation >")
    tokens = input_string.split(" ")
    operands = tokens[0]
    if operands == "q":
        print("You're done")
        break 
    else:
        num1 = tokens[1]
        if len(tokens) < 3:
            num2 = "0"
        else:
            num2 = tokens[2]
    if operands == '+':
        result = add(float(num1), float(num2))    
    elif operands == '-':
        result = subtract(float(num1), float(num2)) 
    elif operands == '*':
        result = multiply(float(num1), float(num2)) 
    elif operands == '/':
        result = divide(float(num1), float(num2))  
    elif operands == 'square':
        result = square(float(num1))       
    elif operands == 'cube':
        result = cube(float(num1))
    elif operands == 'pow':
        result = power(float(num1), float(num2)) 
    elif operands == 'mod':
        result = mod(float(num1), float(num2)) 
    print(result) 