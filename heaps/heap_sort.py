

from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  o(n log n)
        Space Complexity: o(n)
    """

    heap = MinHeap()
    sorted_array = []

    for value in list:
        heap.add(value, value)

    while heap.store:
        sorted_array.append(heap.remove())

    return sorted_array
