from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
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
        # print(list)
        sorted.append(heap.remove())
    return sorted
