from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O log(n)
        Space Complexity: O (1)    """
    heap = MinHeap()
    # adding element in list
    for elem in list:
        heap.add(elem)

    sorted_list = []
    while heap.store:
        # remove
        elem = heap.remove()
        # append sorted element
        sorted_list.append(elem)

    return sorted_list
