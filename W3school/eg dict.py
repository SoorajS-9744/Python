# # Creating a dictionary
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# print(person["name"])
# print(person['age'])

# person['email'] = 'alice.com'

# person['name'] = 'john'

# person['age'] = 50

# del person['city']

# print(person)

    
menu = {'appam':20,                 #-------------------------------------
        'chapathi':30,
        'puttu':40,
        'dhosa':50,
        'porotta':60}
# print(menu.items())                #show seperate tuples

# for item in menu.items():
#     print(item)

# for i in menu.items():
#     print('dish',i[0],': rate : ',i[1])   #seperate print key,value
#,,,,,,,,,,,,,,,,,,,,,,,,,,,
# for i in menu.items():                   #unpacking method
#     food,rate = i
#     print('dish',food,': rate :',rate)      
#-----------------------------
# item = menu.get('puttu')                   # write value
# print(item)

# item = menu.get('idli')
# print(item)
#------------------------------------

value = menu.pop('puttu')                  #using pop
print(value)
print(menu)
#-------------------------------------
# menu.clear()                               # to reomve all
# print(menu)
#---------------------------------

# menu_items = ['appam','dosha','puttu']    #create a dict from 2 list
# menu_rate = [20,30,50]

# menu = dict(zip(menu_items,menu_rate))
# print(menu)
#-----------------------------------------------
# menu = {'appam':20,                 #-------------------------------------
#          'chapathi':30,
#          'puttu':40,
#          'dhosa':50,
#          'porotta':60}
# if 'ladu' in menu.keys():              # found keys in dict
#     print('key found in menu')
# else:
#     print('key not found in menu')

# if 30 in menu.values():                 # found values in dict
#     print('value found in menu')
# else:
#      print('value not found in menu')
#----------------------------------------------------

# a = [('clt',10),('tvm',20),('ekm',30)]   # list of tuple to dict

# t = dict(a)
# print(t)