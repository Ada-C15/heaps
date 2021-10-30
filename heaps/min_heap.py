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
        # append new node to back of list
        self.store.append(node)
        # compare last/newly appended node to its parent to see how far we need to flip them up
        self.heap_up(len(self.store) - 1)
        

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if len(self.store) == 0:
            return None
        
        # swap first and last elements in heap
        self.swap(0, len(self.store) - 1)
        # now our first element is at the end of the list to take out
        min = self.store.pop()
        # now fix the tree :D index 0 is now the node that was at the end of the list
        self.heap_down(0)

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

        child_node = index # current node, index_1
        index = (index - 1) // 2 # parent node, index_2

        # print("child_node index:", child_node)
        # print("index index:", index)
        # print("CHILD NODE KEY:", self.store[child_node].key)
        # print("LIST BEFORE: ", self.store)
        # print()

        while child_node >= 0 and index >= 0 and self.store[child_node].key < self.store[index].key:
            # print("INSIDE CHILD NODE KEY:", self.store[child_node].key)
            # print("INSIDE PARENT NODE KEY:", self.store[index].key)
            # print()
            # temp_parent = index
            self.swap(child_node, index)
            # print("TEMP PARENT: ", temp_parent)
            child_node = index
            index = ((child_node - 1) // 2)
            # print("NEW PARENT NODE: ", index)
  
        # print("LIST AFTER LOOP: ", self.store)
        # print()


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """

        left_child = index * 2 + 1
        right_child = index * 2 + 2

        # Referenced Jen's solution from class
        if left_child < len(self.store):
            
            # set min_child to left node  if there is no right child
            if right_child >= len(self.store):
                min_child = left_child
            elif self.store[left_child].key < self.store[right_child].key:
                min_child = left_child
            else:
                min_child = right_child
            
            if self.store[index].key > self.store[min_child].key:
                self.swap(index, min_child)
                self.heap_down(min_child)

        # # print("BEGINNING LIST: ", self.store[index])
        # while (self.store[index].key > self.store[left_child].key or
        # self.store[index].key > self.store[right_child].key) and index <= len(self.store) - 1:
        #     temp_parent = index
        #     temp_left = left_child
        #     temp_right = right_child

        #     print("BEGINNING LIST: ", self.store)
        #     print()
        #     print("PARENT NODE INDEX: ", index)
        #     print("PARENT NODE KEY: ",  self.store[index].key)
        #     print("LEFT CHILD INDEX: ", left_child)
        #     print("LEFT CHILD KEY: ",  self.store[left_child].key)
        #     print("RIGHT CHILD INDEX: ", right_child)
        #     print("RIGHT CHILD KEY: ",  self.store[right_child].key)
        #     print()

        #     # if right_child >= len(self.store)-1 and self.store[index].key > self.store[left_child].key:
        #     #     self.swap(index, left_child)
        #     #     index = temp_left
        #     #     self.heap_up(temp_left)
        #     #     # left_child = index * 2 + 1
        #     #     # right_child = index * 2 + 2
        #     if self.store[left_child].key < self.store[right_child].key:
        #         print("***INSIDE IF LEFT < RIGHT (BEFORE)")
        #         print("PARENT NODE INDEX: ", index)
        #         print("PARENT NODE KEY: ",  self.store[index].key)
        #         print("LEFT CHILD INDEX: ", left_child)
        #         print("LEFT CHILD KEY: ",  self.store[left_child].key)
        #         print("RIGHT CHILD INDEX: ", right_child)
        #         print("RIGHT CHILD KEY: ",  self.store[right_child].key)
        #         print()    

        #         self.swap(index, left_child)
        #         index = temp_left
        #         self.heap_up(temp_left)
        #         # left_child = index * 2 + 1
        #         # right_child = index * 2 + 2

        #         print("***INSIDE IF LEFT < RIGHT (AFTER)")
        #         print("PARENT NODE INDEX: ", index)
        #         print("PARENT NODE KEY: ",  self.store[index].key)
        #         print("LEFT CHILD INDEX: ", left_child)
        #         print("LEFT CHILD KEY: ",  self.store[left_child].key)
        #         print("RIGHT CHILD INDEX: ", right_child)
        #         print("RIGHT CHILD KEY: ",  self.store[right_child].key)
        #         print()    

        #     elif self.store[right_child].key < self.store[left_child].key:

        #         print("***INSIDE IF, LEFT < RIGHT (BEFORE)")
        #         print("PARENT NODE INDEX: ", index)
        #         print("PARENT NODE KEY: ",  self.store[index].key)
        #         print("LEFT CHILD INDEX: ", left_child)
        #         print("LEFT CHILD KEY: ",  self.store[left_child].key)
        #         print("RIGHT CHILD INDEX: ", right_child)
        #         print("RIGHT CHILD KEY: ",  self.store[right_child].key)
        #         print()  

        #         self.swap(index, right_child)
        #         index = temp_right
        #         self.heap_up(temp_right)
        #         # left_child = index * 2 + 1
        #         # right_child = index * 2 + 2

        #         print("***INSIDE IF, RIGHT < LEFT (AFTER)")
        #         print("PARENT NODE INDEX: ", index)
        #         print("PARENT NODE KEY: ",  self.store[index].key)
        #         print("LEFT CHILD INDEX: ", left_child)
        #         print("LEFT CHILD KEY: ",  self.store[left_child].key)
        #         print("RIGHT CHILD INDEX: ", right_child)
        #         print("RIGHT CHILD KEY: ",  self.store[right_child].key)
        #         print()
            
        #     # else:
        #     #     return

        #     print("LIST AT END OF WHILE LOOP: ", self.store)
        #     print()
        
        
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
