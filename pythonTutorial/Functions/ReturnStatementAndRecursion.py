def hello():
    return("hello world")
print(hello())
hello() #it doesn;t print the value as function retains value
        #but it doesn't print
################################################################
def add(a,b):
    return("Sum of 2 no.s is: ", a+b)
print(add(5,8))
###Recursion##############################################################
def hello2():
    print("hello world")
    return hello2()
#hello2()
####################################################
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print("Factorial of 5 is: ",fact(5))
