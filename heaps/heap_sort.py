from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    list1 = MinHeap()
    list2 = []
    for j in list:
        list1.add(j)
    for _ in range(len(list1.store)):
        element = list1.remove()
        list2.append(element)
    return list2


