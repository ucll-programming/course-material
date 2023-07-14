import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('strings, expected', [
    (
        ["ABC"],
        {
            "A": ["ABC"],
        }
    ),
    (
        ["abc"],
        {
            "A": ["abc"],
        }
    ),
    (
        ["ABC", "abc"],
        {
            "A": ["ABC", "abc"],
        }
    ),
    (
        ["Albert", "Anne"],
        {
            "A": ["Albert", "Anne"],
        }
    ),
    (
        ["Albert", "Anne", "Bert"],
        {
            "A": ["Albert", "Anne"],
            "B": ["Bert"],
        }
    ),
    (
        ["Anne", "Albert", "Bert"],
        {
            "A": ["Anne", "Albert"],
            "B": ["Bert"],
        }
    ),
    (
        ["Anne", "Bert", "Albert"],
        {
            "A": ["Anne", "Albert"],
            "B": ["Bert"],
        }
    ),
    (
        ["Anne", "Bert", "Anne"],
        {
            "A": ["Anne", "Anne"],
            "B": ["Bert"],
        }
    ),
    (
        ["Peter", "Bart", "Annemie", "Stijn"],
        {
            "A": ["Annemie"],
            "B": ["Bart"],
            "P": ["Peter"],
            "S": ["Stijn"],
        }
    ),
    (
        ["Peter", "Bart", "Annemie", "Stijn", "Petra", "Barbara", "Andre"],
        {
            "A": ["Annemie", "Andre"],
            "B": ["Bart", "Barbara"],
            "P": ["Peter", "Petra"],
            "S": ["Stijn"],
        }
    ),
])
def test_group_by_first_letter(strings, expected):
    actual = student.group_by_first_letter(strings)
    assert expected == actual
