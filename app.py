import pandas as pd
lista_numerica = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
lista_texto = [ 'Morango' , 'Python' , 'Sushi' ,'Batata' , 'Massa', 'Crocs', 'Sapo' , 'Quiabo' , 'Igreja' , 'Joaninha']

serie_numeros = pd.Series(lista_numerica)
serie_texto = pd.Series(lista_texto)

indice_alfabetico = [ 'A' , 'B' , 'C' ,'D' , 'E', 'F', 'G' , 'H' , 'I' , 'J']
serie_numeros.index = indice_alfabetico

serie_numeros = serie_numeros + 1

print("Serie Númerica completa")
print(serie_numeros)

print("Serie Alfabetica")
print(serie_texto)

print("\n 6 primeiro elemnetos a serie texto ")
print(serie_texto.head(6))


print("\n 7 ultimos elememtos da serie numeros ")
print(serie_numeros.tail(7))

dic_numeros = serie_numeros.to_dict()
dic_texto = serie_texto.to_dict()

print("\n dicionario  numerico")
print(dic_numeros)

print("\n Dicionário de Texto ")
print(dic_texto)

#df.loc[] -- SERVE PARA ACHAR ALGO NA QUELE INDICE  
#iloc() -- SERVE PARA CORTAR UM INDICE
#df.reset_index()-- SERVE PARA REORGANIZAR OS INDICES ex: 0, 1 o 0 vira 1 e o 1 vira 2
