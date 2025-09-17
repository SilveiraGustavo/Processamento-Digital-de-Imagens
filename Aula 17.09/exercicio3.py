import numpy as np
import matplotlib.pyplot as plt

Matriz1 = np.random.randint(0,256,(6,6))
Matriz2 = np.random.randint(0,256,(6,6))
print("--------- Matriz 1 --------- \n", Matriz1)
print("--------- Matriz 2 --------- \n", Matriz2)

Soma = Matriz1 + Matriz2
print("--------- Soma das matrizes --------- \n", Soma)

Subtracao = Matriz1 - Matriz2
print("--------- Subtração das matrizes --------- \n", Subtracao)

Multiplicacao = Matriz1 * Matriz2
print("--------- Multiplicação das matrizes --------- \n", Multiplicacao)


fig, axs = plt.subplots(2, 3, figsize=(8, 6))

axs[0,0].imshow(Matriz1, cmap="gray")
axs[0,0].set_title("Imagem 1")

axs[0,1].imshow(Matriz2, cmap="gray")
axs[0,1].set_title("Imagem 2")

axs[0,2].imshow(Soma, cmap="gray")
axs[0,2].set_title("Soma")

axs[1,0].imshow(Subtracao, cmap="gray")
axs[1,0].set_title("Subtração")

axs[1,1].imshow(Multiplicacao, cmap="gray")
axs[1,1].set_title("Multiplicação")

# remover os eixos para ficar mais "limpo"
for ax in axs.flat:
    ax.axis("off")

plt.tight_layout()
plt.show()