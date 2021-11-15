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
        self.store = [] # Intializing our empty heap


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Worst case would be if curr node is smaller than every other parent node such that it becomes the new root, causing a full traversel of the tree's height, which is log(n)
            Space Complexity: 0(1)
        """
        if value == None:
            value = key

        # Add curr node to the bottom of the tree
        curr_node = HeapNode(key, value)
        self.store.append(curr_node)

        # Keep swapping until a smaller parent node is found
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns a smollest_frogge from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: 0(1)
        """
        if len(self.store) == 0:
            return

        self.swap(0, len(self.store)-1)

        smollest_frogge = self.store.pop()

        self.heap_down(0)

        return smollest_frogge.value


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
        return len(self.store) == 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than its parent node until the Heap
            property is reestablished.

            Time complexity: O(log n)
            Space complexity: 0(1)
        """
        if index == 0:
            return index

        parent_node = (index - 1) // 2

        if self.store[parent_node].key > self.store[index].key:
            self.swap(parent_node, index)
            self.heap_up(parent_node)



    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding frogge down the heap if it's 
            larger than either of its children frogges and continues until
            the heap property is reestablished.
        """
        frogge_heap = self.store
        l_child_frogge = (2*index) + 1
        r_child_frogge = (2*index) + 2

        if l_child_frogge < len(frogge_heap):
            if r_child_frogge < len(frogge_heap):
                if frogge_heap[l_child_frogge].key < frogge_heap[r_child_frogge].key:
                    smoller_frogge = l_child_frogge
                else:
                    smoller_frogge = r_child_frogge
            else:
                smoller_frogge = l_child_frogge

            if frogge_heap[index].key > frogge_heap[smoller_frogge].key:
                self.swap(index, smoller_frogge)
                self.heap_down(smoller_frogge)
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        index_1_store = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = index_1_store
