# price = input('Enter price: ')
# price = float(price)

price = float(input('Enter price: '))

# state = input('Enter state: ')
# state = state.upper()

state = input('Enter state: ').upper()

print('State is: ' + state)

if state == 'GA' or state =='MS':
    livable = False
    if price >= 1.00:
        tax = 0.07
    else:
        tax = 0.0
elif state in ('TX','AL','FL','KY'):
    livable = False
    tax = 0.12
elif state == 'CA':
    livable = True
    if price >= 1.00 and price <= 5.00:
        tax = 0.08
    else:  
        tax = 0.09
else:
    tax = 0.1

totalPrice = price + price*tax
print('TotalPrice is: ' + str(totalPrice))

if livable:
    print('I like to live in ' + state)