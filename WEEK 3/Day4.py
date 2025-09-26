# write , read and append in file

# with open('create file.txt','w')as file:      #to write a file
#     file.write(input())


# with open('create file.txt','r')as file:
#     a = file.read()
#     print(a)


# with open('create file.txt', 'a')as file:
#     # file.write('\n')                               # to write next line
#     file.write('\n' + input())


# list/Dict comprehension

# even = [x for x in range(20, 41) if x % 2 == 0]     # print even  using list comprehension

# print(even)

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# words = ['elephant', 'Lion', 'Tiger']      # to print a first letter of string

# first_letter = [x[0] for x in words]

# print(first_letter)

# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,dict comprehension

# name = ['Vishnu']

# dict_of_word_length = {x : len(x) for x in name}

# print(dict_of_word_length)

# multiplication table using nested comprehension(dict)

# j = int(input('Enter a number for multiplication table : '))

# multi = {f'{i} * {j}' : i * j for i in range(1 ,11) }

# for key,value in multi.items():
#     print(f'{key} = {value}')

# list a single list from a list using comprehension

# list = [[1, 2], [3, 4], [5, 6]]

# new_list = [a for num in list for a in num]

# print(new_list)


# Count word frequency in a text file

# with open('create file.txt','r')as file:
#     my_file = file.read()
#     # print(my_file)
# my_list = my_file.lower().split()

# print(my_list)


# freq_dict = {word : my_list.count(word) for word in set(my_list)}

# print(freq_dict)

# Store user data in a file


# with open('User data.txt', 'a')as user_data:
#     user_data.write(input('Enter student name : ') + ' ')
#     user_data.write(input('Enter Student mark : ') + '\n')


# Generate a list of squares or primes using comprehensions

prime = [i for i in range(2, 100) if all(i % x != 0 for x in range(2, i))]

print(prime)
