import pytest
import student


def join(lines):
    return "".join(f'{line}\n' for line in lines)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("contents, expected", [
    *(
        (join(given_lines), join(expected_lines))
        for given_lines, expected_lines in [
            (
                [
                ],
                [
                ]
            ),
            (
                [
                    'a',
                ],
                [
                    'a',
                ]
            ),
            (
                [
                    'a',
                    'a',
                ],
                [
                    'a',
                ]
            ),
            (
                [
                    'a',
                    'a',
                    'a',
                    'a',
                    'a',
                    'a',
                    'a',
                ],
                [
                    'a',
                ]
            ),
            (
                [
                    'a',
                    'b',
                    'a',
                ],
                [
                    'a',
                    'b',
                    'a',
                ]
            ),
            (
                [
                    'one',
                    'one',
                    'two',
                    'two',
                    'three',
                    'three',
                ],
                [
                    'one',
                    'two',
                    'three',
                ]
            ),
            (
                [
                    'one',
                    'two',
                    'two',
                    'two',
                    'three',
                    'three',
                    'three',
                ],
                [
                    'one',
                    'two',
                    'three',
                ]
            ),
        ]
    )
])
@pytest.mark.parametrize('source', [
    'a.txt',
    'input.txt',
])
@pytest.mark.parametrize('destination', [
    'b.txt',
    'output.txt',
])
def test_remove_duplicate_lines(tmp_path, source, destination, contents, expected):
    source_path = tmp_path / source
    destination_path = tmp_path / destination
    source_path.write_text(contents)

    student.remove_duplicate_lines(str(source_path), str(destination_path))

    assert destination_path.is_file()
    assert expected == destination_path.read_text()
