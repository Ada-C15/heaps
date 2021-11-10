from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    list_data = MinHeap()
    for item in list:
        list_data.add(item)

    sorted_list = []
    while not list_data.empty():
        sorted_list.append(list_data.remove())

    return sorted_list