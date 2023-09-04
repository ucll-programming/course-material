---
layout: page
title: Pytest
---

* Table of Contents
{:toc}

# Running Exercise Specific Tests

To run the tests associated with one specific exercise, run

```bash
$ pytest test-ID.py
```

Replace `ID` by the name of the function you had to write.

# Limit Output

When tests fail, Pytest tries its best to be helpful and dumps large quantities of information.
For example,

```bash
$ pytest test-five.py
F                                                                                                          [100%]
=================================================== FAILURES ====================================================
___________________________________________________ test_five ___________________________________________________

    @pytest.mark.timeout(1)
    def test_five():
        expected = 5
        actual = student.five()
>       assert expected == actual, f'Expected {expected}, got {actual} instead'
E       AssertionError: Expected 5, got 4 instead
E       assert 5 == 4

test-five.py:9: AssertionError
============================================ short test summary info ============================================
FAILED test-five.py::test_five - AssertionError: Expected 5, got 4 instead
```

If, however, you are only interested in succinct failure messages, you can skip the detailed information and ask only for the summary:

```bash
$ pytest --tb=no test-five.py
F                                                                                                          [100%]
============================================ short test summary info ============================================
FAILED test-five.py::test_five - AssertionError: Expected 5, got 4 instead
1 failed in 0.01s
(progtool-py3.11)
```

# Stopping at First Failure

Another way to prevent Pytest from printing out overly large reports, is to ask it to stop after the first failure.

```bash
$ pytest -x test-five.py
```

# Running All Tests

You can run all tests in the current directory and all subdirectories at once:

```bash
$ pytest
```
