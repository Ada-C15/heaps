
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

    def find_left_child_index(self, parent_index):
        '''Returns nodes's left child index'''
        i_left_child= parent_index * 2 + 1
        return i_left_child

    def find_right_child_index(self, parent_index):
        '''Returns node's right child index'''
        i_right_child = parent_index * 2 + 2
        return i_right_child

    def find_parent_index(self, index):
        '''Returns node's parent index'''
        i_parent = (index-1)//2
        return i_parent
    
    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty(): # heap is empty, just append
            self.store.append(HeapNode(key,value))  
            return
        
        self.store.append(HeapNode(key, value))  # add it to the end
        self.heap_up((len(self.store))- 1) #move up in the list last elem where it belongs 

    def remove(self): #added index
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty(): # heap is empty, return None 
            return None
        
        self.swap(0, len(self.store)-1) # swaps NODE at root for node at last index
        root = self.store.pop()
        self.heap_down(0)
        return root #returns removed (element that was at the root)

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"  # '['2', '3', '6']'

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ?
            Space complexity: ?
        """
        return not self.store

    def heap_up(self, index):
        """ This helper method takes an index and moves the corresponding element up the heap, if it is less than it's parent node until the Heap property is reestablished.
            Time complexity: ?
            Space complexity: ?
        """
        parent_index = (index-1) // 2
        parent = self.store[parent_index] 
        new_node = self.store[index]
 
        while new_node.key < parent.key and index > 0: # self.root   
            self.swap(parent_index,index) # swap of NODES happens, parent_index = 0 , index = 2

            #  assigning new key to new index 
            # need to update index - bc new node was were parent index was
            temp_parent_index = parent_index # saving my old parent index before swaping
            index = temp_parent_index # new child 
            # recalculation of parent index
            parent_index = (parent_index-1)//2 # recalculation of new node's parent index
            parent = self.store[parent_index] # value of parent
    

    def heap_down(self, index):
            """ This helper method takes an index and moves the corresponding element down the heap if it's larger than either of its children and continues until the heap property is reestablished.
            """
            # THERE are NO CHILDREN
            if not self.find_left_child_index(index):
                return

            #  BALANCING THE HEAP yeah~!
            # pass
            # we haven't made it to the end of the list
            while index < len(self.store): # also check when there are no children

                #  WE GOT AN ONLY CHILD
                # elif self.find_left_child_index(index):
                if self.find_left_child_index(index):
                    lc_index = self.find_left_child_index(index)
                    self.swap(lc_index, index)  # our root node has gone down a level
                    #  need to update where we are at in the array / heap level and index
                    self.swap_index(lc_index, index)
                
                # WE GOT TWO CHILDREN !!
                if self.find_left_child_index(index) and self.find_right_child_index(index): 
                    lc_index = self.find_left_child_index(index)
                    rc_index = self.find_right_child_index(index)

                    # AND THE LEFT OF THOSE TWO IS THE SMALLEST KID
                    if self.store[lc_index].key < self.store[rc_index].key:
                        self.swap(lc_index, index)  # our node root has gone down a level
                        #  need to swap index
                        self.swap_index(lc_index, index)
                    # THE RIGHT KID IS SMALLER THAN THE LEFT
                    else: # self.store[lc_index] > self.store[rc_index]
                        self.swap(rc_index, index)  # our node root has gone down a level
                    #  need to update where we are at in the array / heap level and index
                        self.swap_index(rc_index, index)

                

    # def heap_down(self, index):
    #     """ This helper method takes an index and moves the corresponding element down the heap if it's larger than either of its children and continues until the heap property is reestablished.
    #     """
    #     while index < len(self.store):
    #         if self.find_left_child_index(index):
    #             left_child = self.find_left_child_index(index)
    #         else:
    #             break
    #         if self.find_right_child_index(index):
    #             right_child = self.find_right_child_index(index) 

    #         if self.store[left_child].key < self.store[right_child].key:
    #             return index
    
    # # compare root with each of it's children 

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        # store parent
        temp = self.store[index_1]

        # put new node where parent was
        self.store[index_1] = self.store[index_2] # NEW PARENT

        # put child (previously parent) where new node was
        self.store[index_2] = temp

        print('***swap function happening here***')
        print("-------after swap ------")
        print(f'new_parent = {self.store[index_1].key},{self.store[index_1].value} new_child= {self.store[index_2].key},{self.store[index_2].value}')

    def swap_index(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp_index = index_1 # saving parent index before swap
        index_1 = index_2 # assign child index to parent_index variable
        index_2 = temp_index # old parent is now child index

        print('+++ swap index happening here +++ ')
        print("+++ after INDEX swap +++")
        print(f'new_parent index = {index_1} new_child_index= {index_2}')


    # def heap_down(self, index):
    #         """ This helper method takes an index and moves the corresponding element down the heap if it's larger than either of its children and continues until the heap property is reestablished.
    #         """
    #         #  BALANCING THE HEAP yeah~!

    #         # we haven't made it to the end of the list
    #         while index < len(self.store): # also check when there are no children

    #             # THERE are NO CHILDREN
    #             if not self.find_left_child_index(index):
    #                 return

    #             #  WE GOT AN ONLY CHILD
    #             elif self.find_left_child_index(index):
    #                 lc_index = self.find_left_child_index(index)
    #                 self.swap(lc_index, index)  # our root node has gone down a level
    #                 #  need to update where we are at in the array / heap level and index
    #                 self.swap_index(lc_index, index)
                
    #             # WE GOT TWO CHILDREN !!
    #             if self.find_left_child_index(index) and self.find_right_child_index(index): 
    #                 lc_index = self.find_left_child_index(index)
    #                 rc_index = self.find_right_child_index(index)

    #                 # AND THE LEFT OF THOSE TWO IS THE SMALLEST KID
    #                 if self.store[lc_index] < self.store[rc_index]:
    #                     self.swap(lc_index, index)  # our node root has gone down a level
    #                     #  need to swap index
    #                     self.swap_index(lc_index, index)
    #                 # THE RIGHT KID IS SMALLER THAN THE LEFT
    #                 else: # self.store[lc_index] > self.store[rc_index]
    #                     self.swap(rc_index, index)  # our node root has gone down a level
    #                 #  need to update where we are at in the array / heap level and index
    #                     self.swap_index(rc_index, index)


            


# while loop 3 cases
#  no childrend I don't do anything

# only left child
# you just swap

# case 3 2 children 
# if right and left child
# compare values of left and right children 

















# package .json file to see what version of angular 

# {HttpParams} from '@angular/common/http';
# params = HttpParams();


# {URLSearchParams} from '@angular/http';
# # params = URLSearchParams();
# import {URLSearchParams} from '@angular/common/http';

# params = new URLSearchParams();


# // converts Map<string, string[]> into { [key: string]: string []}

# get rawParams() {
#     const obj = Object.create(null);
#     for (for const [k, v] of this.params.paramsMap) {
#         obj[k] = v;
#     }
#     return obj
# }

# error TS2339: Property 'paramsMap' does not exist on type URLSearchParams

