import numpy as np

Matriz = np.random.randint(0, 101, (5, 5))
print("Matriz original. \n",Matriz)


# Encontrando o maior e o menor valor da matriz
Maior = np.max(Matriz)
print("Maior valor da matriz:", Maior)
Menor = np.min(Matriz)
print("Menor valor da matriz:", Menor)


# Encontrando a média dos valores da matriz 
Media = np.mean(Matriz)
print("Media dos valores da matriz:", Media)

Modificar_Matriz = np.where(Matriz > Media, 255, Matriz)
print("Matriz modificada. \n", Modificar_Matriz)
