import math
import time
from random import randint

# Alternativa 1 za predstavljanje heap-a
class Heap():
    def __init__(self):
        self.heap_size = 0
        self.elements = []
    def set_elements(self, elem):
        self.elements = elem[:]
        self.heap_size = len(self.elements)
    def set_heap_size(self, s):
        self.heap_size = s
    def get_heap_size(self):
        return heap_size
    def decrease_heap_size(self):
        self.heap_size -= 1

# Alternativa 2 za predstavljanje heap-a lista sa dva elementa
# gde je prvi element lista a drugi velicina heap-a

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def max_heapify(A,i,heap_size):
    l = left(i)
    r = right(i)
    largest = i
    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        # zameni najvece dete sa roditeljem
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        max_heapify(A, largest, heap_size)
    
def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)-1
    for i in range(len(A)-1, 0, -1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        max_heapify(A,0,heap_size)
        heap_size = heap_size - 1

def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def bucket_sort(A, print_buckets=False, heap_flag=False):
    M = max(A)
    n = len(A)
    # Fill buckets
    B = [[] for i in range(n)]
    for i in range(n):
        B[math.floor(int(A[i] / M *(n-1)))].append(A[i])
    
    if print_buckets:
        print(B)

    # Sort buckets
    for i in range(n):
        if heap_flag:
            heap_sort(B[i])
        else:
            insertion_sort(B[i])
    # Append results, buckets
    sorted_list = []
    for i in range(n):
        sorted_list += B[i]

    return sorted_list

def counting_sort(A, print_counts=False):
    maximum = max(A)
    array_size = len(A)
    C = [0 for i in range(maximum+1)]
    B = [0 for i in range(array_size)]
    # Count values
    for i in range(array_size):
        C[A[i]] += 1
    
    if print_counts:
        print(C)

    # Collect counts
    for i in range(1,maximum+1):
        C[i] += C[i-1]
    # Store values
    for i in range(array_size):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B

if __name__ == '__main__':
    #print(parent(2))
    #print(parent(3))
    #print(parent(4))
    #print(left(1))
    #print(right(1))
    l1 = [4, 5, 1, 2, 3, 7, 9, 11, 0]
    l2 = l1[:]
    l3 = l1[:]

    print("Heap sort")
    print(l1)
    heap_sort(l1)
    print(l1)
    
    print("Bucket sort")
    print(l2)
    l2 = bucket_sort(l2)
    print(l2)

    print("Counting sort")
    print(l3)
    l3 = counting_sort(l3)
    print(l3)

    l4 = [randint(0, 100) for i in range(50)]
    #print(l4)
    l5 = [1,1,1,1,1,1]
    #print(l5)
    
    l6 = l4[:]
    heap_sort(l6)
    print(l6)
    #print(counting_sort(l4))
    #print(bucket_sort(l4))
    #print(counting_sort(l5))
    