class HeapNode:
    def __init__(self, key, value):
        if not value:
            value = key
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


class MinHeap:
    def __init__(self):
        self.store = []

    def find_parent_index(self, index):
        """Returns node's parent index"""
        i_parent = (index - 1) // 2
        return i_parent

    def find_left_child_index(self, parent_index):
        """Returns nodes's left child index"""
        i_left_child = parent_index * 2 + 1
        return i_left_child

    def find_right_child_index(self, parent_index):
        """Returns node's right child index"""
        i_right_child = parent_index * 2 + 2
        return i_right_child

    def left_child_exists(self, index):
        return self.find_left_child_index(index) < (len(self.store))

    def right_child_exists(self, index):
        return self.find_right_child_index(index) < len(self.store)

    def add(self, key, value=None):
        """This method adds a HeapNode instance to the heap
        If value == None the new node's value should be set to key
        Time Complexity: O (log n)
        Space Complexity: O(n)
        """
        if self.empty():  # heap is empty, just append
            self.store.append(HeapNode(key, value))  # O(1)
            return

        self.store.append(HeapNode(key, value)) 
        self.heap_up(len(self.store) - 1)  # move up where it belongs

    def remove(self): 
        """This method removes and returns an element from the heap
        maintaining the heap structure
        Time Complexity: O(log n)
        Space Complexity: ?
        """
        if self.empty():  # heap is empty, return None
            return None

        self.swap(0, len(self.store) - 1)  # swaps NODEs
        root = self.store.pop()
        self.heap_down(0)  # fix the heap structure if needed
        return root.value  # returns removed (element at the root)

    def __str__(self):
        """This method lets you print the heap, when you're testing your 
        app."""
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"  

    def empty(self):
        """This method returns true if the heap is empty
        Time complexity: ?
        Space complexity: ?
        """
        return not self.store

    def heap_up(self, index):
        """This helper method takes an index and moves the corresponding 
        element up the heap, if it is less than it's parent node until 
        the Heap property is reestablished.
        Time complexity: ?
        Space complexity: ?
        """
        parent_index = self.find_parent_index(index)
        parent = self.store[parent_index]
        new_node = self.store[index]

        while new_node.key < parent.key and index > 0:  
            self.swap(parent_index, index)  # swap of NODES 
                    # index_1,     index_2
            # temp_par = parent_index
            # parent_index = index 
            # index = temp_par
            index = parent_index  # update index - new child
            # recalculation of parent index
            parent_index = self.find_parent_index(index) 
            parent = self.store[parent_index]

    def heap_down(self, index):
        """This helper method takes an index and moves the corresponding 
        element down the heap if it's larger than either of its children 
        and continues until the heap property is reestablished."""

        # THERE are NO CHILDREN
        if not self.left_child_exists(index):
            return

        while index < len(self.store): 
            # WE GOT TWO CHILDREN !!
            if self.left_child_exists(index) and \
                self.right_child_exists(index):
                lc_index = self.find_left_child_index(index)
                rc_index = self.find_right_child_index(index)

                # AND -- LEFT child THE SMALLEST
                if self.store[lc_index].key < self.store[rc_index].key:
                    if self.store[lc_index].key < self.store[index].key:
                        self.swap(lc_index, index)
                        index = lc_index
                    else:
                        return

                # AND -- RIGHT KID IS SMALLER
                else:
                    if self.store[rc_index].key < self.store[index].key:
                        self.swap(rc_index, index)  # swapping NODES 
                        index = rc_index
                    else:
                        return

            #  WE GOT AN ONLY CHILD (left child)
            elif self.left_child_exists(index):
                lc_index = self.find_left_child_index(index)  # left i
                if self.store[lc_index].key < self.store[index].key:
                    self.swap(lc_index, index)  # swapping NODES
                    index = lc_index
                else:
                    return

            elif not self.left_child_exists(index):
                # check that this is not out of range none will always 
                # be false
                return

    def swap(self, index_1, index_2):  # index_1= parent, i_2 = index
        """Swaps two elements in self.store
        at index_1 and index_2
        used for heap_up & heap_down
        """
        temp = self.store[index_1]  # saving parent
        self.store[index_1] = self.store[index_2]  # (now parent)
        self.store[index_2] = temp  # old parent is at bottom now child

