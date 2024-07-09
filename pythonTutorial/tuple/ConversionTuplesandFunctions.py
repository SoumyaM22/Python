a = ("Oneplus","Nokia","Redmi")
print("Before Conversion: ", a)

a = list(a)
print("After conversion: ", a)
a.append("Vivo")
print("After adding: ",a)

a= tuple(a)
print("Again conversion of a back: ",a)

#Functions
print(a.count("Nokia"))

print("the index of redmi is: ", a.index("Redmi"))