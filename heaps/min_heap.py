class HeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

# We begin our implementation of a binary heap with the constructor. 
# Since the entire binary heap can be represented by a single list, 
# we could make it so that
# all the constructor will do is initialize the list and an attribute currentSize to track the current size of the heap.
# class BinHeap:
#     def initialize(self):
#         self.heapList = [0] # the zero is there so that simple integer division 
#         self.currentSize = 0
class MinHeap:
    def __init__(self):
        self.store = [] # this is the list where we store stuff

    def parent():
    
    def find_left_child():

    def find_right_child():
        
    

    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(logn)
            Space Complexity: O(n)
        """
        self.store.append(HeapNode.new(key,value))
    # we will append a new value to the end of the 
    # Compare the new node with it's parent
    # If they are out of order swap and heap-up
    # using the parent's index number.
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """

        if self.store.empty?
        return nil

        self.swap(0, self.store.last - 1)
        result = self.store.pop()

    
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
        pass


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        while self.store[parent].key > self.store[index].key:
            if index == 0:
                break
            self.swap(index, parent)
            index = parent
            parent = self.find_parent(index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            than it's parent node.
        """
        smallest_child = self.find_smallest_child(index)
        if smallest_child and index < len(self.store):
            if self.store[index].key > self.store[smallest_child].key:
            
        # start heap_down with the root (index 0)
        lc = self.find_left_child(index)
        rc = self.find_right_child(index)
        while not self.store[index].key <= self.store[lc].key or not self.store[index].key <= self.store[rc].key:
            if self.store[index].key > self.store[lc].key and self.store[lc].key
                smallest_child = lc
            else:
                smallest_child = rc
            self.swap(smallest_child, index)
            index = smallest_child
            lc = self.find_left_child(index)
            rc = self.find_right_child(index)
            if lc > len(self.store)-1 or rc > len(self.store)-1:
                break
            return

        #self.heap_down(0) unless self.store.empty?
        #return result

        while (i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp
        i = mc


    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
