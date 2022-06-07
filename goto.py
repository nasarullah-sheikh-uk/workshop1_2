
#########################################
# Open and dump the file in a list
#########################################
gotofile =  open ('goto.txt')
file_content = gotofile.read()

# replacing end splitting the text 
# when newline ('\n') is seen.
file_into_list = file_content.split("\n")
gotofile.close()

print("Length of our file is: ", len(file_into_list) )


## Check what the line has and return go to line
def check_line(line):
    line_content = file_into_list[line].split(" ")
    if (line_content[1].isnumeric() == True):
        lno = int(line_content[1]) - 1
        return lno
    else:
        ign, ign1, oper, num1, num2 = line_content
            if ( oper == "+"):
                OUT = int(num1) + int(num2)
            elif ( oper == "x" ):
                OUT = int(num1) * int(num2)
            elif ( oper == "/" ):
                OUT = int(num1) / int(num2)
            elif( oper == "-" ):
                OUT = int(num1) - int(num2)
            elif( oper == "**" ):
                OUT = int(num1) * int(num2)
        return OUT


# Process the goto statements
