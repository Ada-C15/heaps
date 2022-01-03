class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return str(self.value)


class MinHeap:

    def __init__(self):
        self.store = []
    
    def __len__(self):
        return len(self.store)


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if value == None:
            value = key
        newNode = HeapNode(key, value)
        self.store.append(newNode)
        last = len(self.store) - 1
        self.heap_up(last)
        

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None
        self.swap(0, len(self.store) - 1)
        min = self.store.pop()
        self.heap_down(0)
        return min.value

    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        if len(self.store) == 0:
            return True
        return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        if index == 0:
            return
        
        parentIndex = (index -1)//2
        if self.store[index].key < self.store[parentIndex].key:
            self.swap(index, parentIndex)
            self.heap_up(parentIndex)



    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
        """
        size = len(self.store)
        while True:
            l, r = index * 2 + 1, index * 2 + 2 
            if max(l, r) < size:
                if self.store[index].key < self.store[l].key and  self.store[index].key < self.store[r].key: break
                elif self.store[l].key > self.store[r].key:
                    self.swap(index, r)
                    index = r
                else:
                    self.swap(index, l)
                    index = l 
            elif l < size:
                if self.store[l].key < self.store[index].key:
                    self.swap(index, l)
                    index = l
                else: break
            elif r < size:
                if self.store[r].key < self.store[index].key:
                    self.swap(index, r)
                    index = r
                else: break
            else: break
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp



