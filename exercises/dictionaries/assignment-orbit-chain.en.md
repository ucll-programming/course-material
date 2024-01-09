# Orbit Chains

We all know the Moon orbits the Earth.
And the Earth orbits the Sun.
The Sun, in turn, orbits a supermassive black hole in the center of our galaxy, named [Sagittarius A*](https://en.wikipedia.org/wiki/Sagittarius_A*).
Quite the galactic dance.

We can represent these relations between heavenly bodies using a `dict`:

:::code{caption="Python"}

```python
orbits = {
    'Moon': 'Earth',
    'Earth': 'Sun',
    'Sun': 'Sagittarius A*'
}
```

:::

We can add a lot more data to `orbits`: other planets in our solar system have many moons, and we know of exoplanets orbiting other stars than the Sun.

Given this information of what-orbits-what, we want to construct a chain as follows:

* We start off at a celestial body, e.g., the Moon.
* We look up in `orbits` what it orbits.
  We find the Earth.
* We look up Earth and find that it orbits the Sun.
* We then look up the Sun and learn that it orbits Sagittarius A*.
* Sagittarius A* does not appear in `orbits`: we have reached the end of the chain.

Our chain is therefore `['Moon', 'Earth', 'Sun', 'Sagittarius A*']`.

:::TASK
Write a function `orbit_chain(orbits, start)` that constructs a chain starting with the celestial body `start`.
:::

:::USAGE

```python
>>> orbits = {
        'Moon': 'Earth',
        'Mars': 'Sun',
        'Earth': 'Sun',
        'Jupiter': 'Sun',
        'Saturn': 'Sun',
        'Sun': 'Sagittarius A*',
        'Phobos': 'Mars',
        'Ganymede': 'Jupiter',
        'Callisto': 'Jupiter',
        'Europa': 'Jupiter',
    }

>>> orbit_chain(orbits, 'Moon')
['Moon', 'Earth', 'Sun', 'Sagittarius A*']

>>> orbit_chain(orbits, 'Earth')
['Earth', 'Sun', 'Sagittarius A*']

>>> orbit_chain(orbits, 'Phobos')
['Phobos', 'Mars', 'Sun', 'Sagittarius A*']
```

:::
