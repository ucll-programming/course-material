# Introduction

In this chapter, we'll deal with files.
Files can be used to store any kind of data: images, video, audio, text, documents, fonts, etc.
Generally, an extension is used to indicate what kind of data is stored:

* `.jpg`, `.gif` and `.png` are popular image formats.
* `.mp3`, `.m4a`, `.ogg`, `.wav`. `.mid` are typical audio formats.
* `.pdf`, `.docx`, `.html` are used for documents.
* and so on.

## Binary vs Text Files

We distinguish between two kinds of files: binary files and text files.
This terminology, even though it's standard, can be a bit confusing: *all* files ultimately contain a long sequence of `0` and `1`s, so in that sense, *all* files are binary.
So, let's clarify the exact difference between these two types of file.

* A *text file* stores data in human-readable form.
  All bytes are to be interpreted as characters (ASCII/Unicode).
  Examples of human-readable file formats are `html`, `md`, `csv`, `xml`, `json` and `yaml`.
* A *binary file* does not try to be human-readable and can therefore store data in much more compact form.
  Most file formats are binary: `.jpg`, `.gif`, `.png`, `.mp3`, `docx`, etc.

To actually see the difference, use Visual Studio Code (or any other text editor) to open an `.html` file and a `.jpg`.

::::EXAMPLE
Consider numbers: in a text file, a number will be written in decimal form, each digit written out as a separate byte.
For example, the number `10000` would take up five bytes, as we need five digits to represent it.

In a binary file, we would wonder how many bytes we actually need to represent 10000.
The answer is two, as two bytes allow us to represent integers up to 65,535.
We could even go further and think in terms of bits: we really only need 14 bits.

In reality it's a little more complicated, but we don't want to fill pages on that topic here.
We have to leave something to the other courses :-)
::::
