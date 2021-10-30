

from heaps.min_heap import MinHeap
from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  n * log n
        Space Complexity: ?
    """

    # Referenced solution from class
    heap = MinHeap()

    # add every element in list as node in heap
    for num in list:
        heap.add(num)

    index = 0
    # if they heap is not empty, remove each node to create an ordered list
    while not heap.empty():
        list[index] = heap.remove()
        index += 1

    return list