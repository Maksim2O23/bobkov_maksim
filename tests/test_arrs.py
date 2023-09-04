from utils import arrs

def test_get_existing_index():
    assert arrs.get([1, 2, 3], 1) == 2

def test_get_non_existing_index():
    assert arrs.get([1, 2, 3], 10) is None

def test_get_with_default():
    assert arrs.get([1, 2, 3], 10, "default_value") == "default_value"

def test_my_slice_with_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]

def test_my_slice_with_start_only():
    assert arrs.my_slice([1, 2, 3, 4], 2) == [3, 4]

def test_my_slice_with_end_only():
    assert arrs.my_slice([1, 2, 3, 4], end=2) == [1, 2]

def test_my_slice_with_no_start_or_end():
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_my_slice_start_greater_than_length():
    assert arrs.my_slice([1, 2, 3, 4], 5) == []

def test_my_slice_end_greater_than_length():
    assert arrs.my_slice([1, 2, 3, 4], end=10) == [1, 2, 3, 4]





