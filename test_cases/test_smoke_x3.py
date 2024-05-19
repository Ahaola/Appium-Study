import pytest

def test1(x):
    return x + 1

def test_a():
    print("………………")
    assert test1(0) == 1

class TestCace:
    def test_b(self):
        print("test_b…………")
        assert 'hehe' in 'hehehehehehe11111'

if __name__ =='__main__':
    pytest.main()

class TestCase2:
    def test_c(self):
        assert 'dodo' in 'dodohaha'

    def test_d(self):
        print('这是test_d')