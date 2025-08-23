from pacotes import det, inv, autovalores, rand_vec, rand_int, escolher, soma_lista, contar_pares

# Exemplo de álgebra linear
mat = [[3, 1], [1, 3]]
print("Matriz:", mat)
print("Determinante:", det(mat)) 
print("Inversa:\n", inv(mat))
print("Autovalores:", autovalores(mat))

# Exemplo de números aleatórios
print("\nVetor aleatório:", rand_vec(3, seed=42))
inteiros = rand_int(5, 10, 50, seed=42)
print("Inteiros aleatórios:", inteiros)
print("Amostra:", escolher(['X', 'Y', 'Z'], seed=42))

# Exemplo de operações básicas
print("Soma dos inteiros:", soma_lista(inteiros))
print("Quantidade de pares:", contar_pares(inteiros))