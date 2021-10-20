class HeapNode:

    def initialize(self, key, value):
        self.key = key
        self.value = value

class MinHeap:

    def __init__(self):
        self.store = []
        if not self.store:
            self.root = None
            
        else:
            self.root = self.store[0]

        # children nodes?
        # for i in range(len(self.store)):
        #     left_child = i * 2 + 1
        #     right_child = i * 2 + 2
        #     left_parent = i % 2 - 1
        
        #     right_child = i * 2 + 2
    

    # def dict(self):
        # return {'key': self.key, 'value': self.value}

    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        if value == None:
            value = key
        
        if self.empty:
            self.store = HeapNode(key, value)
            return

        # adding it to the end of the heap if heap not empty
        self.store.append(HeapNode(key, value))

        # # Compare the new node with it's parent
        parent_node = self.root
        # If they are out of order swap and heap-up
        # using the parent's index number.
        # Implementation not shown purposefully.
        # self.heap_up(self.store.length - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        pass


    
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
        return not self.store


    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        # # Compare the new node with it's parent
        if self.
        # If they are out of order swap and heap-up
        # using the parent's index number.
        # Implementation not shown purposefully.
        # self.heap_up(self.store.length - 1)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
        """
        pass

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
