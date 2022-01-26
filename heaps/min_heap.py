import math


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

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log(n)) : add tail is constant rebalancing is log(n)
            Space Complexity: O(N+1)
        """
        if value is not None:
            self.store.append((key, value))
        else:
            self.store.append((key, key))
        # Bubble up to re balance tree

        self.heap_up(len(self.store)-1)  # list -1 index is last in list (python)

        print(self.store)
        pass

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log(n)) : remove head and replace with tail is constant. re balancing is log(n)
            Space Complexity: O(1) :
        """
        if self.empty():
            return
        min = self.store[0]  # set aside root value
        self.store[0] = self.store[-1]  # Delete root value and replace with last node
        self.store.pop(-1)
        self.heap_down(0)  # re balance the tree from the root position
        return min[1]  # return value removed from heap


    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element[1]) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(nlogn)
            Space complexity: O(n)
        """
        if len(self.store) == 0:
            return True

        return False  # ?? implicit?


    # "Bubble up" to root
    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if
            it is less than it's parent node until the Heap
            property is reestablished.

            This could be **very** helpful for the add method.
            Time complexity: O(logn)
            Space complexity: O(n +1)
        """
        if index == 0:
            return

        if index == 1 or index == 2:
            parent_index = 0
        else:
            parent_index = int(math.ceil((index-2)/2))
            # if parent_index <= 1:
            #     parent_index = int(1)

        print("Parent")
        print(parent_index)
        print(type(parent_index))
        print("index")
        print(index)


        if self.store[int(parent_index)][0] > self.store[index][0]:
            self.swap(index, parent_index)
            self.heap_up(parent_index)

        return

    # "filter down" to child position.
    def heap_down(self, index):
        """ This helper method takes an index and
            moves the corresponding element down the heap if it's
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_index = (index*2)+1
        right_index = (index*2)+2

        if left_index >= len(self.store) or right_index >= len(self.store):
            return

        if self.store[left_index][0] < self.store[index][0]:
            self.swap(left_index, index)
            self.heap_down(index)

        elif self.store[right_index][0] < self.store[index][0]:
            self.swap(right_index, index)
            self.heap_down(index)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        print("Swapping ", index_1, " ", index_2)
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp