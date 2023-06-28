import pytest
import student


@pytest.mark.parametrize("version, breaking_change, new_features, expected", [
    testcase
    for major in [0, 1, 4]
    for minor in [0, 2, 5, 9]
    for patch in [0, 3, 15]
    for testcase in [
        (
            (major, minor, patch),
            True,
            False,
            (major + 1, 0, 0),
        ),
        (
            (major, minor, patch),
            True,
            True,
            (major + 1, 0, 0),
        ),
        (
            (major, minor, patch),
            False,
            True,
            (major, minor + 1, 0),
        ),
        (
            (major, minor, patch),
            False,
            False,
            (major, minor, patch + 1),
        )
    ]
])
def test_increase_version(version, breaking_change, new_features, expected):
    actual = student.increase_version(
        version=version,
        breaking_change=breaking_change,
        new_features=new_features
    )

    assert expected == actual, f"increase_version({version}, {breaking_change}, {new_features}) should return {expected} but returned {actual}"
