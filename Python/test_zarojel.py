from zarojel import zarojelek



def test_zarojel():
    assert zarojelek("((5+3)*2+1)") == True
    assert zarojelek("{[(3+1)+2]+}") == True
    assert zarojelek("(3+{1-1)}") == False
    assert zarojelek("[1+1]+(2*2)-{3/3}") == True
    assert zarojelek("(({[(((1)-2)+3)-3]/3}-3)") == False