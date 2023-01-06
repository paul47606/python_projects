import operator

first = int(input('please enter your number: '))
operator = input('enter operator - (+,-,*,/,%): ')
second = int(input('enter your number: '))

if operator == '+':
    print(first + second)

elif operator == '-':
    print(first - second)

elif operator == '*':
    print(first * second)

elif operator == '/':
    print(first / second)

elif operator == '%':
    print(first % second)

else:
    print('invalid operation')


