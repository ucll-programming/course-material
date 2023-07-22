# Introduction

Integers, floating point numbers, booleans and strings can be seen as basic building blocks of every program.
They can be said to be the atoms out of which everything is built.

::::EXAMPLE
Let's examine a file containing a movie.

* The movie probably has a title, which is represented by a string.
  Other metadata such as director, actors, etc. are also strings.
* The visual part of the movie consists of a long series of images.
  A typical movie runs at 24 frames per second for 2 hours, so around 172,800 images.
* One image is a matrix of colors of size 4096&times;2160.
* A color is defined as a mix of red, blue and green, each of these represented as an int.
* The audio consists of multiple channels, e.g., mono (1 channel), stereo (2 channels), Dolby Surround 7.1 (8 channels).
* Each channel is a sound wave that's been sampled at a rate of (probably) 48,000 samples per second.
* Each sample is an integer.

As you can see, a movie is really just around 4.5 trillion numbers, and a few strings.
::::

Apart from having our building blocks, we also need a way of "glueing" them together, build molecules if you wish.
That's where collections come in.
We'll start with *tuples*.

## Tuples

A tuple is an object that can hold an arbitrary number of other objects.
The syntax is `(a, b, c, d, ...)` where `a`, `b`, `c`, `d`, ... are its content.
A tuple can contain other tuples.

::::EXAMPLE

* A 2D-point has two coordinates.
  We can store these in a tuple: `(4, 9)`.
* A playing card has a value and a suit: `(8, 'hearts')`.
* A hand of playing cards can be represented using nested tuples: `((3, 'clubs'), (10, 'diamonds'), (12, 'spades), ...)`.
* A color has three components: R, G and B.
  These can be stored in a tuple of size three: `(192, 128, 32)`.
* A row of colors can be represented by a tuple of color-tuples: `((0, 0, 0), (255, 255, 255), (192, 64, 64), ...)`.
* An image can be represented by a tuple of such rows: `(((0, 0, 0), (255, 255, 255), (192, 64, 64)), ((128, 128, 128), (64, 64, 64)), ...)`.
::::

* Literals (beware of singleton tuple syntax)
* `[]`, `len`
* `in` (can't be used for subsequences like strings!)
* Destructuring
