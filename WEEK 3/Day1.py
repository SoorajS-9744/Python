# swap 2 variables

# a = 10
# b = 20
# # c = 0

# print(f'a ={a}')
# print(f'b ={b}')
# print('Now Swapping')
# c = a  #------------------------------using 3r variable
# a = b
# b = c

# print(f'a ={a}')
# print(f'b ={b}')

# a, b = b, a  #--------------------------with out 3rd variable

# print(f'a ={a}')
# print(f'b ={b}')

# check a number is even or odd

# number = int(input('Enter a number : '))

# if number % 2 == 0:
#     print(f'{number} is Even')
# else:
#     print(f'{number} is Odd')

# simple calculator

# num1 = int(input('Enter first number : '))
# num2 = int(input('Enter second number : '))
# operator = input('Enter Operator (+,-,*,/): ')

# if operator == '+':
#     print(f'{num1} + {num2} = {num1 + num2}')
# elif operator == '-':
#     print(f'{num1} - {num2} = {num1 - num2}')
# elif operator == '*':
#     print(f'{num1} * {num2} = {num1 * num2}')
# elif operator == '/':
#     print(f'{num1} / {num2} = {num1 / num2}')
# else:
#     print('You entered wrong operator')


# Fizz Buzz implimentation

# print('Fizz , Buzz and FizzBuzz in 1 to 100 : ')

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# print Star  pattern pyramid

row = int(input('Enter rows : '))

for i in range(row , 0, -1):
    print(' ' * (row - i) + '*' * (2 * i - 1))