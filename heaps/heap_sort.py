
from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap = MinHeap()
    return_list = []

    for element in list:
        heap.add(element)

    while heap.empty() == False:
        return_list.append(heap.remove())

    return return_list