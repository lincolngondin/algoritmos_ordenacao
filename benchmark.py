import sys
import time
import tracemalloc
from algoritmos import quickSort, MergeSort, quickSortMedian
from entradaDados import V_aleatorio, V_inverso, V_quase_ordenado

# Ajusta o limite de recursão para QuickSort em grandes vetores
sys.setrecursionlimit(10**6)

def medir_tempo_memoria(algoritmo, vetor):
    tracemalloc.start()
    inicio = time.time()
    if algoritmo == 'quickSort':
        quickSort(vetor, 0, len(vetor) - 1)
    elif algoritmo == 'quickSortMedian':
        quickSortMedian(vetor, 0, len(vetor) - 1)
    elif algoritmo == 'MergeSort':
        MergeSort(vetor)
    fim = time.time()
    mem_pico = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return fim - inicio, mem_pico / 1024 / 1024  # memória em MB

def benchmark_algoritmo(algoritmo, vetor, tamanhos, repeticoes=10):
    resultados = []
    for tamanho in tamanhos:
        tempos = []
        mems = []
        for _ in range(repeticoes):
            v = vetor[:tamanho].copy()
            tempo, mem = medir_tempo_memoria(algoritmo, v)
            tempos.append(tempo)
            mems.append(mem)
        tempo_medio = sum(tempos) / repeticoes
        mem_medio = sum(mems) / repeticoes
        resultados.append((tempo_medio, mem_medio))
    return resultados

if __name__ == "__main__":
    tamanhos = [10**5, 5*10**5, 10**6]
    cenarios = {
        "Aleatório": V_aleatorio,
        "Inverso": V_inverso,
        "Quase Ordenado": V_quase_ordenado
    }
    algoritmos = {
        "QuickSort": 'quickSort',
        "QuickSort Median": 'quickSortMedian',
        "MergeSort": 'MergeSort'
    }
    repeticoes = 10

    for nome_algoritmo, id_algoritmo in algoritmos.items():
        print(f"\n{'='*30}\n{nome_algoritmo}\n{'='*30}")
        for nome_cenario, vetor in cenarios.items():
            print(f"\nCenário: {nome_cenario}")
            resultados = benchmark_algoritmo(id_algoritmo, vetor, tamanhos, repeticoes)
            print(f"{'Tamanho':>10} | {'Tempo Médio (s)':>15} | {'Memória Média (MB)':>20}")
            for tam, (tempo, mem) in zip(tamanhos, resultados):
                print(f"{tam:>10} | {tempo:>15.5f} | {mem:>20.2f}")