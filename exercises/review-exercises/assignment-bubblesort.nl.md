# Bubblesort

Het idee achter Bubble Sort is zeer eenvoudig: we zoeken naar opeenvolgende elementen die in de foute volgorde staan en verwisselen deze van plaats. Dit herhalen we tot alle elementen juist staan.

Bijvoorbeeld, beschouw de lijst [2, 4, 1, 3]:

* De eerste twee elementen 2 en 4 staan juist.
* De volgende twee elementen 4 en 1 staan verkeerd. We wisselen ze om, de lijst is nu [2, 1, 4, 3].
* We kijken naar het volgende paar opeenvolgende elementen, 4 en 3. Ook deze moeten omgewisseld worden, wat aanleiding geeft tot 2, 1, 3, 4.
* We starten weer bij het begin. De eerste twee elementen 2 en 1 staan fout → [1, 2, 3, 4].
* We vinden geen ongeordende koppels meer. Het sorteren is voltooid.

::::TASK
Schrijf een functie `bubblesort(ns)` die bovenstaand algoritme toepast op de lijst `ns`. De functie moet de gegeven lijst ns wijzigen en geen resultaat teruggeven.
::::

::::USAGE

```python
>>> bubblesort([])
[]

>>> bubblesort([0])
[0]

>>> bubblesort([0,1])
[0,1]

>>> bubblesort([1,0])
[0,1]

>>> bubblesort([3,2,1])
[1,2,3]

>>> bubblesort([1,11,2])
[1,2,11]
```

::::

