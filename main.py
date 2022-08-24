import numpy as np

def buscar_pivo(L):
    if (np.nonzero(L)[0]).size == 0:
        return -1
    else:
        return np.nonzero(L)[1][0]

def encontrar_pivos_indices(mat):
    pivos = []
    for i in range(5):
        pivos.append(buscar_pivo(np.array(mat[i])))
    return pivos

mat = np.matrix([[0,5,2,7,8],[8,10,4,14,16],[0,0,0,0,0],[2,6,10,16,22],[3,5,8,9,15]]).astype(float)
print("Matriz original:\n",mat,"\n")

pivos_indices = encontrar_pivos_indices(mat)

linha_aux = 0
for i in range(5):
    linha_aux = linha_aux + 1
    if pivos_indices[i] == -1 and linha_aux < 5 and i < 5:
        m = mat.tolist()
        (m[i],m[linha_aux]) = (m[linha_aux],m[i])
        mat = np.matrix(m)
        pivos_indices = encontrar_pivos_indices(mat)

print(mat,"\n")

linha_aux = 0
for i in range(5): 
    if pivos_indices[i] > pivos_indices[linha_aux] and linha_aux < 5 and i < 5:
        m = mat.tolist()
        (m[i],m[linha_aux]) = (m[linha_aux],m[i])
        mat = np.matrix(m)
        pivos_indices = encontrar_pivos_indices(mat)
    linha_aux = linha_aux + 1

print(mat)