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
            Space Complexity: O(1)? O(log n)?
        """
        if value == None:
            value = key

        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(log n)
        """
        if len(self.store) == 0:
            return None

        caboose = len(self.store) - 1
        self.swap(0, caboose)
        smol = self.store.pop()
        
        self.heap_down(0)
        return smol.value

    
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
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(log n)
        """
        if index == 0:
            return

        parent = (index - 1) // 2
        store = self.store
        if store[parent].key > store[index].key:
            self.swap(parent, index)
            self.heap_up(parent)
        

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
        """
        children = index * 2
        lefty = children
        poncho = children + 1
        if lefty < len(self.store):
            if poncho < len(self.store):
                if self.store[lefty].key < self.store[poncho].key:
                    smol = lefty
                else:
                    smol = poncho
            else:
                smol = lefty
            
            if self.store[index].key > self.store[smol].key:
                self.swap(index, smol)
                self.heap_down(smol)

    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
