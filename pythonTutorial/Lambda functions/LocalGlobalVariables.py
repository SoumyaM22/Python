#x = 24 #local variable
#print("first variable x ",x)
#def hello():
#    x = 25 #local variable
#    return x
#print(hello())
##ouput:first variable x  24
##      25

###Global variable################################
x = 25 #local variable
print("first variable x ",x)
def hello():
    global x #global variable
    x = 24
    return x
print(hello())
print(x)
##ouput: first variable x  25
##          24
##          24

