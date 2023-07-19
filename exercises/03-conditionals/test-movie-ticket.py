import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("duration, imax, is_student, ticket_count, expected", [
    (70, False, False, 1, 10),
    (70, False, True, 1, 7),
    (70, False, True, 2, 14),
    (70, True, False, 1, 12),
    (95, False, False, 1, 11),
    (121, False, False, 1, 12),
    (151, False, False, 1, 15),
    (151, False, False, 3, 45),
    (151, True, False, 1, 18),
    (151, True, True, 1, 15),
])
def test_movie_ticket(duration, imax, is_student, ticket_count, expected):
    actual = student.movie_ticket(duration, imax, is_student, ticket_count)
    assert expected == actual, f'movie_ticket({duration}, {imax}, {is_student}, {ticket_count}) should return {expected} but got {actual}'