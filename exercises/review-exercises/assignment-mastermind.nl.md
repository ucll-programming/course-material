# Mastermind

Mastermind bestaat erin dat je een geheime code moet weten te vinden. Deze code bestaat uit een onbepaald aantal cijfers. Je mag hiervoor zelf meermaals gokken. Voor elke gok krijg je feedback in de vorm van twee getallen :

* Het eerste getal geeft aan hoeveel cijfers je correct gegokt hebt.
* Het tweede getal is het aantal cijfers die wel voorkomen in de code, maar op een andere plaats.

Stel dat de code 1 2 3 4 is en je gokt 1 5 3 2. De feedback die je hierop krijgt is 1 2 :

* Het eerste cijfer 1 is juist en staat op de juiste positie.
* De cijfers 2 en 3 komen in de code voor, maar in je gok staan ze op de vierde en derde plaats, respectievelijk, terwijl ze op de tweede en derde plaats horen.

::::TASK
Schrijf een functie `mastermind(code, gok)` die, gegeven twee lijsten met getallen code en gok, de feedback teruggeeft als een lijst van twee getallen.
::::

::::USAGE

```python
>>> mastermind([],[])
[0,0]

>>> mastermind([1],[1])
[1,0]

>>> mastermind([1],[2])
[0,0]

>>> mastermind([1,2],[2,1])
[0,2]

>>> mastermind([1,2],[1,1])
[1,0]

>>> mastermind([1,1,1],[1,1,2])
[2,0]

>>> mastermind([1,2,3,4],[1,3,2,4])
[2,2]
```

::::


