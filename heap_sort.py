from heaps.min_heap import MinHeap
from heaps.min_heap import HeapNode

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    
    heap = MinHeap()   
    
    if not list:
        return[]
    # want smallest number in root, index 0
    for index in range(len(list)):
        heap.add(HeapNode(index,list[index]))
        
    heap.heap_down(0)
    

    return heap