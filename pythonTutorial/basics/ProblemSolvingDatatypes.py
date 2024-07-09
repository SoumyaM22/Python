#Write a program to display a person's name,age & address in 3 different lines.
name= "Isha"
age= 4
address="222 Walnut street, Atlanta, GA"
print(name)
print(age)
print(address)



#Write a program to swap two variables
#method 1
x=12
y=13

temp=x
print("temp:",temp)
x=y
y=temp

print("x:",x)
print("y:",y)

#method 2
a=30
b=40

#left,right=right,left
a,b=b,a
print("a: ",a)
print("b: ",b)


#Write a program to convert a float into integer.
f=2.3
print("f: ", f)
print(type(f))
x=int(f)
print("int value of f: ",x)
print(type(x))


#Write a program to take details from a student for ID card & then print it in different lines
student_name=input("Enter student_name: ")
student_age=int(input("Enter student_age: "))
student_grade=input("Enter student_grade: ")
student_email=input("Enter student_email: ")
student_phone=input("Enter student_phone: ")
print("_____Student ID Card_____")
print("name: ",student_name)
print("age: ",student_age)
print("grade: ",student_grade)
print("email: ",student_email)
print("phone: ",student_phone)


#Write a program to take an user input as integer then convert to float.
i=int(input("Enter any integer here: "))
print(type(i))
i=float(i)
print("after conversion",type(i))
print(i)