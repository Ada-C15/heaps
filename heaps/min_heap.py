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
            Time Complexity: O(log n)
            Space Complexity: O(n)
        """
        if (value == None):
            newHeapNode = HeapNode(key, key)
        else:
            newHeapNode = HeapNode(key, value)

        self.store.append(newHeapNode)
        index = len(self.store) - 1
        self.heap_up(index)
        return None

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        lastIndex = len(self.store) - 1
        self.swap(0, lastIndex)
        lastNode = self.store.pop(lastIndex)
        self.heap_down(0)
        return lastNode.value

    
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
        if len(self.store):
            return False
        return True


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        if index == 0:
            return

        parentNodeIdx = (index -1) // 2

        if parentNodeIdx < 0:
            return

        if index and (self.store[index].key < self.store[parentNodeIdx].key):
            self.swap(index, parentNodeIdx)
            self.heap_up(parentNodeIdx)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        if index >= len(self.store)-1:
            return

        leftChild = 2 * index + 1
        rightChild = 2 * index + 2

        if rightChild < len(self.store) and self.store[rightChild].key < self.store[leftChild].key:
            leftChild = rightChild

        if leftChild >= len(self.store):
            return None

        elif self.store[leftChild].key < self.store[index].key:
            self.swap(index, leftChild)
            self.heap_down(leftChild)


    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
