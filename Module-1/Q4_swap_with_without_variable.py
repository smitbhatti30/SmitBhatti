'''

#with variable

x = input('Enter value of x: ')
y = input('Enter value of y: ')

A = x
x = y
y = A

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
'''
#without variable 

x = input('Enter value of x: ')
y = input('Enter value of y: ')

x, y = y, x
print("x =", x)
print("y =", y)