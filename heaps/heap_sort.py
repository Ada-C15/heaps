from .min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn) (Each add is log(n), n nodes must be added)
        Space Complexity: O(n)
    """

    heap = MinHeap()

    for item in list:
        heap.add(item)

    # Iterate through list by index and remove heap items to build sorted list in the original array
    for i in range(0, len(list)):
        list[i] = heap.remove()

    return list

    