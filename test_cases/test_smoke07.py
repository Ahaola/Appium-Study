import pytest


@pytest.fixture
def fun(request):
    marker1 = request.node.get_closest_marker("mydata1")
    marker2 = request.node.get_closest_marker("mydata2")
    if marker1 is None:
        data = None
    else:
        # data = marker.args[0] + 1
        data1 = marker1.args[0]
        data1[0] = 666

    if marker2 is None:
        data2 = None
    else:
        data2 = marker2.args[0]
        data2[-1] = 777

    return data1, data2


# @pytest.mark.mydata(3)
@pytest.mark.mydata1([1, 2, 3])
@pytest.mark.mydata2([333, 444, 555])
def test_data(fun):
    print("fun={}".format(fun))


if __name__ == '__main__':
    pytest.main(['-vs'])