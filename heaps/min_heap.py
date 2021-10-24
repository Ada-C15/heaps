
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
            Space Complexity: O(log n)
        """
        new_heapnode = HeapNode(key, value)
        self.store.append(new_heapnode)
        index = len(self.store) - 1
        self.heap_up(index)
        return None

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty():
            return None
        
        last_index = len(self.store) - 1
        self.swap(0, last_index)
        removedItem = self.store.pop(last_index)
        self.heap_down(0)
        return removedItem.value

    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ?
            Space complexity: ?
        """
        return len(self.store) == 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        if index == 0:
            #base case
            return
        
        # Check if the index is odd or even to see whether it is left or right node
        # Find the parent index for the given index
        if index % 2 == 0: 
            #right node parent
            parent_index = int((index - 2) / 2)
        else:
            #left node parent
            parent_index = int((index - 1) / 2)
        
        if(parent_index < 0):
            return

        # If the current key is lower than the parent swap
        if self.store[parent_index].key > self.store[index].key:
            self.swap(parent_index, index)
            self.heap_up(parent_index)
        

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        # index is the last node so return immediately
        # as there is nothing to heap-down further
        if (index >= len(self.store)-1):
            return

        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2

        if (leftChildIndex > len(self.store)-1):
            return

        # gets the index of the child which has smallest key
        indexOfMinKeyChild = self.getIndexOfMinKeyNode(leftChildIndex, rightChildIndex)

        # if the current node key is larger than the min child node 
        # then swap current node with min child node
        if (self.store[index].key > self.store[indexOfMinKeyChild].key):
            self.swap(index, indexOfMinKeyChild)
            self.heap_down(indexOfMinKeyChild)

    def getIndexOfMinKeyNode(self, leftChildIndex, rightChildIndex):
        
        if (rightChildIndex > len(self.store)-1):
            return leftChildIndex

        if (self.store[leftChildIndex].key <= self.store[rightChildIndex].key):
            return leftChildIndex
        return rightChildIndex

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


# test

# heap = MinHeap()
# # Arrange
# key = 5
# value = "Pasta"

# # Act-assert (heap.add returns None)
# assert heap.add(key, value) == None