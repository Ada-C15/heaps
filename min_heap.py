class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


# Min heap every node is smaller than its children. Min bubbles up
class MinHeap:

    def __init__(self):
        self.store = []

    def find_left_child(self, index):
        left_child = 2 * index + 1
        return left_child
    
    def find_right_child(self, index):
        left_child = 2 * index + 2
        return left_child
    
    def find_parent(self,index):
        parent_index = (index - 1) // 2
        return parent_index

        
    def check_for_right_child(self,index):
        left_child = self.find_left_child(index)
        if left_child == len(self.store) -1:
            return False
        return True 

    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: ?
        """
        new_node = HeapNode(key,value)
        self.store.append(new_node)
        self.heap_up(len(self.store)-1)
        

    # remove only the root node from heaps. swap root node with last node,then pop old root node off
    # heap down. check the root with children to check keys  
    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if len(self.store) == 0:
            return None
        else:
            self.swap(0,-1)
            min = self.store.pop()
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
            Time complexity: ?
            Space complexity: ?
        """
        if not self.store:
            return True
    

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        
        parent_index = self.find_parent(index)      
        while self.store[parent_index].key > self.store[index].key:
            # if index.key is less than parent.key we want to swap the nodes themselves, and swap the index pointers to find the new parent and new node to make a comparison to move up the heap
            if index == 0:
                break
            self.swap(index,parent_index)
            index = parent_index 
            parent_index = self.find_parent(parent_index)
            
            
    
    
    
    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        # index is the node being moving down the heap
        # index.key gets swapped with the smallest child 
        # check to see if the smallest child has a smallest child, this will let us know we are at the end. 
        # if there is no left child that means there is no right child since heaps move left to right
        left_child = self.find_left_child(index)
        right_child = self.find_right_child(index)
        if len(self.store) == 1: 
                return
        while left_child < len(self.store): #<-- means there is at least one left child
            has_right_child = self.check_for_right_child(index) #<-- returns true if there is a right child
            if not has_right_child: #<-- if right child doesnt exist, then left child is the smallest child
                smallest_child = left_child
            
            elif self.store[left_child].key <= self.store[right_child].key and self.store[index].key > self.store [left_child].key:
               smallest_child = left_child
            
            elif self.store[right_child].key < self.store[left_child].key and self.store[index].key > self.store[left_child].key:
                smallest_child = right_child
            else:
                break 
            
            self.swap(smallest_child,index)
            index = smallest_child
            left_child = self.find_left_child(index)
            right_child = self.find_right_child(index)
            
          
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp

    




            
        
    
