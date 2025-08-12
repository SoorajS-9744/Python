# a = lambda x : x % 2 == 0 #-----------using lambda
# x = 17
# print(a(x))
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# add = lambda x,y : x + y

# x = int(input('Enter a number : '))
# y = int(input('Enter a number : '))

# print(add(x,y))
#---------------------------------------------------------------------------------

# a = [1,3,5,7,9]

# def new(x):
#     y = x*2
#     return y

# b = list(map(new,a))
# print(b)
#---------------------------------------------

# a = [1,3,5,7,9]      # map using function and list
# b = [2,4,6,8,10]

# def add(x,y):
#     z = x+y
#     return z
# c = list(map(add,a,b))

# print(c)

#--------------------------------------------------

# a = [1,3,5,7,9]      # map using lambda and list
# b = [2,4,6,8,10]

# x = lambda a,b:a+b
# c = list(map(x,a,b))

# c = list(map(lambda x,y:x+y,a,b))

# print(c)
