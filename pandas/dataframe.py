import pandas as pd

dataframe = pd.DataFrame()

print(dataframe.empty)

dictionary = {
    "Column 0": [0,1,2,3,4],
    "Column 1": ['a','b','c','d','e'],
    "Column 2": ['!','@','#','$','%']
}

somaDeDictionarys = [elemA + elemB for elemA, elemB in zip(dictionary['Column 0'], [10,10,10,10,10])]

print(somaDeDictionarys)

dataframe = pd.DataFrame(data=dictionary)

print(dataframe)
print(dataframe.columns)

#Adicionando Colunas no dataFrame
dataframe["Column 3"] = somaDeDictionarys

#Posicao em colunas má prática
print("\n\n Acessando valores da coluna direto utlizando dataFrame como matriz")
print(dataframe["Column 3"])
print(dataframe["Column 3"][3])
dataframe["Column 3"][3] = 0
print(dataframe)

#Posicao em colunas boa prática
print("\n\n Atributo At para localizar elementos em colunas e alterar valores")
print(dataframe.at[3,"Column 3"])
dataframe.at[3,"Column 3"] = 99
print(dataframe.at[3,"Column 3"])

#Posicao em linhas boa prática
print("\n\n Atributo Loc para localizar elementos em linhas e alterar valores")
print(dataframe.loc[1,"Column 2"])
dataframe.loc[1,"Column 2"] = "&"
print(dataframe.loc[1,"Column 2"])

