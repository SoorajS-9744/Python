# class book:
#     catagory = print('Autobiography')

#     def __init__(self, Name, Writer, pages):
#         self.Name = Name
#         self.writer = Writer
#         self.pages = pages

#     def Display(self):
#         print(f'Book Name is {self.Name}')
#         print(self.writer)
#         print(self.pages)


# book1 = book('One Day', 'Sooraj', 500)

# book1.Display()








class employe:
    def __init__(self,Name,Salary):
        self.Name = Name
        self.Salary = Salary

    def display(self):
        print(self.Name)
        print(self.Salary)

    def hello(self):
        print(f'hello {self.Name} your salary is {self.Salary}')


class Worker(employe):
    def __init__(self, Name, Salary,Position):
        super().__init__(Name, Salary)
        self.position = Position

    def posi(self):
        print(self.position)
    
    def hello(self):
        print(f'hello')           #Override




employe1 = Worker('Vishnu',50000,'Manager')

employe1.display()
employe1.posi()
employe1.hello()



        

