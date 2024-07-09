#Write a program to display this
#if pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print(j,end=" ")
    print() # to print in next line

#######################################
# *
# * *
# * * *
# * * * *
# * * * * *
#for i in range(1,6): #rows
#    for j in range(1,i+1): #columns
#        print("*",end=" ")
#    print()
########################################
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6): #rows
    for j in range(1,i+1): #columns
        print(i,end=" ")
    print()

########################################
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()

########################################
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
#########################################

