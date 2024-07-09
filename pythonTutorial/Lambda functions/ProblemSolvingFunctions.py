#1. Write a function to find maximum of 3 no.s in Python
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print("Greatest number: ",val1)
    elif val2>val1 and val2>val3:
        print("Greatest number: ",val2)
    else:
        print("Greatest number: ",val3)
maximum_num(62,31,83)
maximum_num(62,31,8)
#2. Write a python function to create and print a list where the values are squares of numbers between 1 & 30.
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())
#3. Write a python function that takes a number as a parameter and check if number is prime or not.
def check_prime(num):
    if num == 1:
        print("It's not prime")
    if num == 2:
        print("It's prime")
    if num > 2:
        for i in range(2,num):
            if num % i == 0:
                print("It's not prime")
                break
        else:
                print("It's prime number")
check_prime(2)
check_prime(9)
check_prime(3)

#4. Write a python function to sum all the numbers in a list.
##solution-1 Using List
def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return total
print(add([12,4,5,6,7,8]))

##solution-2 Using Recursion
def add_recur(numbers):
    if len(numbers) == 1:
        return (numbers[0])
    else:
        return (numbers[0]+ add_recur(numbers[1:]))

print(add_recur([12,4,5,6,7,8]))

#5. Write a python function to solve the Fibonacci squence using Recursion.
##0,1,1,2,3,5,8,13

def fs(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fs(num-1)+fs(num-2))

print(fs(8)) # here index starts from 7 to 1