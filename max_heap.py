import math


A = [16, 14, 10, 8 , 7 ,9, 3, 2, 4,1]

def Parent(i):
    return math.floor(i/2);

def Left(i):
    return 2 * i;

def Right(i):
    return (2*i) + 1


def Max_Heapify(A, i):
    l = Left[i]
    r = Right(i)
    if l<= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
        
    if r<=A.heap_size and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        [A[i], A[largest]]  = [A[largest], A[i]]
        Max_Heapify(A,largest) 

def build_max_heap(A, n):
    A.heap_size = n
    i = math.floor(n/2)
    for i in range(l):
        Max_Heapify(A, i)
    
    
build_max_heap(A, 10)