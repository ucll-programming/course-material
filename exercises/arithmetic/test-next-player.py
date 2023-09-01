import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("player, player_count", [
    (player, player_count)
    for player_count in [1, 4, 10, 25]
    for player in range(player_count)
])
def test_next_player(player, player_count):
    actual = student.next_player(player=player, player_count=player_count)

    assert (actual == player + 1 and actual < player_count) or (actual == 0 and player + 1 == player_count)
