import pytest

seq = ["case1", "case2", "case3"]


@pytest.fixture(scope="function", params=seq)
def params(request):
    return request.param


def test_params(params):
    assert "case" in params
