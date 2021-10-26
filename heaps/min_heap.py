class HeapNode:
    def __init__(self, key, value):
        if value == None:
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
        Time Complexity: ?
        Space Complexity: ?
        """
        if self.empty():  # heap is empty, just append
            self.store.append(HeapNode(key, value))
            return

        self.store.append(HeapNode(key, value))  # add it to the end
        self.heap_up(len(self.store) - 1)  # move up in the list last elem where it belongs

    def remove(self):  # added index
        """This method removes and returns an element from the heap
        maintaining the heap structure
        Time Complexity: ?
        Space Complexity: ?
        """
        if self.empty():  # heap is empty, return None
            return None

        self.swap(0, len(self.store) - 1)  # swaps NODE at root for node at last index
        root = self.store.pop()
        self.heap_down(0)  # fix the heap if needed
        return root.value  # returns removed (element that was at the root)

    def __str__(self):
        """This method lets you print the heap, when you're testing your app."""
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"  # '['2', '3', '6']'

    def empty(self):
        """This method returns true if the heap is empty
        Time complexity: ?
        Space complexity: ?
        """
        return not self.store

    def heap_up(self, index):
        """This helper method takes an index and moves the corresponding element up the heap, if it is less than it's parent node until the Heap property is reestablished.
        Time complexity: ?
        Space complexity: ?
        """
        parent_index = (index - 1) // 2
        parent = self.store[parent_index]
        new_node = self.store[index]

        while new_node.key < parent.key and index > 0:  # self.root
            self.swap(parent_index, index)  # swap of NODES happens 
            # need to update index - bc new node was were parent index was
            temp_parent_index = (parent_index)
            index = temp_parent_index  # new child
            # recalculation of parent index
            parent_index = (parent_index - 1) // 2  # recalculation of new node's parent index
            parent = self.store[parent_index]  # value of parent

    # Heap down algorithm
    #  no childrend I don't do anything

    # only left child
    # check if parent is smaller you just swap

    # case 3 2 children
    # if right and left child
    # compare values of left and right children

    def heap_down(self, index):
        """This helper method takes an index and moves the corresponding element down the heap if it's larger than either of its children and continues until the heap property is reestablished."""

        # THERE are NO CHILDREN
        if self.left_child_exists(index) == False:
            return

        while index < len(self.store):  # and self.find_left_child_index(index)
            # WE GOT TWO CHILDREN !!
            if self.left_child_exists(index) and self.right_child_exists(index):
                lc_index = self.find_left_child_index(index)
                rc_index = self.find_right_child_index(index)

                # AND -- LEFT child THE SMALLEST
                if self.store[lc_index].key < self.store[rc_index].key:
                    if self.store[lc_index].key < self.store[index].key:
                        self.swap(lc_index, index) 
                        index = lc_index
                        # not_used_i, index = self.index_swap(lc_index, index)
                        print(f' if left child small, new index of parent {index}')
                    else:
                        return

                # AND -- RIGHT KID IS SMALLER 
                # elif self.store[lc_index].key > self.store[rc_index].key:
                else:
                    if self.store[rc_index].key < self.store[index].key:
                        self.swap(rc_index, index)  # SWAPING NODES, root node down
                        #  update where we are at in the array / heap level and index
                        # index = rc_index
                        index = rc_index
                        # not_used_i, index = self.index_swap(rc_index, index)
                        print(f' if left child small, new index of parent {index}')
                
                    else:
                        return

            #  WE GOT AN ONLY CHILD (left child)
            elif self.left_child_exists(index):
                lc_index = self.find_left_child_index(index) # find it's index
                if self.store[lc_index].key < self.store[index].key:
                    self.swap(lc_index, index)  # SWAPING NODES 
                    #  update where we are at in the array / heap level and index
                    index = lc_index
                    print(f' if  only left child exist, new index of parent {index}')
                else:
                    return

            elif not self.left_child_exists(index):
                # check that this is not out of range none will always be false
                return


    def swap(self, index_1, index_2):
        """Swaps two elements in self.store
        at index_1 and index_2
        used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
        print("***swap NODES function happening here***")
        print("-------after swap ------")
        print(
            f"new_parent = {self.store[index_1].key},{self.store[index_1].value} new_child= {self.store[index_2].key},{self.store[index_2].value}"
        )

    def index_swap(self, index_1, index_2):
        """Swaps two elements in self.store
        at lc_index and index
        used for heap_up & heap_down
        """
        
        index = index_1
        updated_index_1 = index_2 
        # updated position of parent
        updated_index_2 = index
        return updated_index_1, updated_index_2






    # def heap_down(self, index):
    #     """This helper method takes an index and moves the corresponding element down the heap if it's larger than either of its children and continues until the heap property is reestablished."""
    #     #  BALANCING THE HEAP yeah~!

    #     # THERE are NO CHILDREN
    #     if self.left_child_exists(index) == False:
    #         return

    #     # we haven't made it to the end of the list
    #     print(f"index moving down = {index}")

    #     while index < len(self.store):  # and self.find_left_child_index(index)

    #         # WE GOT TWO CHILDREN !!
    #         if self.left_child_exists(index) and self.right_child_exists(index):
    #             lc_index = self.find_left_child_index(index)
    #             rc_index = self.find_right_child_index(index)
    #             print("------------------------------------")
    #             print(f"lc_index = {lc_index}, rc_index = {rc_index}")

    #             # AND THE LEFT OF THOSE TWO IS THE SMALLEST KID
    #             if self.store[lc_index].key < self.store[rc_index].key:
    #                 print("----LEFT child THE SMALLEST----")
    #                 print(
    #                     f"left child key = {self.store[lc_index].key}, right child key = {self.store[rc_index].key}"
    #                 )
    #                 if self.store[lc_index].key < self.store[index].key:
    #                     self.swap(
    #                         lc_index, index
    #                     )  # SWAPING NODES our node root has gone down
    #                     # self.swap_index(lc_index, index)
    #                     index = lc_index
    #                     print("updating where node is now by swaping indices")
    #                     print(f"new index = {index}, swapped lc_index = {lc_index}")
    #                     # return index

    #             # THE RIGHT KID IS SMALLER THAN THE LEFT
    #             else:  # self.store[lc_index] > self.store[rc_index]
    #                 if self.store[rc_index].key < self.store[index].key:
    #                     self.swap(
    #                         rc_index, index
    #                     )  # SWAPING NODES our node root has gone down
    #                     #  need to update where we are at in the array / heap level and index
    #                     self.swap_index(rc_index, index)
    #                     index = rc_index
    #                     print("updating where node is now by swaping indices")
    #                     print(f"new index = {index}, swapped lc_index = {rc_index}")
    #                     # return index

    #         #  WE GOT AN ONLY CHILD (left child)
    #         elif self.left_child_exists(index):
    #             lc_index = self.find_left_child_index(index)  # find it's index
    #             if self.store[lc_index].key < self.store[index].key:
    #                 self.swap(
    #                     lc_index, index
    #                 )  # SWAPING NODES our node root has gone down
    #                 #  need to update where we are at in the array / heap level and index
    #                 # self.swap_index(lc_index, index)
    #                 index = lc_index
    #                 # update index!
    #                 # temp_lc_index = lc_index  # saving child index before swap
    #                 # lc_index = index  # assign parent index to lc-index variable
    #                 # index = temp_lc_index  # old child is now parent index
    #                 print("updating where node is now by swaping indices")
    #                 print(f"new index = {index}, swapped lc_index = {lc_index}")
    #                 # return index
    #         #
    #         # elif not self.left_child_exists(index):
    #         else:  # no children case
    #             # check that this is not out of range none will always be false
    #             return
