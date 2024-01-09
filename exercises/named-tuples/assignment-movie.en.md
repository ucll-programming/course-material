# Movie

We want to create a small movie database.
We'll start off by defining a data structure that holds a movie's information and then proceed with defining some functions that allow us to extract information from our little movie database.

## Movie Type

A movie has the following properties:

* A title
* A runtime (expressed in minutes)
* A director
* A tuple of actors

::::TASK
Create a new named tuple `Movie` with the properties mentioned above.
Be careful to respect their order.
::::

## Actor Count

::::TASK
Create a function `actor_count(movie)` that returns the number of actors in the movie.
::::

::::USAGE

```python
>>> movie = Movie(
    title='Buried',
    runtime=95,
    director='Rodrigo Cortes',
    actors=(Ryan Reynolds,)
)
>>> actor_count(movie)
1
```

::::

## Movies by Director

::::TASK
Create a function `movies_by(movies, director)` that, given a list of movies, returns the titles of all movies made by `director`.

The order in which the names are returned does not matter.
::::

::::USAGE

```python
>>> movies = [
...     Movie(
...         title='The Prestige',
...         director='Christopher Nolan',
...         ...
...     ),
...     Movie(
...         title='Inception',
...         director='Christopher Nolan',
...         ...
...     )
...     Movie(
...         title='Postal',
...         director='Uwe Boll',
...     )
... ]
>>> movies_by(movies, 'Christopher Nolan')
['The Prestige', 'Inception']
```

::::

## Longest Movie

::::TASK
Write a function `longest_movie(movies)` that returns the longest movie in the list.
Return the entire `Movie` object, not just the title.
::::

::::USAGE

```python
>>> movies = [
        Movie(
            title="Once Upon a Time in America",
            runtime=229,
            ...
        ),
        Movie(
            title="Lawrence of Arabia",
            runtime=218,
            ...
        )
        Movie(
            title="Amra Ekta Cinema Banabo",
            runtime=1265,
            ...
        )
... ]
>>> longest_movie(movies)
Movie(title="Amra Ekta Cinema Banabo", runtime=1265, ...)
```

::::
