# x = " heLLo, im sOOraj , oooo"
# # print(f'Type of x is {type(x)}') #--------------show tpre

# # print(x.strip())     #-------------------------------remove space
# a = x.strip()
# print(a.capitalize()) #---------------------capitalize (first letter)
# print(a.replace('hello' , 'Good mrng')) #----------replace a string
# print(a.upper())
# print(a.lower())
# print(a.casefold())  #-------------------------to convert lower
# print(a.center(50,'$')) #---------------------first width , 2 nd fill chyyande sanm
# print(a.count('o')) #----------------count a letter or word

# a = 'കാലം പോകുന്ന പോക്കേ'
# print(a)
# b = a.encode('utf-8')
# print(b.decode('utf-8'))


a = [1, 2, 3, 4, 8, 7, 11, 20, 15, 14]

# odd = []

# even = []

# for i in a:
#     if i % 2 != 0:
#         odd.append(i)
#     else:
#         even.append(i)

# print(odd)
# print(even)
# ------------------------------------------------------------prime or not
# prime = []
# non_prime = []

# for i in a:
#     if i > 1:
#         for x in range(2 , i):
#             if i % x == 0:
#                 non_prime.append(i)
#                 break
#         else:
#             prime.append(i)


# print(prime)
# print(non_prime)

# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# ------------------------------------------------------

# a = ['a', 'b', 'c', 'd', 'e', 'f']

# count = 0

# for i in a:
#     if i in str('aeiouAEIOU'):
#         count += 1
# print(count)

# a = int(input('Emter a number : '))  #-------------------------------------------------

# for i in range(1,11):
#     x = i * a
#     print(f'{i} * {a} = {x}')


# a = 'Programming'  # ------$$$$$$$$$$$$$$ without using built in function to reverse a string

# x = ''

# for i in a:
#     x = i + x
# print(x)

# def rev_String(a):  # ----------using function
#     x = ''
#     for i in a:
#         x = i + x
#     print(x)


# string = 'programming'

# rev_String(string)


# row = 5

# for i in range(row , 0 ,-1):
#     print(' ' * (row - i) + ' *' * i)

# a = lambda x,y : x+y

# print(a(3,5))
