import pandas as pd
import random
import math

# leitura do dataset
df = pd.read_csv("dataset/wine.csv", usecols=['WineID'], sep=',')

# embaralha o daframe
df_aleatorio = df.sample(frac=1).reset_index(drop=True)

# transforma o df em uma lista
V = df.values.flatten().tolist()

# transforma todo o df_aleatorio em uma lista única
V_aleatorio = df_aleatorio.values.flatten().tolist()

# vetor inversamente ordenado a partir do df original
V_inverso = sorted(V, reverse=True)

# cria uma cópia ordenada do vetor original e faz o embaralhamento de 5% das posições
V_quase_ordenado = sorted(V) # faz a ordenação
quantidade = math.ceil(len(V_quase_ordenado) * 0.05) # calcula 5% do tamanho
idx = random.sample(range(len(V_quase_ordenado)), quantidade) # sorteia índices aleatórios
valores = [V_quase_ordenado[i] for i in idx] # embaralha os elementos das posições
random.shuffle(valores)
# aplica de volta os valores embaralhados nas posições sorteadas
for idx, val in zip(idx, valores):
    V_quase_ordenado[idx] = val