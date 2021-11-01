from heap_sort import heap_sort

def test_it_sorts_an_empty_list():
    assert heap_sort([]) == []

def test_it_sorts_a_one_element_list():
    assert heap_sort([5]) == [5]

def test_it_can_sort_a_5_element_list():
    # Arrange
    numbers = [5, 27, 3, 16, 50]

    # Act
    result = heap_sort(numbers)

    # Assert
    assert result == [3, 5, 16, 27, 50]
