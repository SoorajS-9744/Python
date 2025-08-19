# #July 22 2025
# #My first program
# # initialize variables
# customer_id = 150
# name = "Sooraj"
# account_balance = 20000.00
# loan_elegibility = True

# # print customer details

# print("......................")
# print("Customer Details")
# print("customer ID:",customer_id)
# print("Name:",name)
# print("Account Balance:",account_balance)
# print("Eligibily:",loan_elegibility)

# # corrected customer details

# name = "Vishnu"
# account_balance = 15000.00

# # print corrected details

# print("......................")
# print("Customer Details")
# print("customer ID:",customer_id)
# print("Name:",name)
# print("Account Balance:",account_balance)
# print("Eligibily:",loan_elegibility)
# --------------------------------------------------------------------------------------------

# n = int(input("Enter number of rows : "))

# for i in range(n, 0, -1):
#     print(' ' * (n-i) + " *" * (i))

# count = 0
# for i in range(1,10):
#     if i % 2 != 0:
#         print(i)
#         count += i
# print(count)


# print('Play a game ROCK , PAPPER , SISOR')

# while True:

#     choices = 'r', 'p', 's'

#     choice_1 = input('First choice: ')
#     choice_2 = input('Second choice: ')

#     if choice_1 not in choices:
#         print('invalid input')
#         continue

#     elif choice_2 not in choices:
#         print('invalid input')
#         continue

#     if choice_1 == choice_2:
#         print('tie')
#     elif choice_1 == 'r' and choice_2 == 'p':
#         print(f'{choice_2} wins')
#     elif choice_1 == 'p' and choice_2 == 'r':
#         print(f'{choice_1} wins')
#     elif choice_1 == 'p' and choice_2 == 's':
#         print(f'{choice_2} wins')
#     elif choice_1 == 's' and choice_2 == 'p':
#         print(f'{choice_1} wins')
#     elif choice_1 == 's' and choice_2 == 'r':
#         print(f'{choice_2} wins')
#     elif choice_1 == 'r' and choice_2 == 's':
#         print(f'{choice_1} wins')
#     break


# while True:

#     choices = 'r', 'p', 's'

#     choice_1 = input('First choice: ')
#     choice_2 = input('Second choice: ')

#     if choice_1 not in choices:
#          print('invalid input')
#          continue

#     elif choice_2 not in choices:
#          print('invalid input')
#          continue

#     if choice_1 == choice_2:
#         print('tie')
#     elif choice_1 == 'r' and choice_2 == 'p' or choice_1 == 'p' and choice_2 == 's' or choice_1 == 's' and choice_2 == 'r':
#          print(f'{choice_2} wins')
#     elif choice_1 == 'p' and choice_2 == 'r' or choice_1 == 's' and choice_2 == 'p' or choice_1 == 'r' and choice_2 == 's':
#          print(f'{choice_1} wins')
#     break

# a = [[1, 2], [3, 4]]

# b = []

# for sub_list in a:
#     for item in sub_list:
#         b.append(item)
# print(b)


a = [1, 2, 3, 4, 8, 7, 11, 20, 15, 14]

odd = []
even = []

for i in a:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
print(odd)
print(even)
