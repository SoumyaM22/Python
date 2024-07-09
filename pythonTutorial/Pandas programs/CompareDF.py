##pip install pandas - install using package manager in Terminal not console
##pip list - to check installed packages
import pandas as pd

dict = {"Fruits":["mango","apples","banana","papaya"],
        "Price":[100,150,50,35],
        "Quantity":[15,10,10,3]}

df1 = pd.DataFrame(dict)
print("DF1",df1)

df2 = df1.copy()

df2.loc[0,"Price"] = 120
df2.loc[1,"Price"] = 175
df2.loc[3,"Price"] = 30
df2.loc[0,"Quantity"] = 12
df2.loc[1,"Quantity"] = 15
df2.loc[3,"Quantity"] = 5
print("DF2",df2)

print(df1.compare(df2))
print("Align axis","\n",df1.compare(df2,align_axis=0))
print("Keep_equal=True","\n",df1.compare(df2,keep_equal=True)) #no difference
print("keep_shape=True","\n",df1.compare(df2,keep_shape=True))
#keep_shape=True, Values which remained same is displayed as NaN
print("keep_shape=False","\n",df1.compare(df2,keep_shape=False)) #By default keep_shape remains False