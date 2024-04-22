def test_true():
    print("Testing True")
    assert True == True
    assert getattr(True, "__name__") == "True"

def test_false():
    print("Testing False")
    assert False == False
    assert getattr(False, "__name__") == "False"

test_true()
test_false()