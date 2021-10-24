from heaps.heap_sort import heap_sort

class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MinHeap:

    def __init__(self):
        self.store = []


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """
        new_heapnode = HeapNode(key, value)
        self.store.append(new_heapnode)
        index = len(self.store) - 1
        self.heap_up(index)
        return None

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.store.empty:
            return None
        
        last_index = self.store - 1
        self.swap(0, last_index)
        result = self.store.pop()

        while not self.store.empty:
            self.heap_down(0)
            result.value

    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ?
            Space complexity: ?
        """
        pass


    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        
        if index == 0:
            #base case
            return self.store
        
        # Check if the index is odd or even to see whether it is left or right node
        # Find the parent index for the given index
        if index % 2 == 0: 
            #right node parent
            parent_index = int((index - 2) / 2)
        else:
            #left node parent
            parent_index = int((index - 1) / 2)
        
        # If the current key is lower than the parent swap
        if self.store[parent_index].key > self.store[index].key:
            self.swap(parent_index, index)
            self.heap_up(parent_index)
        

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
        """
        child_index = index * 2

        #return if you reach the bottom of the tree
        if child_index > self.store.length -1:
            return
        
    


    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp


# test

# heap = MinHeap()
# # Arrange
# key = 5
# value = "Pasta"

# # Act-assert (heap.add returns None)
# assert heap.add(key, value) == None