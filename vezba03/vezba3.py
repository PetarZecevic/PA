import random
import time
import math

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def merge(array, start, middle, end):
    # Procedura koja spaja dva niza u jedan u rastucem poretku
    
    left, right = array[start:middle], array[middle:end]
    left.append(math.inf)
    right.append(math.inf)
    l_max, r_max = middle-start, end-middle
    i,j,k = 0,0,start
    
    while i < l_max or j < r_max:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

def merge_sort(array, start, end):
    if end-start > 1:
        middle = start+(end-start)//2
        merge_sort(array, start, middle)
        merge_sort(array, middle, end)
        merge(array, start, middle, end)
    
def quick_sort(array):
    length = len(array)
    if length == 0:
        return []
    elif length == 1:
        return [array[0]]
    else:
        left = []
        right = []
        pivot = array[length//2]
        for i in range(length):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
 
if __name__ == '__main__':
    l = random_list(1, 10000000, 999999)
    list1 = l
    #print("Before merge sort")
    #print(list1)
    #print("After merge sort")
    start_time = time.clock()
    merge_sort(list1, 0, len(list1))
    end_time = time.clock() - start_time
    #print(list1)
    print('Time: ' + str(end_time))
    
    list2 = l
    #print("Before quick sort")
    #print(list2)
    #print("After quick sort")
    start_time = time.clock()
    list2 = quick_sort(list2)
    end_time = time.clock() - start_time
    #print(list2)
    print('Time: ' + str(end_time))
    
