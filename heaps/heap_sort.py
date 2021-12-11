from heaps.min_heap import *



def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  o.n
        Space Complexity: o.1
    """
    
    heap = MinHeap()

    list = [heap.add(num) for num in list]
    i = 0
    while not heap.empty():

        list[i] = heap.remove()
        i+=1
     
    return list

    
    

    

    

    



