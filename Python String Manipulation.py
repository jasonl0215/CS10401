nameString = input("Please enter your last name, first name, your favorite color, your favorite animal and your favorite team:")
commaLocation1 = nameString.find(",")
nameStringLength = len(nameString)
lname = nameString[0:5]
fname = nameString[6:11]
pet = nameString[12:15]
color = nameString[16:20]
team = nameString[21:28]                              
print ("My name is", fname, lname, ", my favorite color is ", color, ", my favorite animal is a", pet, ", and my favorite team is the", team, ".")


