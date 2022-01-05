class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)



class MinHeap:

    def __init__(self):
        self.store = []


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(logn)
            Space Complexity: O(n)
        """
        self.store.append(HeapNode(key, (value if value else key)))
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
        valueToRemove = self.store.pop()
        self.heap_down(0)

        return valueToRemove.value


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
    
        return len(self.store)==0

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(logn)
            Space complexity: O(1)
        """
        parentIdx = (index-1)//2
        while index>0 and self.store[index].key<self.store[parentIdx].key:
            self.swap(index,parentIdx)
            index=parentIdx
            parentIdx=(index-1)//2
        

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        childOneIdx = index*2+1
        childTwoIdx = childOneIdx+1

        if len(self.store)>childTwoIdx and self.store[childOneIdx].key>self.store[childTwoIdx].key:
            childOneIdx=childTwoIdx
            
        if len(self.store)<=childOneIdx:
            return None

        if self.store[childOneIdx].key<self.store[index].key:
            self.swap(index,childOneIdx)
            self.heap_down(childOneIdx)
        

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
