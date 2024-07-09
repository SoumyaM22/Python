#Write a program to check if a number is positive,
#num=int(input("enter a number here: "))
#print("num: ", num)
#if num>0:
#    print("num is positive")

#Write a program to check whether a number is odd or even.
#num=int(input("enter a number here: "))
#print("num: ", num)
#if (num%2)==0:
#    print("num is even")
#else:
#    print("num is odd")

#Write a program to create area calculator.
#print("*****AREA CALCULATOR*****")
#print("""press 1 to get the area of Square
#press 2 to get the area of rectangle
#press 3 to get the area of circle
#press 4 to get the area of triangle""")

#choice = int(input("enter any number 1-4: "))
#if choice == 1:
#    side= float(input("enter length of one side"))
#    area = side**2
#    print("Area of square: ", area)
#elif choice == 2:
#    length = float(input("enter length: "))
#    breadth = float(input("enter breadth: "))
#    area = length * breadth
#    print("Area of Rectangle: ", area)
#elif choice == 3:
#    radius = float(input("enter radius: "))
#    area = 3.14*(radius**2)
#    print("Area of Circle: ", area)
#elif choice == 4:
#    breadth = float(input("enter breath: "))
#    height = float(input("enter height: "))
#    area = 0.5*breadth*height
#    print("Area of Triangle: ", area)
#else:
#    print("Invalid input")

#Write a program to check whether the passed letter is a vowel or not.
#letter = input("Enter a letter here: ")
#if letter in "aeiou" or letter in "AEIOU":
#    print("letter is vowel")
#else:
#    print("it is not a vowel")

#Write a program to check if a number is a single digit number, 2-digit number and so on.. , up to 5 digits
num = int(input("Enter a number here up to 5 digits"))
if num >= 0 and num <= 9:
    print("it is one digit no. ")
elif num >= 10 and num <= 99:
    print("it is two digit no. ")
elif num >= 100 and num <= 999:
    print("It is three digit no. ")
elif num >= 1000 and num <= 9999:
    print("It is four digit no. ")
elif num >= 10000 and num <= 99999:
    print("It is five digit no. ")
else:
    print("It is invalid input !!! ")