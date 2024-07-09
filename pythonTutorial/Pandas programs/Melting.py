import pandas as pd

dict = {"Names":["John","Ben","David","Peter"],
        "Houses":["Red","Blue","Green","Red"],
        "Grades":["3rd","8th","9th","8th"]}

df = pd.DataFrame(dict)
print(df)
#print(pd.melt(df,id_vars=["Names","Grades"],value_vars=["Houses"]))
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="Values"))