# Movie

We want to create a small movie database.

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
