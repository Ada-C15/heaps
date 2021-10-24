from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(log n)
        Space Complexity: O(n)
    """
    heap_store = MinHeap()
    sorted_list = []

    if len(list) == 0:
        return sorted_list

    for item in list:
        heap_store.add(item)

    while heap_store.size() > 0:
        item = heap_store.remove()
        sorted_list.append(int(item))

    return sorted_list

