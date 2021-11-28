
from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    if not list:
        return [] 
    if len(list) == 1:
        return list

    heap = MinHeap()

    for item in list:
        heap.add(item)

    sorted = []

    while heap.store:
        # print(sorted)
        sorted.append(heap.remove())
    return sorted