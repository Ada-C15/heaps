from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(n)
    """
    if len(list) <= 1:
        return list

    heap = MinHeap()
    for num in list:
        heap.add(num)

    sorted_list = []
    while heap.store:
        sorted_list.append(heap.remove())
    return sorted_list