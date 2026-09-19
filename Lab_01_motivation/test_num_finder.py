from num_finder import NumFinder

def test_num_finder_mixed_numbers():
    # Arrange & Act
    nf = NumFinder()
    nf.find([4, 25, 7, 9])
    
    # Assert
    assert nf.largest == 25
    assert nf.smallest == 4

def test_num_finder_descending_list_catches_elif_bug():
    """
    Checks the descending list [4, 3, 2, 1].
    With 'elif', largest remains float('-inf').
    With two separate 'if' blocks, both smallest and largest are correct.
    """
    nf = NumFinder()
    nf.find([4, 3, 2, 1])
    assert nf.largest == 4
    assert nf.smallest == 1

def test_num_finder_ascending_list():
    nf = NumFinder()
    nf.find([1, 2, 3, 4])
    assert nf.largest == 4
    assert nf.smallest == 1

def test_num_finder_single_element():
    nf = NumFinder()
    nf.find([5])
    assert nf.largest == 5
    assert nf.smallest == 5