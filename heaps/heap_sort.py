

from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    heap = MinHeap()
    for i in list:
        heap.add(i)
    
    data = []

    while not heap.empty():
        data.append(heap.remove())

    return data