import pytest
import student


@pytest.fixture
def averager():
    return student.Averager()


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected_average", [
    ([5], 5),
    ([10, 20], 15),
    ([20, 30, 40], 30),
    ([0, 0, 0, 0, 0], 0),
    ([12, 13], 12.5)
])
def test_averaging(averager, ns, expected_average):
    for n in ns:
        averager.add(n)

    assert averager.average() == pytest.approx(expected_average)


def test_reset(averager):
    averager.add(10)
    averager.reset()
    averager.add(20)
    assert averager.average() == 20
