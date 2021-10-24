from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    heap = MinHeap()
    sorted_list = []

    if list == []:
        return sorted_list

    for item in list:
        heap.add(item)

    while heap.empty() is False:
        sorted_list.append(int(heap.remove()))

    return sorted_list
