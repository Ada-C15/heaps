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
            Time Complexity: ?
            Space Complexity: ?
        """
        # check for value, if there is no value -> value of the new node should be set to key
        if value is None:
            value = key
        
        # if there is a value
        # create a node variable and add the node to the heap -> store/storage
        node = HeapNode(key, value)
        self.store.append(node)

        # call heap_up (helper method) to ensure all nodes in heap are in the correct position
        # checking the value of the appended node against it's parent node 
        self.heap_up(len(self.store) - 1)
        

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        # check if the heap is empty (call empty helper) -> if it's empty, there's  nothing to remove
        if self.empty():
            return None
        
        # if the heap isn't empty, swap the root with the last index
        self.swap(0, len(self.store) - 1)
        # pop the root node, store this in a variable
        minimum = self.store.pop()

        # continue heaping down, starting from the root
        self.heap_down(0)

        # return the value of the var that was popped (the root)
        return minimum.value

    
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
        # this will return a boolean depending on if the length of store/storage is 0
        # if store == 0 --> the heap is empty 
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
            return index 

        # find the parent index
        parent_index = (index - 1) // 2

        # check if the current index's key is larger than it's parent index's key
        # if it is --> need to initiate a swap b/c the indexes are not in correct position
        if self.store[parent_index].key > self.store[index].key:
            # call swap helper method to switch the position's of the parent index and the current index
            self.swap(parent_index, index)
            # continue heaping up to ensure that all node's are in the correct position
            self.heap_up(parent_index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        heap_arr = self.store

        left_child = index * 2 + 1
        right_child = index * 2 + 2

        if left_child < len(heap_arr):
            if right_child < len(heap_arr):
                if heap_arr[left_child].key < heap_arr[right_child].key:
                    smallest_child = left_child
                else:
                    smallest_child = right_child
            else:
                smallest_child = left_child

            if heap_arr[index].key > heap_arr[smallest_child].key:
                self.swap(index, smallest_child)
                self.heap_down(smallest_child)
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

