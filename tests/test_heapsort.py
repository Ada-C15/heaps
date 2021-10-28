from heaps.heap_sort import heap_sort

def test_it_sorts_an_empty_list():
    assert heap_sort([]) == []

def test_it_sorts_a_one_element_list():
    assert heap_sort([5]) == [5]

def test_it_can_sort_a_5_element_list():
    # Arrange
    numbers = [5, 27, 3, 16, 50]
    # numbers = [3, 6, 1, 0, 16, 57]

    # Act
    result = heap_sort(numbers)

    # Assert
    assert result == [3, 5, 16, 27, 50]
    # assert result == [0, 1, 3, 6, 16, 57]
