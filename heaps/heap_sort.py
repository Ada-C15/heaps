
def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  ?
        Space Complexity: ?
    """
    
    if not list: 
        return []

    i = 0

    heap_list = []

    while list:
        smallest = min(list)
        heap_list.append(smallest)
        list.remove(smallest)
    
    return heap_list

    
    

    

    

    



