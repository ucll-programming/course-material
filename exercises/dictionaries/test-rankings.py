import pytest
import student
import itertools


@pytest.mark.timeout(1)
@pytest.mark.parametrize('participants', [
    [],
    ['Raymond Garraty'],
    *(
        permutation
        for permutation in itertools.permutations(['Raymond Garraty', 'Stebbins', 'Peter McVries', 'Arthur Baker', 'Abraham'])
    ),
])
def test_combine(participants):
    result = student.rankings(participants)

    for expected, participant in enumerate(participants, start=1):
        actual = result[participant]
        assert expected == actual
