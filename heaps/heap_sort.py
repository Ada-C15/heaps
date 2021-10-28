def swap(list, index_1, index_2):
    """ Swaps two elements in a list"""
    list[index_1], list[index_2] = list[index_2], list[index_1]


def find_left_child(list, index):
    return 2 * index + 1


def find_right_child(list, index):
    return 2 * index + 2


def heap_down(list, index, last_node_index):
    """ Takes an index and moves it down the heap if it's smaller
        than it's child node.
        last_node_index - defines the bound b/w sorted and unsorted
        part of array.
    """

    length = last_node_index

    while True:

        left = find_left_child(list, index)
        right = find_right_child(list, index)

        if right < length:
            # both left and right children exist
            # swap with the biggest of them
            if list[index] >= max(list[left], list[right]):
                break
            elif list[left] < list[right]:
                swap(list, index, right)
                index = right
            else:
                swap(list, index, left)
                index = left
        elif left < length:
            # no right child
            # check if the only child is bigger:
            # yes -> swap
            # no -> break, because we reached the end of the heap
            if list[left] > list[index]:
                swap(list, index, left)
                index = left
            else:
                break
        else:
            break


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(logn)
        Space Complexity: O(1)

        We need to sort an array in ASCENDING order.

        1. Create max-heap.
        - iterate over parents nodes (that have at least one child) from bottom to top to check if parent node is bigger than its children, if not - swap with bigger child.
        2. Root node is always going to be max of all numbers
        3. Iterate n times, where n is number of elements and for each iteration:
        - Take root node and swap it with the last leaf in the heap (unsorted part of array).
        - Swapped root nodes will eventually form a sorted portion of the array, so next time exlude this sorted portion from consideration -> for every new iteration consider n-m elements, where m - number of sorted elements.
        - heap-down new root node, to get max-heap again.
    """
    # create max-heap
    for last_parent_node_index in range((len(list) - 2) // 2, -1, -1):
        heap_down(list, last_parent_node_index, len(list))

    # sorting part
    for last_node_index in range(len(list) - 1, 0, -1):
        swap(list, 0, last_node_index)
        heap_down(list, 0, last_node_index)

    return list
