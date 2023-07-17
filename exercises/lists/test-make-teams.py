import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("participants, team_size", [
    (
        [*"abcdefghijklmnopqrstuvwxyz"[:participant_count]],
        team_size
    )
    for participant_count in range(1, 27)
    for team_size in range(1, 10)
])
def test_make_teams(participants, team_size):
    teams = student.make_teams(participants, team_size)

    assert len(participants) < team_size or all(len(team) >= team_size for team in teams), f'{len(participants)} participants, teamsize={team_size}'
    assert sorted(participants) == sorted(participant for team in teams for participant in team)
    assert max(len(team) for team in teams) - min(len(team) for team in teams) <= 1
