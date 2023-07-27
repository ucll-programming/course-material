# Password

::::TASK
Write a class `Password`.

* Its constructor takes a string that represents a password.
* It stores this password in a private field named `password` (adapt this name as needed).
* Define a method `verify(string)` that checks if the given `string` is equal to the password.
::::

Note how the class makes the password inaccessible from outside, but still allows to check whether a given password is correct.
The class's public interface does not leak any information about the password.

::::USAGE

```python
>>> password = Password('azer1234')
>>> password.verify('qwer1234')
False

>>> password.verify('azer1234')
True
```

::::

::::IMPORTANT
In reality, the password will *never* be stored directly as it is an unacceptable security risk.
Instead, a [hash digest](https://en.wikipedia.org/wiki/Cryptographic_hash_function#Password_verification) will be stored.
This still allows the password to be verified, but if the hash digest were to become public, the accounts will not be compromised.
::::
