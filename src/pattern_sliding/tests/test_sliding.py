from src.pattern_sliding.a_sliding import find_averages_of_subarrays
from src.pattern_sliding.b_max_sum_subrray import find_max_sum_subarray


def test_find_averages_of_subarrays():
    assert find_averages_of_subarrays(
        5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) == [2.2, 2.8, 2.4, 3.6, 2.8]
    assert find_averages_of_subarrays(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    assert find_averages_of_subarrays(1, [1, 2, 3, 4, 5]) == [
        1.0, 2.0, 3.0, 4.0, 5.0]
    assert find_averages_of_subarrays(2, [1, 2, 3, 4, 5]) == [
        1.5, 2.5, 3.5, 4.5]
    assert find_averages_of_subarrays(3, [1, 2, 3]) == [2.0]


def test_find_max_sum_subarray():
    assert find_max_sum_subarray(2, [2, 3, 4, 1, 5]) == [3, 4]
    assert find_max_sum_subarray(3, [2, 1, 5, 1, 3, 2]) == [5, 1, 3]
    assert find_max_sum_subarray(2, [2, 1, 5, 1, 3, 2]) == [5, 1]
    assert find_max_sum_subarray(4, [2, 1, 5, 1, 3, 2]) == [5, 1, 3, 2]
    assert find_max_sum_subarray(1, [2, 1, 5, 1, 3, 2]) == [5]
