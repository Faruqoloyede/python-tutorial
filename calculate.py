a = int(input('enter first number:'))
b = int(input('enter second number'))
c = str(input('enter the operation you want to perform '))

if c == 'addition:':
    print(a + b)
elif c == 'subtraction':
    print(a - b)
elif c == 'multiplication':
    print(a * b)
elif c == 'division':
    print(a /b)
elif c == 'modulus':
    print(a%b)
else:
    print('unable to perform operation')
