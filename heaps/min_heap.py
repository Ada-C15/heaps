class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

class MinHeap:

    def __init__(self):
        self.store = []

    def find_left_child(self, i):
        return i * 2 + 1

    def find_right_child(self, i):
        return i * 2 + 2
        
    def find_parent(self, i):
        parent = (i - 1) // 2
        return parent

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(n)
        """
        if not value:
            value = key
        new_node = HeapNode(key, value)
        self.store.append(new_node)
        new_node_i = len(self.store) - 1
        self.heap_up(new_node_i)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        self.swap(0, len(self.store) -1)
        removed_element = self.store.pop()
        self.heap_down(0)

        return removed_element.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        return self.store == []


    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        parent = self.find_parent(index)
        while self.store[parent].key > self.store[index].key:
            if index == 0:
                break
            self.swap(index, parent)
            index = parent
            parent = self.find_parent(index)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        smallest_child = self.find_smallest_child(index)
        while smallest_child and index < len(self.store):
            if self.store[index].key > self.store[smallest_child].key:
                self.swap(index, smallest_child)
                self.heap_up(smallest_child)
                index = smallest_child
            smallest_child
            break

    def find_smallest_child(self, index):
        lc = self.find_left_child(index)
        rc = self.find_right_child(index)
        heap_length = len(self.store)
# The current node has no children (you're done)
        if lc >= heap_length and rc >= heap_length:
            return None
# The current node has 1 child (that child is the smallest child)
        if lc < heap_length and rc >= heap_length:
            smallest_child = lc
        elif rc < heap_length and lc >= heap_length:
            smallest_child = rc
# The current node has 2 children, (you need to figure out the index of the smallest)
        elif lc < heap_length and rc < heap_length:
            if self.store[lc].key <= self.store[rc].key:
                smallest_child = lc
            else:
                smallest_child = rc
        return smallest_child
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
