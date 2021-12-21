# from tests.test_min_heap import heap


class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

# 	https://github.com/Ada-C15/heaps

#   https://www.geeksforgeeks.org/min-heap-in-python/
#   https://www.educative.io/edpresso/what-is-the-repr-method-in-python

class MinHeap:

    def __init__(self):
        self.store = []
        self.size = 0
        self.FRONT = 1


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        if value == None:
            value = key
        node = HeapNode(key, value)
        
         # Need to increment size  
        self.size +=1
        self.store.insert(self.size, node)
        
        # use self when referring to method or attribute of the class
        self.heap_up(self.size-1)
        # self.heap_up(len(self.store)-1)
         

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """

        # take copy first
        # copy last one to position 1
        # modify size 
        #heapify
        # if len(self.store)== 0:
        #     return None
        if self.empty() == True:
            return None
        # self.swap(0,len(self.store) -1)
        
        min = self.store[self.FRONT]

        self.store[self.FRONT] = self.store[self.size-1]
        self.size -= 1
        self.heap_down(self.FRONT)
        # min returns object we need it to return value min.value
        return min.value



    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ?
            Space complexity: ?
        """
        if len(self.store)== 0:
            return True
    
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos

    def rightChild(self, pos):
        child_position = 2 * pos + 1
        if child_position < self.size:
            return child_position
        return None

    # Function that returns true if the passed
    # node is a leaf node if it is leaf node (no left and right children) then it does not have children, it is not a parent
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    
 


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        #self.store[index] value for the new node that we are adding
        #self.parent(index) is the value of the current parent/leaf - that may have its first child or second if child is smaller we need to swap
        current = index
        while self.store[current].key < self.store[self.parent(current)].key:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        # if not self.isLeaf(index):
        #     if (self.Heap[index].key > self.Heap[self.leftChild(index)].key or self.Heap[index].key > self.Heap[self.rightChild(index)].key):
                #call swap


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        # If the node is a non-leaf node and greater
        # than any of its child -- if it is a parent then
        #check right child if exists and check it's index and see if it is greater than or = the store.size 
        if not self.isLeaf(index):
            if self.rightChild(index) != None:

                if (self.store[index].key > self.store[self.leftChild(index)].key or self.store[index].key > self.store[self.rightChild(index)].key):
                
                # Swap with the left child and heapify
                # the left child
                    if self.store[self.leftChild(index)].key < self.store[self.rightChild(index)].key:
                        self.swap(index, self.leftChild(index))
                        self.heap_down(self.leftChild(index))

                    # Swap with the right child and heapify
                    # the right child
                    else:
                        self.swap(index, self.rightChild(index))
                        self.heap_down(self.rightChild(index))



    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
        """
        
        self.store[index_1], self.store[index_2] = self.store[index_2], self.store[index_1]

    # Function to build the min heap using
    # the minHeapify function
    def my_minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.heap_down(pos)

