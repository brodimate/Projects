from median import the_median


def test_median():
    assert the_median([1, 2, 3, 4, 5]) == 3
    assert the_median([3, 1, 2, 5, 3]) == 3
    assert the_median([1, 300, 2, 200, 1]) == 2
    assert the_median([3, 6, 20, 99, 10, 15]) == 12.5