from heaps.min_heap import MinHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(nlogn) -- n for loop log n for heap sort
        Space Complexity: O(n)
    """
    sorted_list = []
    heap = MinHeap()

    for element in list:
        heap.add(element)
    for i in range(len(list)):
        min = heap.remove()
        sorted_list.append(min)
    return sorted_list
    
    
    