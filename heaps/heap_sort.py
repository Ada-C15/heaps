from heaps.min_heap import MinHeap 
from heaps.min_heap import HeapNode

def heap_sort(list):
    """ This method uses a heap to sort an array.
    
        Time Complexity:  Adding to the heap O(n log n), removing from the heap is O(n log n), 
        total time complexity is O(n log n) + O(n log n) = O(n log n)

        Space Complexity: Space complexity is either constant O(1) because your always only creating one new list or O(n) 
        becuase the size of the new list created is dependent on the size of the list to be sorted. 
    """
    
    newHeap = MinHeap()
    sorted_list = []

    for element in list:
        newHeap.add(element)

    for i in range(len(newHeap.store)):
        element_to_add = newHeap.remove()
        sorted_list.append(element_to_add)
    
    return sorted_list