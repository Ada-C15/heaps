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
        if not value:
            new_heapnode = HeapNode(key, key)
        else:
            new_heapnode = HeapNode(key, value)
        self.store.append(new_heapnode)
        index = len(self.store) - 1
        self.heap_up(index)
        return None

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        last_index = len(self.store) - 1
        self.swap(0, last_index)
        node_to_remove = self.store.pop(last_index)
        self.heap_down(0)
        return node_to_remove.value


    
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
        return len(self.store) == 0


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(n)
        """
        if index == 0:
            return index

        parent_node = (index - 1) // 2
        current_nodes = self.store
        if current_nodes[parent_node].key > current_nodes[index].key:
            self.swap(parent_node, index)
            self.heap_up(parent_node)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        current_nodes = self.store
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2

        if left_child_index < len(self.store):
            if right_child_index < len(current_nodes):
                if current_nodes[left_child_index].key < current_nodes[right_child_index].key:
                    node = left_child_index
                else:
                    node = right_child_index
            else:
                node = left_child_index

            if current_nodes[index].key > current_nodes[node].key:
                self.swap(index, node)
                self.heap_down(node)
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
