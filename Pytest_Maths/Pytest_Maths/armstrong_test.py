from amstrong_no import is_armstrong

def test_armstrong():
    assert is_armstrong(153) == True
    assert is_armstrong(370) == True
    assert is_armstrong(9474) == True
    assert is_armstrong(9475) == False
    assert is_armstrong(1634) == True
    assert is_armstrong(8208) == True
    assert is_armstrong(0) == True
    assert is_armstrong(-370) == False
