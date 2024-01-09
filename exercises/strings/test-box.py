import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected", [
    (
        "x",
        "\n".join([
            "+---+",
            "| x |",
            "+---+",
        ])
    ),
    (
        "xy",
        "\n".join([
            "+----+",
            "| xy |",
            "+----+",
        ])
    ),
    (
        "xyz",
        "\n".join([
            "+-----+",
            "| xyz |",
            "+-----+",
        ])
    ),
    (
        "xyz abcde",
        "\n".join([
            "+-----------+",
            "| xyz abcde |",
            "+-----------+",
        ])
    ),
])
def test_box(string, expected):
    actual = student.box(string)
    assert expected == actual
