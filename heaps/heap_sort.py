from .min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    for elem in list:
        heap.add(elem)
    
    sorted_list = []
    while heap.store:
        elem = heap.remove()
        sorted_list.append(elem)
    
    return sorted_list