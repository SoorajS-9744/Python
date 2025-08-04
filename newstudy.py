# a = {'appu':20,'doppu':30,'kuppi':40,'thoppi':50}
# print(a)
# x = a.pop('choppi','not found')

# print(x)
# print(a)

# a = {'appu':20,'doppu':30,'kuppi':40,'thoppi':50}

# for name ,age in a.items():
#     print(name ,"is",age,'yrs old')  # old method
#     print(f'my name is {name} iam {age} yrs old')    # new method
    
# a = ['apple','banana','orange','apple','orange','apple']   #using function----------------------------

# def count(a):
#     c = {}
#     for b in a:
#         c[b] = c.get(b,0)+1
#     return c
# print(count(a))

# a = [[5,3,6],[1,10,7]]     #;;;;;;;;;;;;;;;;;;;;;for nxt reviw

# b = []

# for sublist in a:
#     for c in sublist:
#         b.append(c)
# print(b)

a = [1,2,1,3,5,3,6,4,8,9,5,9,1,2] #-----------------------to convert SET
# b = set(a)
# print(b)

# b.add(15)
# print(b)
# b.remove(15)
# print(b)
# b.discard(9)
# print(b)
#--------------------------sum of even numbers
# sum = 0
# for i in a:
#     if i % 2 == 0:
#         sum += i
# print(sum)
#-------------------------------

#-------------------------Dict task--------------------------------------------------------------------
# a = {'symbro':[20,10,5],'sooraj':[15,8,12],'vyshnav':[50,40,30]}  #-------------------Task of dict

# a['rahul'] = [2,1,0]

# print(a)

# for name,mark in a.items():
#     avg = sum(mark) / len(mark)
#     print(f'{name}\'s avarage mark is {avg:.2f}')
#     if avg > 5 :
#         print('Great studnt')
#     else:
#         print('Waste studnt')
#--------------------------------------------------------------------------------------------------------
std = []
roll_no = set()

for i in range(5):
    a = input('enter student name : ')
    b = input('enter roll no : ')
    std.append(a)
    roll_no.add(b)



print(std)
print(roll_no)