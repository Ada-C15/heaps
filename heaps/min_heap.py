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
            Space Complexity: O(1)
        """
        if value == None:
            value = key
        
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if len(self.store) == 0:
            return None

        self.swap(0, len(self.store) - 1)
        mini = self.store.pop()
        self.heap_down(0)

        return mini.value

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
        if len(self.store) == 0:
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
            return index
        parent_node = (index - 1) // 2

        if self.store[parent_node].key > self.store[index].key:
            self.swap(parent_node, index)
            self.heap_up(parent_node)       

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        current_size = self.store
        left_child = index * 2 + 1
        right_child = index * 2 + 2

        if left_child < len(current_size):
            if right_child < len(current_size):
                if current_size[left_child].key < current_size[right_child].key:
                    less = left_child
                else:
                    less = right_child
            else:
                less = left_child

            if current_size[index].key > current_size[less].key:
                self.swap(index, less)
                self.heap_down(less)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
