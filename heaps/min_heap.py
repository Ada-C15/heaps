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
            
            Time Complexity: Adding an element to the heap is o(n) for the actual addition of the element to the end of the array.
            It is O(log n) for the heap_up process as it traverses the heap so overall it is a O(log n) operation. 
    
            Space Complexity: The space complexity is constant O(n) because only one new node is added at a time.
        """
        if value == None:
            value = key

        newNode = HeapNode(key,value)
        self.store.append(newNode)
        
        index_of_new_node = len(self.store) - 1
        self.heap_up(index_of_new_node)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            
            Time Complexity: Removing a node from the heap is O(n) for the process of swapping and popping it off the end. 
            But it increases to O(log n) for the process of traversing the heap to move the swapped root back down to it appropriate place in the heap. 
            Overall time complexity ios then O(log n).
            
            Space Complexity: The space complexity is constant O(1) becuase one element is popped off and saved to the variable removed_node
            each time a node is removed. 

        """
        if self.empty():
            return None
        
        #min_heap will always remove the smallest element b/c the removal is always from the root and the root 
        #in min_heap will always  be the smallest element

        heap_size = len(self.store) 

        index = 0
        
        if (index * 2) + 1 <= heap_size:
            self.swap(0, len(self.store)-1)
            removed_node = self.store.pop()
            self.heap_down(0)
        
        return removed_node.value


    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty

            Time complexity: O(1) constant because the method only needs to calculate the length of the array
            each time to perform its function and the en() function in Python runs in O(1) complexity.

            Space complexity: O(1) beacause only one new variable (heap_size) is created each time the function is called. 
        """
        heap_size = len(self.store)

        if heap_size == 0:
            return True
        return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.

            Time complexity: O(log n) because we do max 1 swap at each level of the heap.
            
            Space complexity: O(1) because a constant number (3) of variables are created in space each time. 
        """
        current_index = index
        parent_index = (index-1)//2
        heap_length =len(self.store)

        for i in range(len(self.store) -1, -1, -1):
            if i > 0:
                parent_index = (i-1)//2
                if self.store[i].key < self.store[parent_index].key:
                    self.swap(i, parent_index)
            continue

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        heap_size = len(self.store) - 1

        while (index * 2) + 1 <= heap_size:
            min_child_index = self.min_child(index)

            if min_child_index != index:
                
                if self.store[index].key > self.store[min_child_index].key:
                    self.swap(index, min_child_index)

                index = min_child_index      
            else:
                break
    def min_child(self, index):

        left_index = (index * 2) + 1
        right_index = (index * 2) + 2
        heap_size = len(self.store) - 1
        min_child_index = index

        if right_index > heap_size and left_index <= heap_size:
            if self.store[left_index].key < self.store[index].key:
                min_child_index = left_index
            
        elif right_index <= heap_size:
            if self.store[right_index].key < self.store[left_index].key:
                min_child_index = right_index
            else:
                min_child_index = left_index
        
        return min_child_index

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


#helper functions to optimize code with

    # def parent(self, index):
    #     return index//2

    # def leftChild(self, index):
    #     return (index * 2) + 1

    # def rightChild(self, index):
    #     return (index * 2) + 2

    # def leaf(self, index):
    #     heap_size = len(self.store)-1

    #     if index >= heap_size//2 and index <= heap_size:
    #         return True
    #     return False

    # def hasLeftChild(self, index):
    #     heap_size = len(self.store)
    #     left_index = index * 2 
    #     if left_index > heap_size and self.store[left_index] == None:
    #         return False
    #     return True

    # def hasRightChild(self, index):
    #     heap_size = len(self.store)
    #     right_index = (index * 2) + 1
    #     if self.store[right_index] == None and right_index > heap_size:
    #         return False
    #     return True