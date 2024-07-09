def add(x,y): # parameters: variables mentioned while defining function
    print(x+y)
add(3,4) # arguments: values passed tp parameters while function calling

################################################
def rectangle(x,y):
    print("Area of rectangle: ",x*y)
rectangle(3,4)

##################################################
def hello(name):
    print("hello, my name is, ",name)
hello("John")
####################################################
def hello(*name):
    print("hello, my name is, ",name[1])
hello("John","lisa","Peter")


