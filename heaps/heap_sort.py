from min_heap import MinHeap
from min_heap import HeapNode

def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n logn)
        Space Complexity: 0(1)
    """
    
    heap = MinHeap()   
    
    if not list:
        return[]
    # want smallest number in root, index 0
    for num in list: 
        heap.add(num)
        #heap.add(HeapNode(index,list[index])) <-- dont understand why we dont make instances of nodes?
        print(heap)
    index = 0
    while heap:
        list[index] = heap.remove()
        index += 1
        
    return list
    

  