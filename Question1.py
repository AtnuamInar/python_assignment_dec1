#!usr/bin/python3

fname=input('Enter Customers Name')
address=input('enter your Address')
items=input('Enter the number of items brought')

price=float(items)*100

print('_____________________________________________________')
print('Welcome to Fuchu Supermarket')
print('_____________________________________________________')


print("HI {0}, here is your bill:".format(fname))
print('You brought {0} items'.format(items))
print('Total price={}'.format(price))



