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

## Reading from Files

TODO file.readline()
