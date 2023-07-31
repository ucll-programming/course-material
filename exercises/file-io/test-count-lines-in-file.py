import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("contents, expected", [
    *(
        ("\n".join(lines), len(lines))
        for lines in [
            [
                'a'
            ],
            [
                'a',
                'b',
            ],
            [
                'abc',
            ],
            [
                'line',
                'line',
                'line',
                'line',
                'line',
            ]
        ]
    )
])
@pytest.mark.parametrize('filename', [
    'a.txt',
    'file.dat',
])
def test_count_lines_in_file(tmp_path, contents, filename, expected):
    path = tmp_path / filename
    path.write_text(contents)
    actual = student.count_lines_in_file(str(path))
    assert expected == actual
