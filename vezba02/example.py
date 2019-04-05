import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list
    
def insertion_sort(A):
   for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key: 
            A[j+1] = A[j] # move elements to right
            j -= 1
        A[j + 1] = key #insert element

def bubble_sort(A):
    array_size = len(A)
    for i in range(array_size):
        for j in range(array_size-i-1):
            if A[j] > A[j+1]:
                # swap elements
                A[j], A[j+1] = A[j+1], A[j]
   

def lin_search(A, value):
    index = -1
    for i in range(len(A)):
        if A[i] == value:
            index = i
            break
    return index

def binary_search(A, value):
    index = -1
    low_limit, upper_limit = 0,len(A)
    middle = len(A) // 2
    while low_limit != upper_limit:
        if value  == A[middle]:
            index = middle
            break
        elif value > A[middle]:
            low_limit = middle+1
        else:
            upper_limit = middle
        middle = (upper_limit + low_limit) // 2
    return index

#def bin_search_rec(A, low, high)

def test_lin_search(l, value):
    print("Test linear search")
    start_time = time.clock()
    index = lin_search(l, value)
    end_time = time.clock() - start_time
    print("Index " + str(index))
    print("Duration: ", end_time)

def test_bin_search(l, value):
    print("Test binary search")
    start_time = time.clock()
    index = binary_search(l, value)
    end_time = time.clock() - start_time
    print("Index " + str(index))
    print("Duration: ", end_time)

if __name__ == '__main__':
    l = random_list(1, 1000, 999)

    l1 = l
    print("Test insertion sort")
    start_time = time.clock()
    insertion_sort(l1)
    #print(l1)
    end_time = time.clock() - start_time
    print("Duration: ", end_time)

    l2 = l
    print("Test bubble sort")
    start_time = time.clock()
    bubble_sort(l2)
    #print(l2)
    end_time = time.clock() - start_time
    print("Duration: ", end_time)

    test_lin_search(l1, 999)
    test_bin_search(l1, 999)
    
    l3 = random_list(1, 100000, 99999)
    l3.sort()
    test_lin_search(l3, 99999)
    test_bin_search(l3, 99999)

    l3 = random_list(1, 100, 99)
    l3.sort()
    test_lin_search(l3, 5)
    test_bin_search(l3, 5)
    