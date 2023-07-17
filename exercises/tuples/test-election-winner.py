import pytest
import student
from collections import Counter


@pytest.mark.timeout(1)
@pytest.mark.parametrize("votes", [
    (),
    ('Kang',),
    ('Kang', 'Kodos'),
    ('Kang', 'Kodos', 'Kang'),
    tuple([*"aaaabbbccd"]),
    tuple([*"abbcccdddd"]),
    tuple([*"sjoxjqopxqppxxjopxoqjpxpkpaxutajkxxmfaxmx"]),
    "a" * 1000 + "b" * 1001 + "c" * 1002 + "d" * 1003,
    "a" * 1000 + "b" * 1008 + "c" * 1002 + "d" * 1003,
    "a" * 1000 + "b" * 1008 + "c" * 1102 + "d" * 1003,
])
def test_election(votes):
    actual = student.election_winner(votes)
    counts = Counter(votes)

    assert votes or actual is None
    assert not votes or counts[actual] == max(counts.values())
