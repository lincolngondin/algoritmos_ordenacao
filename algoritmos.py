import random

# Algoritmo merge sort
def MergeSort(vetor: list[int]):
    if len(vetor) > 1:
        merge(vetor, 0, len(vetor) - 1)

def merge(vetor, esquerda, direita):
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        merge(vetor, esquerda, meio)
        merge(vetor, meio + 1, direita)
        combinar(vetor, esquerda, meio, direita)

def combinar(vetor, esquerda, meio, direita):
    esquerda_temp = vetor[esquerda:meio + 1]
    direita_temp = vetor[meio + 1:direita + 1]

    i = j = 0
    k = esquerda

    while i < len(esquerda_temp) and j < len(direita_temp):
        if esquerda_temp[i] <= direita_temp[j]:
            vetor[k] = esquerda_temp[i]
            i += 1
        else:
            vetor[k] = direita_temp[j]
            j += 1
        k += 1

    while i < len(esquerda_temp):
        vetor[k] = esquerda_temp[i]
        i += 1
        k += 1

    while j < len(direita_temp):
        vetor[k] = direita_temp[j]
        j += 1
        k += 1
        
# quickSort utilizando pivô aleatório
def partition(A, p, r):
    index_aleatorio = random.randint(p, r)
    A[index_aleatorio], A[r] = A[r], A[index_aleatorio]
    x = A[r] # o pivô é um elemento aleatório e é movido para a última posição
    i = p - 1 # índice do menor elemento
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[j], A[i] = A[i], A[j]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
        return A

# quickSort utilizando median-of-three        
def median_of_three(A, p, r):
    meio = (p + r) // 2
    
    # encontra a mediana entre os três elementos
    if A[p] <= A[meio] <= A[r] or A[r] <= A[meio] <= A[p]:
        return meio
    elif A[meio] <= A[p] <= A[r] or A[r] <= A[p] <= A[meio]:
        return p
    else:
        return r
    
def partition_median(A, p, r):
    # obtém o índice da mediana dos três
    mediana_index = median_of_three(A, p, r)
    # faz a troca da mediana com o último elemento
    A[mediana_index], A[r] = A[r], A[mediana_index]
    x = A[r] # o pivô agora é a mediana na posição r
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[j], A[i] = A[i], A[j]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def quickSortMedian(A, p, r):
    if p < r:
        q = partition_median(A, p, r)
        quickSortMedian(A, p, q - 1)
        quickSortMedian(A, q + 1, r)
        return A