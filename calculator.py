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
        num1 = float(tokens[1])
        if len(tokens) < 3:
            num2 = "0"
        else:
            num2 = float(tokens[2])
    if operands == '+':
        result = add(num1, num2)    
    elif operands == '-':
        result = subtract(num1, num2) 
    elif operands == '*':
        result = multiply(num1, num2) 
    elif operands == '/':
        result = divide(num1, num2)  
    elif operands == 'square':
        result = square(num1)       
    elif operands == 'cube':
        result = cube(num1)
    elif operands == 'pow':
        result = power(num1, num2) 
    elif operands == 'mod':
        result = mod(num1, num2) 
    print(result) 