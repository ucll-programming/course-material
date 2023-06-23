import pytest
import student


@pytest.mark.parametrize("player, player_count", [
    (player, player_count)
    for player_count in [1, 4, 10, 25]
    for player in range(player_count)
])
def test_next_player2(player, player_count):
    actual = student.next_player2(player=player, player_count=player_count)

    assert (actual == player + 1 and actual <= player_count) or (actual == 1 and player == player_count)
