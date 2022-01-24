from heaps.min_heap import MinHeap

def heap_sort(list):
    """ 
        Time Complexity:  O(n log n)?
        Space Complexitty: O(n)?
    """
    listless = MinHeap()
    sorts= []

    for node in list:
      listless.add(node)
    
    for i in range(len(list)):
      nod = listless.remove()
      sorts.append(nod)
      
    return sorts
    