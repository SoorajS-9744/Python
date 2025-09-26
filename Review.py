# a = [1,2,3,4,5]

# b = ''

# for i in a:


# class student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

# std1 = student('Sooraj',50)


# num = 10

# def change():
#     num = 5

# change()

# print(num)


# x = [1,2,3,4,5,6]

# y = [y for y in x if y % 2 == 0]

# print(y)


# row = int(input('Enter rows : '))

# for i in range(row , 0 , -1):
#     print(' ' * (row-i) + ' *' * i)


a = [2, 3, 4, 5, 6, 7]

# prime = [i for i in a if all (a % )]

for i in a:
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        print(i)


# b = 10

# for i in range(2, b):
#     if b % i == 0:
#         print('This is  not a prime')
#         break
# else:
#     print('This is a prime')
