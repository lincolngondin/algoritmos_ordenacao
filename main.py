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


test()