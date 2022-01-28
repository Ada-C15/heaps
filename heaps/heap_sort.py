from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  Onlogn
        Space Complexity: On
    """
    heap = MinHeap()
    sorted_list = []

    for item in list:
        heap.add(item)

    while not heap.empty():
        sorted_list.append(int(heap.remove()))
        
    return sorted_list