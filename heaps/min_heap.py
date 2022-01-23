# from tests.test_min_heap import heap


from lib2to3.pytree import Node


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
        self.size = 0
        self.FRONT = 0


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(1)   not counting heap_up
            Space Complexity: O(1) not counting heap_up
        """
        if value == None:
            value = key
        node = HeapNode(key, value)
        print(node)

        
         # Need to increment size  
        self.store.insert(self.size, node)
        self.size +=1
        
        # use self when referring to method or attribute of the class
        self.heap_up(self.size-1)
         

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(1)   not counting heap_down
            Space Complexity: O(1) not counting heap_down
        """

        # take copy first
        # copy last one to position 1
        # modify size 
        # heapify
        
        if self.empty() == True:
            return None
        
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
            Time complexity: O(1)
            Space complexity: O(1)
        """
        if len(self.store)== 0:
            return True
    
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        if pos == 0:
            return 0

        return (pos-1)//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        child_position =  2 * pos + 1
        if child_position < self.size:
            return child_position
        return None

    # Function to return the position of
    # the right child for the node currently
    # at pos

    def rightChild(self, pos):
        child_position = 2 * pos + 2
        #maybe add to left child
        if child_position < self.size:
            return child_position
        return None

    # Function that returns true if the passed
    # node is a leaf node if it is leaf node (no left and right children) then it does not have children, it is not a parent
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos < self.size:
            return True
        return False

    

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: log(n) only takes one path
            Space complexity: O(1) not creating anything
        """
        #self.store[index] value for the new node that we are adding
        #self.parent(index) is the value of the current parent/leaf - that may have its first child or second if child is smaller we need to swap
        current = index
        while self.store[current].key < self.store[self.parent(current)].key:
            self.swap(current, self.parent(current))
            current = self.parent(current)
            # I don't think I am checking the whether the right key is bigger than the left.  
            
    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.

            Time complexity: log(n) only takes one path
            Space complexity: O(1) not creating anything
        """
        # If the node is a non-leaf (not a leaf) node and greater
        # than any of its child -- if it is a parent then
        #check right child if exists and check it's index and see if it is greater than or = the store.size 

        #keep looping while given index current = index > value of it's children so check both children
        current = index
        # check if current if a leaf node

        hasLeftChild =  self.leftChild(current) is not None
        hasRightChild =  self.rightChild(current) is not None


        #see if it has both children
        #compare and swap with the smaller

        while (hasLeftChild and (self.store[current].key > self.store[self.leftChild(current)].key)) or (hasRightChild and (self.store[current].key > self.store[self.rightChild(current)].key)):
            if hasLeftChild and hasRightChild:
                if self.store[self.leftChild(current)].key > self.store[self.rightChild(current)].key: 
                    self.swap(current, self.rightChild(current))
                    current = self.rightChild(current)
                else:
                    self.swap(current, self.leftChild(current))
                    current = self.leftChild(current)

            else:
                self.swap(current, self.leftChild(current))
                current = self.leftChild(current)
                print('left child:', current)
           
            hasLeftChild =  self.leftChild(current) is not None
            hasRightChild =  self.rightChild(current) is not None

    
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
    # range(start, stop[, step])
    def my_minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.heap_down(pos)
    
    