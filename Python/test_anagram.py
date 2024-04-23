from anagram import anagram1, anagram2, normalize



def test_anagram1():
    assert anagram1("listen","silent") == True
    assert anagram1("A gentleman", "Elegant man") == True
    assert anagram1("Clint Eastwood", "Old west action") == True
    assert anagram1("hello", "mello") == False

def test_anagram2():
    assert anagram2("listen","silent") == True
    assert anagram2("A gentleman", "Elegant man") == True
    assert anagram2("Clint Eastwood", "Old west action") == True
    assert anagram2("hello", "mello") == False


def test_normalize():
    assert normalize("Clint Eastwood") == "clinteastwood"

