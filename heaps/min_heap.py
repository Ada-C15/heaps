class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)
        
class MinHeap:
    def __init__(self):
        self.store = [] # this is the list where we store stuff

    def add(self, key, value = None):
        """ 
        This method adds a HeapNode instance to the heap
        If value == None the new node's value should be set to key
        Time Complexity: O(logn)
        Space Complexity: O(n)
        """
        if not value:
            value = key
        self.store.append(HeapNode(key, value))
        # we will append a new value to the end of the heap
        # Compare the new node with it's parent
        # If they are out of order swap and heap-up
        # using the parent's index number.
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ 
        This method removes and returns an element from the heap
        maintaining the heap structure
        Time Complexity: ?
        Space Complexity: ?
        """
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
        remove_val = self.store.pop()
        self.heap_down(0)

        return remove_val.value
    
    def __str__(self):
        """ 
        This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ 
        This method returns true if the heap is empty
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return len(self.store) == 0


    def heap_up(self, index):
        """
        This helper method takes an index and
        moves the corresponding element up the heap, if 
        it is less than it's parent node until the Heap
        property is reestablished.
        This could be **very** helpful for the add method.
        Time complexity: O()
        Space complexity: 0()
        """
        parent_index = (index-1)//2
        while index>0 and self.store[index].key < self.store[parent_index].key:
            self.swap(index,parent_index)
            index = parent_index
            parent_index = (index-1)//2

    def heap_down(self, index):
        """ 
        This helper method takes an index and 
        moves the corresponding element down the heap if it's 
        larger than either of its children and continues until
        the heap property is reestablished.
        than it's parent node.
        """

        childOne = index*2+1
        childTwo = childOne+1

        if len(self.store)>childTwo and self.store[childOne].key>self.store[childTwo].key:
            childOne=childTwo

        if len(self.store)<=childOne:
            return None

        if self.store[childOne].key<self.store[index].key:
            self.swap(index,childOne)
            self.heap_down(childOne)

    def swap(self, index_1, index_2):
        """
        Swaps two elements in self.store
        at index_1 and index_2
        used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp