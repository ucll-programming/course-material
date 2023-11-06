---
layout: page
title: Pytest
---

* Table of Contents
{:toc}

# Interpreting Test Results

Let's use the exercise `middle` from the chapter Arithmetic as working example.
It asks you to write a function `middle(a, b, c)` that takes three numbers (`a`, `b` and `c`) and returns the "middle" one, i.e., the number that is in between the lowest and highest number.
For example, `middle(4, 1, 3)` should return `3`.

The tests will try out many combinations of values for `a`, `b` and `c` and your algorithm must return correct results for each of them.
Let's consider a naive implementation:

```python
def middle(a, b, c):
    return a
```

If we run the tests, we get a long series of results, ending with

```bash
$ pytest test-middle.py
[3280 lines of output omitted]
FAILED test-middle.py::test_middle[7-7-1] - AssertionError: middle(1, 7, 7) should return 7 but got 1 instead
FAILED test-middle.py::test_middle[7-7-3] - AssertionError: middle(3, 7, 7) should return 7 but got 3 instead
FAILED test-middle.py::test_middle[7-7-4] - AssertionError: middle(4, 7, 7) should return 7 but got 4 instead
182 failed, 161 passed in 1.31s
```

Let's ask so see only the first failing case:

```bash
$ pytest -x test-middle.py
.F
========================================== FAILURES ========================================
___________________________________ test_middle[-3--3--1] __________________________________

a = -1, b = -3, c = -3

    @pytest.mark.timeout(1)
    @pytest.mark.parametrize("a", [-3, -1, 0, 1, 3, 4, 7])
    @pytest.mark.parametrize("b", [-3, -1, 0, 1, 3, 4, 7])
    @pytest.mark.parametrize("c", [-3, -1, 0, 1, 3, 4, 7])
    def test_middle(a, b, c):
        expected = sorted([a, b, c])[1]
        actual = student.middle(a, b, c)

>       assert expected == actual, f'middle({a}, {b}, {c}) should return {expected} but got {actual} instead'
E       AssertionError: middle(-1, -3, -3) should return -3 but got -1 instead
E       assert -3 == -1

test-middle.py:13: AssertionError
================================ short test summary info ====================================
FAILED test-middle.py::test_middle[-3--3--1] - AssertionError: middle(-1, -3, -3) should return -3 but got -1 instead
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 1 passed in 0.05s
```

* The test takes three inputs: `a`, `b` and `c`.
  Each of these will take on the values `-3`, `-1`, `0`, `1`, `3`, `4`, and `7`, as specified by the three `@pytest.mark.parametrize` lines.
* `expected` is a local variable in which the test stores the expected value.
* `actual` is a local variable in which the result of your algorithm.
* `assert expected == actual` states that the tests expects `expected` and `actual` to be equal.
  If not, the test will fail.
* Below this line, you can see the actual values of `expected` and `actual`:
  * `expected` is `-3`, which is the correct value for `middle(-1, -3, -3)`.
  * `actual` is `-1`, which is a consequence of your implementation always returning `a`.
* In the short test summary info, you can see the failure boiled down to a single line: `FAILED test-middle.py::test_middle[-3--3--1] - AssertionError: middle(-1, -3, -3) should return -3 but got -1 instead`.

When you are confronted with such a test failure report, you will want to find out

* What were the inputs given to your function?
* What is the value your function returned?
* What is the value your function should have returned?

With this information, you should be better equipped to fix your algorithm.

# Running Exercise Specific Tests

To run the tests associated with one specific exercise, run

```bash
$ pytest test-ID.py
```

Replace `ID` by the name of the function you had to write.

# Limit Output

When tests fail, pytest tries its best to be helpful and dumps large quantities of information.
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

Another way to prevent pytest from printing out overly large reports, is to ask it to stop after the first failure.

```bash
$ pytest -x test-five.py
```

You can combine this with the option discussed in the previous section:

```bash
$ pytest -x --tb=no test-five.py
```

# Running All Tests

You can run all tests in the current directory and all subdirectories at once:

```bash
$ pytest
```
