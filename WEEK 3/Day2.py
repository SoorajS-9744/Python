# to check a number is prime or not
# def check(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print('It is not a prime number')
#             break
#     else:
#         print('It is a prime number')


# a = int(input('Enter a number : '))
# check(a)

# Reusable function to convert temperature

# def temp_converter(temp, unit):
#     if unit == 'c' or 'C':
#         f = (9/5*temp)+32
#         print(f'fahrenheit unit of {temp} digree celsious is = {f} F')
#     elif unit == 'f' or 'F':
#         c = ((temp-32)*5)/9
#         print(f'celsious unit of {temp} fahrenheit is = {c} C')
#     else:
#         print('wrong unit')


# a = int(input('Enter Temperature : '))
# b = input('Enter unit : ')

# temp_converter(a, b)

# Error handling

# try:
#     a = int(input('Enter a number : '))
#     b = int(input('Enter second number : '))

#     print(f'{a} / {b} = {a / b}')

# except ZeroDivisionError :
#     print('Dividing by Zero is not allowed')

# Create a custom exception scenario

# def age(age):
#     if age < 10:
#         print('Child')
#     elif age < 25:
#         print('Young')
#     elif age < 50:
#         print('Men')
#     elif age < 80:
#         print('Legend')
#     else:
#         raise ValueError


# try:
#     a = int(input('Enter Age : '))
#     age(a)
# except ValueError:
#     print('Passed away')

