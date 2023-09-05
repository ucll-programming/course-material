import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("s1, s2, expected", [
    (
        "\n".join([
            'a'
        ]),
        "\n".join([

        ]),
        0
    ),
    (
        "\n".join([
            'a'
        ]),
        "\n".join([
            'a'
        ]),
        1
    ),
    (
        "\n".join([
            'a'
        ]),
        "\n".join([
            'b'
        ]),
        0
    ),
    (
        "\n".join([
            'a',
            'a'
        ]),
        "\n".join([

        ]),
        0
    ),
    (
        "\n".join([
            'a',
            'a',
        ]),
        "\n".join([
            'a',
        ]),
        1
    ),
    (
        "\n".join([
            'a',
            'b',
        ]),
        "\n".join([
            'a',
        ]),
        1
    ),
    (
        "\n".join([
            'a',
            'b',
        ]),
        "\n".join([
            'a',
            'b',
        ]),
        2
    ),
    (
        "\n".join([
            'a',
            'b',
        ]),
        "\n".join([
            'a',
            'b',
            'c'
        ]),
        2
    ),
    (
        "\n".join([
            'a',
            'b',
        ]),
        "\n".join([
            'b',
            'a',
        ]),
        2
    ),
    (
        "\n".join([
            'a',
            'a',
            'a',
            'a',
            'a',
            'a',
        ]),
        "\n".join([
            'b',
            'b',
            'b',
            'b',
            'b',
        ]),
        0
    ),
    (
        "\n".join([
            'abc',
            'xyz',
        ]),
        "\n".join([
            'abc',
        ]),
        1
    ),
    (
        "\n".join([
            'abc',
            'xyz',
        ]),
        "\n".join([
            'xyz',
        ]),
        1
    ),
    (
        "\n".join([
            'abc',
            'xyz',
            '12345'
        ]),
        "\n".join([
            'xyz',
            '12345',
        ]),
        2
    ),
    (
        "\n".join([
            'abc',
            'xyz',
            '12345'
        ] * 1000),
        "\n".join([
            'xyz',
            '12345',
        ] * 1000),
        2
    ),
    (
        "\n".join([
            str(k) for k in range(0, 1000)
        ] * 2),
        "\n".join([
            str(k) for k in range(0, 1000)
        ] * 2),
        1000
    ),
    (
        "\n".join([
            str(k) for k in range(0, 100)
        ] * 3),
        "\n".join([
            str(k) for k in range(0, 1000)
        ] * 2),
        100
    ),
])
def test_plagiarism(s1, s2, expected):
    actual = student.plagiarism(s1, s2)
    assert expected == actual
