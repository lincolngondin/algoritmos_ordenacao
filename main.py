import random
import math
import time

# Algoritmo merge sort
def MergeSort(vetor: list[int]):
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
        
def QuickSort(vetor):
    quickSort(vetor, 0, len(vetor)-1)

def QuickSortMedian(vetor):
    quickSortMedian(vetor, 0, len(vetor)-1)


# Funcao que carrega o dataset e retorna a lista com o tamanho desejado
def carregarDataset(tamanho: int) -> list[int]:
    return [random.randint(1, tamanho) for _ in range(tamanho)]

# Funcao para o primeiro cenario, embaralha uma copia do vetor de entrada e retorna
def embaralharDataset(vetor: list[int]) -> list[int]:
    return random.sample(vetor, k=len(vetor))

# Funcao para o segundo ceneario, ordena uma copia do vetor, embaralha 5 porcento dele e retorna
def embaralhar5PorcentoDataset(vetor: list[int]) -> list[int]:
    n = len(vetor)
    copia = sorted(vetor)
    # cada troca afeta duas posicoes
    numTrocas = max(1, (n * 5) // 100 // 2)
    for _ in range(numTrocas):
        # Escolhe dois elementos aleatorios do vetor e troca eles
        i, j = random.sample(range(n), k=2)
        copia[i], copia[j] = copia[j], copia[i]
    return copia

# Funcao retorna uma copia inversamente ordenada do vetor
def inversamenteOrdenado(vetor: list[int]) -> list[int]:
    return sorted(vetor,reverse=True)

# Retorna o tempo de execução do algoritmo de entrada, mede apenas o tempo de execução,
# Faz uma copia interna do vetor, portanto não é necessario passar uma copia para ela.
def medirTempoExecucao(vetor, algoritmo):
    copia = vetor.copy()
    t1 = time.perf_counter()
    algoritmo(copia)
    t2 = time.perf_counter()
    return t2-t1
    

def compararTempos():
    tamanhos = [10**5, 5*(10**5), 10**6]
    for n in tamanhos:
        print(f"Para n = {n}:")
        dataset = carregarDataset(n)
        # Cenario 1: Vetor completamente aleatorio
        C1Dataset = embaralharDataset(dataset)
        C1tempoMergeSort = medirTempoExecucao(C1Dataset, MergeSort)
        C1tempoQuickSort = medirTempoExecucao(C1Dataset, QuickSort)
        C1tempoQuickSortMedian = medirTempoExecucao(C1Dataset, QuickSortMedian)
        
        print("    Cenario 1: Vetor completamente aleatorio:")
        print(f"    MergeSort: {C1tempoMergeSort}s")
        print(f"    QuickSort: {C1tempoQuickSort}s")
        print(f"    QuickSortMedian: {C1tempoQuickSortMedian}s")

        # Cenario 2: Vetor quase ordenado (embaralho em 5% das posições)
        C2Dataset = embaralhar5PorcentoDataset(dataset)
        C2tempoMergeSort = medirTempoExecucao(C2Dataset, MergeSort)
        C2tempoQuickSort = medirTempoExecucao(C2Dataset, QuickSort)
        C2tempoQuickSortMedian = medirTempoExecucao(C2Dataset, QuickSortMedian)

        print("\n    Cenario 2: Vetor quase ordenado:")
        print(f"    MergeSort: {C2tempoMergeSort}s")
        print(f"    QuickSort: {C2tempoQuickSort}s")
        print(f"    QuickSortMedian: {C2tempoQuickSortMedian}s")

        # Cenario 3: Vetor inversamente ordenado
        C3Dataset = inversamenteOrdenado(dataset)
        C3tempoMergeSort = medirTempoExecucao(C3Dataset, MergeSort)
        C3tempoQuickSort = medirTempoExecucao(C3Dataset, QuickSort)
        C3tempoQuickSortMedian = medirTempoExecucao(C3Dataset, QuickSortMedian)

        print("\n    Cenario 3: Vetor inversamente ordenado:")
        print(f"    MergeSort: {C3tempoMergeSort}s")
        print(f"    QuickSort: {C3tempoQuickSort}s")
        print(f"    QuickSortMedian: {C3tempoQuickSortMedian}s")

compararTempos()