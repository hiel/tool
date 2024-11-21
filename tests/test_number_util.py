from python.number_util import NumberUtils


def test_is_in_closed_range():
    assert NumberUtils.is_in_closed_range(20, 10, 30) is True
    assert NumberUtils.is_in_closed_range(20, 20, 30) is True
    assert NumberUtils.is_in_closed_range(20, 10, 20) is True
    assert NumberUtils.is_in_closed_range(20, 30, 30) is False
    assert NumberUtils.is_in_closed_range(20, 10, 10) is False
    assert NumberUtils.is_in_closed_range(20, 30, 10) is False


def test_is_in_open_range():
    assert NumberUtils.is_in_open_range(20, 10, 30) is True
    assert NumberUtils.is_in_open_range(20, 20, 30) is False
    assert NumberUtils.is_in_open_range(20, 10, 20) is False
    assert NumberUtils.is_in_open_range(20, 30, 10) is False


def test_is_in_closed_range():
    assert NumberUtils.is_in_closed_range(20, 10, 30) is True
    assert NumberUtils.is_in_closed_range(20, 20, 30) is True
    assert NumberUtils.is_in_closed_range(20, 10, 20) is True
    assert NumberUtils.is_in_closed_range(20, 30, 30) is False
    assert NumberUtils.is_in_closed_range(20, 10, 10) is False
    assert NumberUtils.is_in_closed_range(20, 30, 10) is False


def test_is_in_closed_range():
    assert NumberUtils.is_in_closed_range(20, 10, 30) is True
    assert NumberUtils.is_in_closed_range(20, 20, 30) is True
    assert NumberUtils.is_in_closed_range(20, 10, 20) is True
    assert NumberUtils.is_in_closed_range(20, 30, 30) is False
    assert NumberUtils.is_in_closed_range(20, 10, 10) is False
    assert NumberUtils.is_in_closed_range(20, 30, 10) is False
