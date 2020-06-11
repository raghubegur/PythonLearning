x = 42
y = 0

print()

try:
    print(x / y)
except ZeroDivisionError as e:
    print('Division by zero not allowed')
else:
    print('Something else went wrong')
finally:
    print('This is my clean up code')

print()