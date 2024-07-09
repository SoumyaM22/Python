#1. Write a program to get Fibonacci series
#a=0
#b=1
#n = int(input("Enter any number here: "))
#if n==1:
#    print(1)
#else:
#    print(a)
#    print(b)

#    for i in range(2,n):
#        c=a+b
#        a=b
#        b=c
#        print(c)

#2. Write a program to check if a number is prime or not
#num=int(input("Enter any num here: "))
#if(num<=1):
#    print("not prime, enter num>1")
#else:
#    for i in range(2,num):
#        if num % i == 0:
#            print(" number is not prime ")
#            break
#        else:
#            print("number is prime")
#3. Write a program to find a palindrome of integers.
#num = int(input("Enter any num here: "))
#temp = num
#rev = 0
#while num>0:
#    dig = num % 10
#    rev = rev*10 +dig
#    num=num//10
#if rev==temp:
#    print("it is palindrome")
#else:
#    print("it is not palindrome")

#4. Write a program to create an area calculator.
print("*****AREA CALCULATOR*****")
while True:
    print("""press 1 to get the area of Square
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get the area of triangle""")

    choice = int(input("enter any number 1-4: "))
    if choice == 1:
        while True:
            side= float(input("enter length of one side: "))
            area = side**2
            print("Area of square: ", area)
            repeat = input("do you want to repeat with square again? ")
            if repeat == "no":
                break
    elif choice == 2:
        while True:
            length = float(input("enter length: "))
            breadth = float(input("enter breadth: "))
            area = length * breadth
            print("Area of Rectangle: ", area)
            repeat = input("do you want to repeat with rectangle again? ")
            if repeat == "no":
                break
    elif choice == 3:
        while True:
            radius = float(input("enter radius: "))
            area = 3.14*(radius**2)
            print("Area of Circle: ", area)
            repeat = input("do you want to repeat with circle again? ")
            if repeat == "no":
                break
    elif choice == 4:
        while True:
            breadth = float(input("enter breath: "))
            height = float(input("enter height: "))
            area = 0.5*breadth*height
            print("Area of Triangle: ", area)
            repeat = input("do you want to repeat with triangle again? ")
            if repeat == "no":
                break
    else:
        print("Invalid input")

    repeat1 = input("do you want to repeat with menu again? ")
    if repeat1 == "no":
        break
