import pandas as pd

dict = {"keys":["k1","k2","k1","k2"],
        "Names":["John","Ben","David","Peter"],
        "Houses":["Red","Blue","Green","Red"],
        "Grades":["3rd","8th","9th","8th"]}

df = pd.DataFrame(dict)
print(df)
print(df.pivot_table("Houses","keys","Names",aggfunc="first"))
print(df.pivot_table(["Houses","Grades"],"keys","Names",aggfunc="first"))