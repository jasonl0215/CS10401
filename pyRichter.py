#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Jason Lyons
#Your ID: s1302192

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
# Input Richter scale value or -99 to end
# While (value does not equal -99)
#             Set the correct warning message
#             Program must print only one warning message for each value entered
#       if (value is less than 0 and does not equal -99)
#             Warning message equals "Value must be greater than 0" and user must enter another value
# Output the warning message
#
# 
# 
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
#Write "Enter the Richter scale value or -99 to end: "
#Read richter scale value
#WHILE (value does not equal -99)
#       Program must print the corret warning message
#       Program must print only one warning message for each richter scale value entered
#    if (value is less than 0 and does not equal -99)
#       print "Value must be greater than 0" and user must enter another value
#Write "The answer is "
#Write answer
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------
answer = ""
rsv = 0
value = ""
while (value != "-99"):
    print()
    rsv = input("Enter the Richter scale value or -99 to end: ")
    value = str(rsv)
    if value >= "8":
        value ="Most structures fall"
    elif value >="7":
        value ="Many buildings destroyed"
    elif value >="6":
        value ="Many buildings considerably damaged, some collapse"
    elif value >="4.5":
        value ="Damage to poorly constructed buildings"
    elif value <"4.5" and value >="0":
        value ="No destruction of buildings"
    elif value <"0" and value !="-99":
        print(value)
        print("Value must be greater than 0, enter another value: ")
    if value != "-99":
        answer = value
        print("The answer is: "+ answer)
    
        
        





      
