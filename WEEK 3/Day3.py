# Student score tracker using dictionaries-------------

# student = {}

# while True:
#     print('---Student score tracker---')
#     print("1. Add Student")
#     print("2. View Scores")
#     print("3. Update Score")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = input('Enter your choice : ')

#     if choice == '1':
#         name = input('Enter student name : ')
#         score = int(input('Enter student score : '))
#         student[name] = score
#         print('Student added succesfully')

#     elif choice == '2':
#         if student:
#             for name, score in student.items():
#                 print(f'{name} = {score}')
#         else:
#             print('Student list empty')

#     elif choice == "3":
#         name = input('Enter Update student name : ')
#         if name in student:
#             new_score = int(input('Enter new score : '))
#             student[name] = new_score
#             print(f'{name} = {new_score}')
#         else:
#             print('Student no found')

#     elif choice == "4":
#         name = input('Enter name to delete : ')
#         if name in student:
#             del student[name]
#             print('Student removed successfully')
#         else:
#             print('Name is not found')

#     elif choice == '5':
#         print('You are exit , Thankyou.')
#         break
#     else:
#         print('You entered wrong choice')

# Remove duplicates using sets

# a = [1,2,2,3,3,4,5,5,5,7,8]

# b = list(set(a))
# print(b)

# use another method ------------------------------------

# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# unique_numbers = []
# seen = set()

# for num in numbers:
#     if num not in seen:
#         unique_numbers.append(num)
#         seen.add(num)

# print("List without duplicates (order preserved):", unique_numbers)


# Sort list of tuples

# list_of_tuples = [(1,'banana',15),(3,'apple',10),(2,'cherry',5)]

# a = sorted(list_of_tuples)                                                       # list 1 st digit
# a = sorted(list_of_tuples, key= lambda x : x [1])                                 # list 2 nd digit
# a = sorted(list_of_tuples, key= lambda x : x [2] , reverse=True)                  # list 3 rd digit

# print(a)

# sort group words by lenght

words = ["apple", "bat", "car", "elephant", "dog", "banana", "ant"]

sorted_list = {}

for word in words:
    length = len(word)
    if length not in sorted_list:
        sorted_list[length] = []
    sorted_list[length].append(word)

for key, value in sorted_list.items():
    print(key, '=', value)
