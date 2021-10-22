
class HeapNode:


    def __init__(self, key, value):
        self.key = key
        self.value = value
        # self.left = none
        # self.right = none 

class MinHeap:

    def __init__(self):
        self.store = []
        # self.root = None

        # left_child = parent * 2 + 1
        
        # right_child = parent * 2 + 2
    
    # def dict(self):
        # return {'key': self.key, 'value': self.value}

    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        # min heap
        # [5, 10, 21, 11, 14, 25, 31]
        # [0,  1, 2,  3,  4,  5,  6]

        # append a node
        if value == None:
            value = key
        
        # adding it to the end of the heap if heap not empty 
        if self.empty():
            self.store.append(HeapNode(key,value))  
            return

        self.store.append(HeapNode(key, value))
        self.heap_up((len(self.store))- 1)

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
        return f"[{', '.join([str(element.value) for element in self.store])}]"


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
         # left_child = index * 2 + 1
        # right_child = index * 2 + 2
        parent_index = (index-1) // 2
        parent = self.store[parent_index] 
        new_node = self.store[index]
 
        while new_node.value < parent.value:
            self.swap(parent_index, index)
            new_node = self.store[parent_index] # updating where parent was 
            parent_index = (parent_index-1)//2 #  i = 0 # recalculation  new index  - figure out new parent
            parent = self.store[parent_index] # value of parent

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
