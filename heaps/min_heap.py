class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
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
            self.store.append(HeapNode(key, key))
        else:
            self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None
        data = self.store[0].value
        self.store[0] = self.store[len(self.store) - 1]
        self.store.pop()

        self.heap_down(0)
        return data


    
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
        else:
            return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node,
            until the heap property is restablished.
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        parent_index = (index - 1) // 2
        if self.store[index].key < self.store[parent_index].key:
            self.swap(parent_index, index)
            if parent_index != 0:
                self.heap_up(parent_index)
            

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it down the heap if it's larger
            than either of its children and continues
            until the heap property is restablished.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        child_left_index = (index * 2) + 1
        child_right_index = (index * 2) + 2

        if child_left_index >= len(self.store):
            return

        target_index = child_left_index
        if child_right_index < len(self.store) and self.store[child_left_index].key > self.store[child_right_index].key:
            target_index = child_right_index
        
        if self.store[index].key > self.store[target_index].key:
            self.swap(index, target_index)
            self.heap_down(target_index)
        

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
