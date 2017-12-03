def lhs(a,b):
    return (a+b)**2

def rhs(a,b):
    return a**2+2*a*b+b**2

a = input('Enter a number: ')
b = input('Enter another number: ')

l=lhs(int(a),int(b))

r=rhs(int(a),int(b))


print('{}={} Hence Proved'.format(l,r))
