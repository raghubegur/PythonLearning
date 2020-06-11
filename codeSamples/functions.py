from datetime import datetime

def myFunction(msg):
    print(msg)
    print(datetime.now())

def myProduct(a,b):
    prod = a * b
    return(prod)

def getInitials(firstName, lastName, force_uppercase):
    if force_uppercase:
        return(firstName[0:1].upper() + lastName[0:1].upper())
    else:
        return(firstName[0:1] + lastName[0:1])

myFunction('for loop begin time')

for x in range (0,20):
    print(x)

# myFunction('for loop end time')

# firstNum = int(input('Enter first number: '))
# secNum = int(input('Enter second number: '))

# product = myProduct(firstNum,secNum)
# print(product)

# firstNum = int(input('Enter first number: '))
# secNum = int(input('Enter second number: '))

# product = myProduct(firstNum,secNum)
# print(product)

# firstNum = int(input('Enter first number: '))
# secNum = int(input('Enter second number: '))

# print(myProduct(firstNum,secNum))

firstName = input('Enter first name: ')
lastName = input('Enter second name: ')
print('Your initials are: ' + getInitials(firstName,lastName,True))

firstName = input('Enter first name: ')
lastName = input('Enter second name: ')
print('Your initials are: ' + getInitials(firstName,lastName,False))

fName = input('Enter first name: ')
lName = input('Enter second name: ')
# Use named notation when passing parms to function
print('Your initials are: ' + getInitials(lastName = lName, firstName = fName, force_uppercase = False))


