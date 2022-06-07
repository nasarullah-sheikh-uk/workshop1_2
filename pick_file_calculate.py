filecalc = open('calculate.txt')
Lines = filecalc.readlines()

count = 0
ADD_all_lines = 0

for line in Lines:
    line = line.strip()
    ign, oper, num1, num2 = line.split(" ")
    count += 1

    if ( oper == "+"):
        ADD = int(num1) + int(num2)
        ADD_all_lines = ADD_all_lines + ADD
        print( "Sum of numbers: ", ADD )
    elif ( oper == "x" ):
        PROD = int(num1) * int(num2)
        ADD_all_lines = ADD_all_lines + PROD
        print( "Product of numbers: ", PROD )
    elif ( oper == "/" ):
        DIV = int(num1) / int(num2)
        ADD_all_lines = ADD_all_lines + DIV
        print( "Division of numbers: ", DIV )
    elif( oper == "-" ):
        SUB = int(num1) - int(num2)
        ADD_all_lines = ADD_all_lines + SUB
        print( "Subtraction of numbers: ", SUB )
    elif( oper == "**" ):
        POW = int(num1) * int(num2)
        ADD_all_lines = ADD_all_lines + POW
        print( "Number1 power to Number2: ", POW )
    
    print ("Line number: ", count, oper, num1, num2, ADD_all_lines)

print ("Sum of all line calculations is: ", ADD_all_lines)


filecalc.close()

