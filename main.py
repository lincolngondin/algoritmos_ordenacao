import random
import math

def mergeSort(vetor: list[int]):
    merge(vetor, 0, len(vetor)-1)

def merge(vetor: list[int], p, r):
    if r > p:
        q = math.floor((r + p) / 2)
        merge(vetor, p, q)
        merge(vetor, q+1, r)
        combinar(vetor, p, q, r)

def combinar(vetor: list[int], p, q, r):
    w = [0] * (r-p+1)
    i = p
    j = q+1
    t = 0
    for k in range(r-p+1):
        if i > q:
            t = 1
        else:
            if  j > r:
                t = 0
            else:
                if vetor[i] < vetor[j]:
                    t = 0
                else:
                    t = 1
        if t == 0:
            w[k] = vetor[i]
            i+=1
        else:
            w[k] = vetor[j]
            j+=1
    vetor[p:r+1] = w

def test():
    tries = 100
    for _ in range(tries):
        v = [random.randint(1, 10000) for _ in range(10000)]
        vc = v.copy()
        vc.sort()
        mergeSort(v)
        if v != vc:
            print("Algoritmo está errado!")
            return

# test()
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
        # não há return. Faz a alteração no próprio vetor

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
        # não há return. Faz a alteração no próprio vetor
        
# Exemplo de uso:
# V = [20, 30, 50, 1, 8, 5]
# quickSort(V, 0, len(V) - 1)
# W = [1, 5, 8, 5, 1, 2]
# quickSortMedian(W, 0, len(W) - 1)