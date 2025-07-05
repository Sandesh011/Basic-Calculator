import math
while True:
    number1 = input("ENTER A NUMBER: ")
    operator = input("Select your operator (+,-,*,/,%,**,sqrt and q for quit): ")
    if operator.lower() =="q":
        print("Thanks for using our calculator.Goodbye!")
        break
    if operator != "sqrt":
        number2 =input("ENTER SECOND NUMBER: ")
    else:
        number2= None
    try:
        number1 = float(number1)
        if operator != "sqrt":
            number2 = float(number2)
    except ValueError:
        print("You have entered invalid number please enter valid numbers")
        continue
    if operator == "+":
        result = (number1) + (number2)
    elif operator == "-":
        result = (number1) - (number2)
    elif operator == "*":
        result = (number1) * (number2)
    elif operator == "/":
        if (number2) == 0:
            result = "Error! You cannot divide any number by 0"
        else:
            result = (number1) / (number2)
    elif operator == "%":
        if number2 == 0:
            result= "Error! You cannot module with 0"
        else:
            result = number1 % number2
    elif operator == "**":
        result= number1 ** number2
    elif operator == "sqrt":
        if number1< 0:
           result= "You cannot get square root of negative numbers"
        else:
            result = math.sqrt(number1)
    else:
        result = "Invalid operator please enter valid operator to continue!"
    print(result)