# Segunda Prova - Projeto de Pacotes Python

Este projeto demonstra a criação e uso de um pacote Python chamado `pacotes`, que contém funções para álgebra linear, geração de números aleatórios e operações básicas com listas.

## Estrutura do Projeto

```
segunda.prova/
│
├── proj_principal.py
└── pacotes/
    ├── __init__.py
    ├── alg_lin.py
    ├── basic.py
    └── random.py
```

## Funcionalidades

- **Álgebra Linear (`alg_lin.py`):**
  - `det(mat)`: Calcula o determinante de uma matriz.
  - `inv(mat)`: Calcula a inversa de uma matriz.
  - `autovalores(mat)`: Calcula os autovalores de uma matriz.

- **Números Aleatórios (`random.py`):**
  - `rand_vec(tam, seed=None)`: Gera um vetor de números aleatórios.
  - `rand_int(tam, min=0, max=100, seed=None)`: Gera inteiros aleatórios em um intervalo.
  - `escolher(lista, tam=3, seed=None)`: Seleciona elementos aleatórios de uma lista.

- **Operações Básicas (`basic.py`):**
  - `soma_lista(lista)`: Soma todos os elementos de uma lista.
  - `contar_pares(lista)`: Conta quantos elementos pares existem em uma lista.

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale o numpy, se necessário:
   ```
   pip install numpy
   ```
3. Execute o arquivo principal:
   ```
   python proj_principal.py
   ```
