#Write a program to find a sum of all the even numbers up to 50
#sum=0
#for i in range(1,51):
#    if i%2 == 0:
#        sum += i
#print("The sum of all even numbers upto 50:", sum)

#Write a program to write first 20 numbers & their squared numbers.
#for i in range(1,21):
#    print("i",i,"square: ",i**2)

#Write a program to write first 10 odd numbers using while loop.
#using while loop
#i=0
#sum=0
#while i<=20:
#    if i%2 != 0:
#        sum +=i
#    i += 1
#print("Sum of first 10 odd no.s: ", sum)

#Write a program to check if a number is divisible by
# 8 and 12, upto 100 numbers.
for i in range (1,101):
    if i%8==0 and i%12==0:
        print(i)
#Write a program to create a billing system at supermarket.
while True:
    Name = input("Enter customer name: ")
    total = 0
    while True:
        quantity = float(input("Enter how many: "))     #2
        amount = float(input("Enter price: "))   #2*100 = 200
        total += (amount * quantity)       #200 + 50 = 250
        repeat = input("Enter yes or no: ")
        if repeat=="no" or repeat=="No":
            break
    print("Customer name: ", Name)
    print("Total amount: ",total)
    print("-"*40)
    print("****Happy Shopping****")

    repeat1 = input("do you want to go to next customer? (yes/no)")
    if repeat1 == "no" or repeat == "No":
        break













