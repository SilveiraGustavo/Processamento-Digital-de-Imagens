import numpy as np

# Criar uma matriz binária 6x6
matriz = np.random.randint(0, 2, (6, 6))
print("Matriz binária 6x6:\n", matriz)

# Escolher um pixel (linha 3, coluna 4 -> índice (2,3))
r, c = 2, 3
print(f"\nPixel escolhido: ({r},{c}) valor={matriz[r,c]}")

# Vizinhos-4 (cima, baixo, esquerda, direita)
vizinhos4 = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
vizinhos4 = [(i,j) for i,j in vizinhos4 if 0 <= i < 6 and 0 <= j < 6]
print("Vizinhos-4:", vizinhos4)

# Vizinhos-8 (inclui diagonais)
vizinhos8 = [(r+i, c+j) for i in (-1,0,1) for j in (-1,0,1) if not (i==0 and j==0)]
vizinhos8 = [(i,j) for i,j in vizinhos8 if 0 <= i < 6 and 0 <= j < 6]
print("Vizinhos-8:", vizinhos8)

# Verificar se dois pixels estão na mesma região (conectividade-4)
from collections import deque

def mesma_regiao(matriz, p1, p2):
    if matriz[p1] == 0 or matriz[p2] == 0:
        return False
    fila = deque([p1])
    visitados = {p1}
    while fila:
        r,c = fila.popleft()
        if (r,c) == p2:
            return True
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:  # conectividade 4
            nr, nc = r+dr, c+dc
            if 0 <= nr < 6 and 0 <= nc < 6 and matriz[nr,nc] == 1 and (nr,nc) not in visitados:
                visitados.add((nr,nc))
                fila.append((nr,nc))
    return False

pA = (2,3)
pB = (4,3)
print(f"\n({pA}) e ({pB}) estão na mesma região? {mesma_regiao(matriz, pA, pB)}")
