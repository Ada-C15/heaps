from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn)
        Space Complexity: O(n)
    """
    heap = MinHeap()

    for item in list:
        heap.add(item)

    i = 0
    while not heap.empty():
        list[i] = heap.remove()
        i += 1

    return list