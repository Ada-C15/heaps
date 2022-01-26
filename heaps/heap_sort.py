from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n)
        Space Complexity: O(1)
    """
    heap = MinHeap()

    for num in list:
        heap.add(num)

    index = 0

    while not heap.empty():
        list[index] = heap.remove()
        index += 1
    return list