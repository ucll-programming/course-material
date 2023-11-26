# Writing Files

All data a Python program generates disappear as soon as it ends.
If you want your program to "remember" data from the previous time it was run, you have to store this data somewhere.
Typically this is done using files.

## Opening a File with Write Access

As discussed earlier, files need to be opened prior to interacting with them.
By default, we only get read access.
In order to get write access, we have to request this explicitly:

:::code{caption="Python"}

```python
with open(filename, 'w', encoding='utf-8') as file:
    # Interact with file
```

:::

The `'w'` tells the OS we intend to write.
Note that opening a file in mode `w` will empty that file: all data that was in it is lost.

::::INFO
The [possible modes](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) for opening a file are

:::center
| Mode | Description |
| :---: | ----------- |
| `'r'`  | Read only |
| `'w'`  | Write only (empties file first!) |
| `'r+'` | Reading and writing |
| `'a'` | Appending (writing at end) |
:::

::::

## Writing to a File

The following methods can be used to write to a file:

* `file.write(string)` writes the given `string` to the file.
  The current stream position moves with it: you can call `write` multiple times and each `string` will be added to the end of the file.
* `file.writelines(strings)` writes all `strings` to the file.

Note that neither of these methods add newlines.

::::EXAMPLE

:::code{caption="Python"}

```python
with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(['a', 'b', 'c'])
```

:::

The file `output.txt' now contains

:::code{caption="Text"}

```text
abc
```

:::

Note how, even though the method is called `writelines`, all strings are written to the same line.
In order to put the strings on separate lines, you have to add the newlines yourself:

:::code{caption="Python"}

```python
with open('output.txt', 'w', encoding='utf-8') as file:
    file.writelines(['a\n', 'b\n', 'c\n'])
```

:::

::::

An alternative approach to writing to a file is to rely on `print`:

:::code{caption="Python"}

```python
with open(output_file, 'w') as output:
    print(string, file=output_file)
```

:::

Here, we named the file `output_file` to avoid confusion: `print` has a parameter named `file` which can be used to express where to send the `string` to.
By default, this is [STDOUT](https://en.wikipedia.org/wiki/Standard_streams), i.e., to the screen.
In our case, we want the data to be sent to a file.

Note that `print` does automatically add a newline, so each string you feed to `print` will end up on a separate line.
