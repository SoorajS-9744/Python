row = int(input('Enter rows : '))

# for i in range(row, 0, -1):
#     print(' ' * (row - i) + '*' * (2 * i - 1))

# for i in range(1 , row+1):
#     print(' ' * (row - i) + '*' * (2 * i - 1))


# for i in range(1 , row+1):
#     print('*' * i )


# for i in range(1 , row+1):
#     print(' ' * (row - i) + '*' * i)

# for i in range(row , 0 , -1):
#     print('* ' * i )


for i in range(row , 0 , -1):
    print(' ' * (row - i) + '*' * i)