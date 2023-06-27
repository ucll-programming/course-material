# Cake 4

We now have our very fancy `cake3` function that allows us to easily determine how many cakes we can bake.
Unfortunately, the required amounts for each ingredient are [_hardcoded_](https://en.wikipedia.org/wiki/Hard_coding).
We would like to generalize the function so that we can specify ourselves how much of ingredient we need.

Write a function `cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake)`
that returns the number of cakes you can make.

* The first four parameters tell you how many of each ingredient you have in stock.
* The last four parameters tell you how many of each ingredient you need per cake.

Hardcoding is often a bad idea: it makes your code less usable for no good reason.
It is as if your code makes certain rigid assumptions, such as believing that all cakes always require the exact same amount of ingredients in this case.

As a general rule, it is better to rely on parameters.

`cake4` still hard codes certain assumptions, i.e., it is possible to generalize it further.
Can you tell how?

We don't have the necessary tools to actually make a fully generalized `cake` function, but we'll definitely revisit this exercise later on when we do.
