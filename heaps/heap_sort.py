

def heap_sort(list):
    """ This method was supposed to use a heap instance to sort an array. But here we are.
        sources: 
        https://towardsdatascience.com/data-structure-heap-23d4c78a6962
        Time Complexity:  O(n log n)?
        Space Complexity: O(n log n) bc not in place? O(1) if I had figured out how to do it correctly
    """
    i = 0
    sorted = []

    def min_heap_sort(list, i):
      smol = i
      lefty = 2 * i + 1
      poncho = 2 * i + 2
      length = len(list) - 1
      
      if lefty <= length and list[i] > list[lefty]:
            smol = lefty
      if poncho <= length and list[smol] > list[poncho]:
            smol = poncho
      if smol != i:
            list[i], list[smol] = list[smol], list[i]
            min_heap_sort(list, smol)
      
    for i in reversed(range(len(list)//2)):
      min_heap_sort(list, i)

    for i in range(len(list)):
      list[0], list[-1] = list[-1], list[0]
      sorted.append(list.pop())
      min_heap_sort(list, 0)

    return sorted