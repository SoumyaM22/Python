##items()############################################################
Student = {"name":"John","class":6,"roll_no":23}
a=Student.items()
print(a)
##keys()#############################################################
b=Student.keys()
print(b)
##values()###########################################################
c=Student.values()
print(c)
##copy()##############################################################
d=Student.copy()
print(d)
##setdefault()########################################################
x=Student.setdefault("phone_no",123456789)
print(x)
print(Student)
##update()############################################################
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}

d1.update(d2)
print(d1)
##pop()###############################################################
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d.pop("Age")
##popitem()###########################################################
d3 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d3.popitem()
print(d3)

d3.popitem()
print(d3)
##clear()################################################################
d4 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d4.clear()
print(d4)
