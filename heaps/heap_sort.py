from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap_o_frogges = MinHeap()

    for num in list:
        heap_o_frogges.add(num)

    i = 0
    while not heap_o_frogges.empty():
        list[i] = heap_o_frogges.remove()
        i += 1
    
    return list 