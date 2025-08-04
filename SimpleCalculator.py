# Here is a simple calculator program

#Usiing a function to define the program:
def calculator():
    print("This is as Simple Calculator.\n Use it to do the following operations:")
    print(" +, -, *, /\n")
    print("Please don't be tempted to do strange stuff like divide by zero. \nYou may open a portal to worlds unknown...")
    

    # Get user input
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    # Perform calculation based on operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed! \nStop trying to open portals please.\n I want to finish this course, thank you")
            return
    elif ValueError:
        print("Error: Please enter valid numbers! This is a simple program. I am not a graphing calculator yet!")
    else:
        print("Invalid operation! Please use one of: +, -, *, /")
        return
    
    # Print the result
    print(f"Result: {num1} {operation} {num2} = {result}")
 
        

# Run the calculator
calculator()