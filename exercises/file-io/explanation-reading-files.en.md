# Reading Files

In this section we discuss how we can read data from text files.

## Opening Files

Files can be read from and written to.
That is really their purpose.

However, multiple programs could try to access the same file at the same time.
This would lead to chaos: the two programs would overwrite each other's data, and the file would become corrupt, i.e., the data inside it makes no sense.
To prevent this, the operating system demands that you *open* a file first.
You can then interact with the file.
After you're done, you *close* the file.

The OS will make sure no two programs have the same file open at the same time.
If you try to open a file that's already in use by another program, you will get an error.
It's also important that you close a file, hereby giving others a chance to use the file.

As always, reality is a bit more complex.
For example, multiple programs reading from the same file at the same time is perfectly safe.
However, once one program needs to write it, it needs exclusive access.
This is why when opening a file, you need to mention whether you intend to read or write to it.
Based on that, the OS can decide whether to grant you access or not.

Opening and closing a file in Python can be done using

:::code{caption="Python"}

```python
file = open("my-file.txt")
# interact with file
file.close()
```

:::

This approach is a bit risky however: what if something bad happens while interacting with the file?
The `file.close()` statement would then be skipped, making it impossible for other programs to access the file.
For this reason, Python offers a special construct:

:::code{caption="Python"}

```python
with open("my-file.txt") as file:
    # interact with file
```

:::

Here, at the end of the `with` block, the file will automatically be closed.
No matter what happens while interacting with the file, it is guaranteed that it will be closed at the end.
In other words, you should always rely on `with` when dealing with files.

::::INFO
If you write code that opens a file, then crashes before closing it again, there's no problem:
the OS will clean up after you.

However, a script can recover from crashes (see exceptions).
In this case, the `close` operation will be skipped yet your program keeps running.
As long as it runs, the file will remain open, making it inaccessible to others.
This can become a big problem in the case of long running programs.
::::

## Encoding

There are [many ways](https://en.wikipedia.org/wiki/Character_encoding) texts can be encoded: [ASCII](https://en.wikipedia.org/wiki/ASCII), [UTF-8](https://en.wikipedia.org/wiki/UTF-8), [EBCDIC](https://en.wikipedia.org/wiki/EBCDIC) and so on.
These days most files are encoded using UTF-8.
It is strongly recommended that you make the encoding explicit when opening the file.
This is done as follows:

:::code{caption="Python"}

```python
with open("my-file.txt", encoding='utf-8') as file:
    # interact with file
```

:::

::::INFO
The `encoding=` parameter is known as a keyword argument.
Suffice it to say that Python allows you to explicitly mention the parameter name, for the sake of clarity.
Keyword arguments have a few more advantages, but we won't discuss them in detail right now.
::::

## Reading from Files

Say you open a file using

:::code{caption="Python"}

```python
with open("my-file.txt", encoding='utf-8') as file:
    # interact with file
```

:::

Inside the `with` block, the variable `file` is set to a special object representing the opened file.
Note that `file` is just an identifier: you can pick any name you want.

You can invoke methods on it, just like you could with strings, using the syntax `file.method_name(arguments)`.
We discuss some of these methods, specifically those that let you read from the file.

* `file.read()` reads the entire contents of the file and returns it as a *single string*.
  You probably shouldn't use this approach when the file is large.
* `file.readlines()` reads the entire contents of the file and returns it as an *array of strings*, where each string correspond to a line.
* `file.readline()` reads the next line in the file and returns it as string.
   If no more lines are left in the file, an empty string is returned.

::::IMPORTANT
An opened file keeps track of a "current stream position", i.e., it remembers to what point you have read from the file.
Initially this position is set to the beginning of the file.
`file.readline()` advances this position to the beginning of the next line, so that the next time you invoke `file.readline()` it knows where to look for the next line.
`file.read()` and `file.readlines()` both read the entire contents in one go, therefore the position is moved to the end of the file.
::::

::::IMPORTANT
Whenever you read lines (i.e., using `readline` or `readlines`), know that each string will contain the newline character `\n`.
In other words, a line `abc` in the file will be represented by `"abc\n"`.
::::

::::EXAMPLE
Say we have a file `input.txt` with the following contents:

:::code{caption="Text"}

```text
First line
Second line
Third line
Fourth line
Fifth line
```

:::

:::code{caption="Python"}

```python
# We open it the "wrong" way (= not using with) so that
# we can work step by step for the sake of this example
>>> file = open('input.txt', encoding='utf-8')

>>> file.readline()
"First line\n"

>>> file.readline()
"Second line\n"

# Also starts reading from the current stream position
>>> file.readlines()
["Third line\n", "Fourth line\n", "Fifth line"]

# Current stream position is at end of file, no more lines left
>>> file.readline()
""
```

:::

::::
