# to check a number is prime or not
def check(num):
    for i in range(2,num):
        if num % i == 0:
            print('It is not a prime number')
            break
    else:
        print('It is a prime number')

                
a = int(input('Enter a number : '))
check(a)