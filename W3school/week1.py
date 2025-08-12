# a = 1
# b = 3
# b = 10
# print(b)


import re             # find digits in string
# a = "my ID is A123B456"

# b = re.findall(r'\d+',a)

# print(b)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# ---------------------print digits only
# import re
# x = 'My Phone number is 88916614669744'

# y = re.search(r'\d{10}', x)

# if y:
#     print(y.group())

# def num(x):
#     return bool(re.fullmatch(r'\d+',x))

# print(num('Hello boy'))
# print(num('123456'))

# to right a file--------------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$$-----------------------------------------------------

# with open('Welcome.txt','w')as file:
#     file.write('Hey Brooooo!!!!!!')

# to read a file----------------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$$$$-----------------------------------------------

# with open('Welcome.txt','r')as y:
#     x = y.read()
#     print(x)

# to append a write prgm---------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4-------------------------------------

# with open('Welcome.txt','a')as y:
#     y.write('\n How are you??????????????')
#     y.write('\n iam fine broh.................')

# to read line by line -----------------------------------$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4-------------------------------------

# with open('Welcome.txt','r')as y:
#     for i in y:
#         print(i.strip())


# -------------------------------------To print a mesg replace error mesg----------------------
# try:
#     x = int(input('Enter 1st no : '))
#     y = int(input('Enter 2nd no : '))

#     z = x / y

#     print(z)
# except ZeroDivisionError:
#     print('You cant devide a number by zero')

# -------------------------------------------------------------------------------------

# for i in range(1,6):   #---------------to create multiplication table ----------------------
#     z = i * 5
#     print(f'{i} * 5 = {z}')

# -------------------------to create multiplication table ----------------------

# ---------------------------------------------using class for task
class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_name(self):
        print(f'Student name is {self.name}')
        print(f'Student grade is {self.grade}')

    def std_age(self, yr):
        print(f'Age of {self.name} is {yr}')


S1 = student('Vishnu', 100)

S1.display_name()
S1.std_age(25)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,without init
#

#     def display_name(self,name,grade):
#         print(f'Student name is {name}')
#         print(f'Student grade is {grade}')

# S1 = student()

# S1.display_name('dude',10)
