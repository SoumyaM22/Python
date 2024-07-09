#A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
##1. Write a program to separate the following string into coma(,) separated values.
#b = A.split('.')
#print(b)
##2. Write a program to sort strings alphabetically in python.
#input = input("enter any char here to be sorted: ")
#c = sorted(input)
#print(c)
##3. Write a program to remove a given character from a string.
#Z = "F.R.I.E.N.D.S"
#print(Z.replace("F","A"))
##4. Write a program to remove dot (.) from the following string.
#print(Z.replace(".",""))
##5. Write a program to check the number of occurances of string.
#print(A.count("OT"))

##############################################################
#1. Take an input from a user as a string then, reverse it
##e = input("enter any string from user: ")
##print(e[::-1])

#2. Write a program to check ifit contains only digits.
##f = input(" enter any string: ")
##print(f.isdigit())
##if f == "True":
##    print("it contains only digits")
##else:
##    print("it doesn't contain only digits")

#3. Write a program to check if a string is palindrome.
##g = input("enter any string from user: ")
##rev = g[::-1]
##print(rev)
##if rev==g:
##    print("it is palindrome")
##else:
##    print("it is not palindrome")

#4. Write a program to find number of vowels in a string.
##h = input("enter any input here: ")
##vowels = 0
##for i in h:
##    if i == "a" or i =="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="U" or i=="u":
##        vowels += 1
##print("no. of vowels in string: ",vowels)

#5. Write a program to check if every word in a string begins with a capital letter.
j = input("enter any string here: ")
k = j.istitle()
if k==True:
    print("it is capital at each word")
else:
    print("it is not capital at each word")