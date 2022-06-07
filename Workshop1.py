def get_an_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value            

while True:
    try:
        oper = input("Please enter a operation to provide ( + - / * ** ): ")

    except ValueError:
        print("Sorry, I did not understand that.")
        continue

    if oper not in ["+", "*", "-", "/", "**"]:
            print("Sorry, operator should be as follows: Add +, subtract - , mulitply *, raise a power **.")
            continue        
    else:
        # We picked correct operator
        break

num1 = get_an_integer("Please enter first number: ")
num2 = get_an_integer("Please enter 2nd number number: ")

if ( oper == "+"):
    print( "Sum of numbers: ", num1 + num2 )
elif ( oper == "*" ):
    print( "Product of numbers: ", num1 * num2 )
elif ( oper == "/" ):
    print( "Division of numbers: ", num1 / num2 )
elif( oper == "-" ):
    print( "Subtraction of numbers: ", num1 - num2 )
elif( oper == "**" ):
    print( "Number1 power to Number2: ", num1 ** num2 )