import pytest
from heaps.min_heap import MinHeap

# Fixture to start each test with a new Heap
@pytest.fixture()
def heap() -> MinHeap:
    return MinHeap()

def test_can_be_instantiated(heap):
    assert isinstance(heap, MinHeap)

def test_remove_on_empty_heap_returns_none(heap):
    assert heap.remove() == None

def test_can_add_nodes_to_heap(heap):
    # Arrange
    key = 5
    value = "Pasta"

    # Act-assert (heap.add returns None)
    assert heap.add(key, value) == None

def test_nodes_are_added_in_proper_order(heap):
    # Arrange
    heap.add(3, "Pasta")
    heap.add(6, "Soup")
    heap.add(1, "Pizza")

    # Act
    output = str(heap)

    # Assert
    assert output == "[Pizza, Soup, Pasta]"


def test_works_for_adding_nodes_in_proper_order_with_6_nodes(heap):
    # Arrange
    heap.add(3, "Pasta")
    heap.add(6, "Soup")
    heap.add(1, "Pizza")
    heap.add(0, "Donuts")
    heap.add(16, "Cookies")
    heap.add(57, "Cake")

    # Act
    output = str(heap)

    # Assert
    assert output == "[Donuts, Pizza, Pasta, Soup, Cookies, Cake]"

def test_works_for_adding_nodes_in_proper_order_with_6_nodes_2(heap):
    # Arrange
    # heap.add(3)
    # heap.add(6)
    # heap.add(1)
    # heap.add(0)
    # heap.add(16)
    # heap.add(57)

    numbers = [5, 27, 3, 16, 50]
    for num in numbers:
        heap.add(num)
    # Act
    output = str(heap)

    # Assert
    # assert output == "[0, 1, 3, 6, 16, 57]"
    assert output == "[3, 16, 5, 27, 50]"

def test_it_can_remove_nodes_in_proper_order(heap):
    # Arrange
    heap.add(3, "Pasta")
    heap.add(57, "Cake")
    heap.add(6, "Soup")
    heap.add(1, "Pizza")
    heap.add(0, "Donuts")
    heap.add(16, "Cookies")


    # Act
    returned_items = ["Donuts", "Pizza", "Pasta", "Soup", "Cookies", "Cake"]

    for item in returned_items:
        assert heap.remove() == item

