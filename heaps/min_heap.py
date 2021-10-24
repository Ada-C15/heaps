class HeapNode:

    # why isn't this __init__?
    # def initialize(self, key, value):
    #     self.key = key
    #     self.value = value

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
            value = key

        # creates new node
        node = HeapNode(key, value)
        # appends new node to end of store/list/heap (is 'store' the heap here?)
        self.store.append(node)
        # calls heap_up method which takes the last index in store as an argument
        self.heap_up(len(self.store) - 1)
        print(str(self))

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        # calls swap method which takes in an argument of the first index in store and the last index in store as arguments
        # this will swap the lowest value (root node) with the last value, which will be removed
        self.swap(0, len(self.store) - 1)
        # saves the min value to return, and removes it from the heap
        min = self.store.pop()
        # calls heap_down method which takes the first index of store as an argument
        # why do we need to do this?
        self.heap_down(0)

        return str(min)

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(n) (because you need to check the length of the store?)
            Space complexity: O(1)
        """
        if len(self.store) == 0:
            return True
        return False

    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than its parent node.
            It could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        # compare index of current node to index of parent
        # how do I find the parent node of the current index, without a linked list?

        # if it's less than the parent, swap the position of the nodes
        # use swap() helper method with the index of the current node and the index of the parent node
        # should this be solved with a while loop? or with recursion?
        parent = (index - 1)//2
        while self.store[parent].key > self.store[index].key:
            if parent == -1:
                break
            self.swap(parent, index)
            index = parent
            parent = (index - 1)//2

    def heap_down(self, index):
        """ This helper method takes an index and
            moves it up the heap if it's smaller
            than its parent node.
        """
        # in this method, index always starts at 0

        if (index >= len(self.store) - 1):
            return

        right_child = index * 2 + 2
        left_child = index * 2 + 1

        if (left_child > len(self.store) - 1):
            return

        if left_child < len(self.store):

            if right_child >= len(self.store) or self.store[left_child].key < self.store[right_child].key:
                min_node = left_child
            else:
                min_node = right_child

        if self.store[index].key > self.store[min_node].key:
            self.swap(index, min_node)
            self.heap_down(min_node)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
