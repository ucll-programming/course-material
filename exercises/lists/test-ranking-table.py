import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ranking, expected_lines", [
    (
        [
            ("a", 1),
        ],
        [
            "1 a 1.00",
        ]
    ),
    (
        [
            ("a", 1),
            ("b", 2),
        ],
        [
            "1 a 1.00",
            "2 b 2.00",
        ]
    ),
    (
        [
            ("a", 1),
            ("bb", 2),
        ],
        [
            "1 a  1.00",
            "2 bb 2.00",
        ]
    ),
    (
        [
            ("a", 1.1),
            ("bb", 2.32),
        ],
        [
            "1 a  1.10",
            "2 bb 2.32",
        ]
    ),
    (
        [
            ("a", 1.1),
            ("bb", 2.32),
            ("c", 3),
        ],
        [
            "1 a  1.10",
            "2 bb 2.32",
            "3 c  3.00",
        ]
    ),
    (
        [
            ('Max Park', 3.13),
            ('Yusheng Du', 3.47),
            ('Tymon Kolasiński', 3.85),
            ('Jode Brewster', 3.88),
            ('Asher Kim-Magierek', 3.89),
            ('Yiheng Wang', 3.90),
            ('Luke Garrett', 3.95),
            ('Max Siauw', 4.03),
            ('Ruihang Xu', 4.06),
            ('Sean Patrick Villanueva', 4.11)
        ],
        [
            " 1 Max Park                3.13",
            " 2 Yusheng Du              3.47",
            " 3 Tymon Kolasiński        3.85",
            " 4 Jode Brewster           3.88",
            " 5 Asher Kim-Magierek      3.89",
            " 6 Yiheng Wang             3.90",
            " 7 Luke Garrett            3.95",
            " 8 Max Siauw               4.03",
            " 9 Ruihang Xu              4.06",
            "10 Sean Patrick Villanueva 4.11",
        ]
    ),
])
def test_ranking_table(ranking, expected_lines):
    expected = "\n".join(expected_lines)
    actual = student.ranking_table(ranking)
    assert actual == expected
