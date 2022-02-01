from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n)
        Space Complexity: O(n)
    """
    heaps_dont_lie = MinHeap()

    for num in list:
        heaps_dont_lie.add(num)

    i = 0
    while not heaps_dont_lie.empty():
        list[i] = heaps_dont_lie.remove()
        i += 1

    return list
    