# Verwarming

Een architect moet verschillende verwarmingstoestellen plaatsen in een groot gebouw. Om een computersimulatie te kunnen maken van de warmteregeling van het gebouw, moet hij een reeks verwarmingstoestellen kunnen voorstellen. Hierbij wordt elk individueel verwarmingstoestel beschreven aan de hand van volgende informatievelden: de naam van het toestel, de huidige instelling van de temperatuur, de minimum toegelaten temperatuur en de maximum toegelaten temperatuur. Binnen de simulatie moet de temperatuur van een bepaald toestel verhoogd of verlaagd kunnen worden, en moet de huidige temperatuur van elke toestel te allen tijden kunnen opgevraagd worden.


::::TASK
Definieer een klasse `Verwarming` die minstens de volgende methoden ondersteunt:

* Een initialisatiemethode `__init__` waaraan de naam van het toestel (str) moet doorgegeven worden. Daarnaast zijn er nog drie parameters waaraan de volgende informatie wordt doorgegeven: i) de huidige instelling van de temperatuur (int of float), ii) de minimum toegelaten temperatuur (int of float) en iii) de maximum toegelaten temperatuur (int of float).
* Een methode `__str__` die een stringvoorstelling van het verwarmingstoestel (str) teruggeeft. Bekijk onderstaand voorbeeld om te bepalen hoe deze stringvoorstelling er moet uitzien. Alle getallen moeten weergegeven worden met één decimaal cijfer (gebruik afronding).
* Een methode `wijzig_temperatuur` waarmee de huidige instelling van de temperatuur kan gewijzigd worden. Aan deze methode moet de temperatuursverhoging (int or float; of temperatuursverlaging indien dit een negatief getal is) doorgegeven worden. De methode moet er wel voor zorgen dat de temperatuur binnen het toegelaten interval blijft. Als de nieuwe temperatuur bijvoorbeeld lager zou zijn dan de minimale temperatuur, dan wordt de nieuwe temperatuur de minimale temperatuur. Analoog voor het overschrijden van de maximale temperatuur.
* Een methode `temperatuur` waaraan geen argumenten moeten doorgegeven worden. De methode moet de huidige instelling van de temperatuur teruggeven (float).
::::

::::USAGE
```python
>>> toestel1 = Verwarming('radiator keuken', 20, 0, 100)
>>> toestel2 = Verwarming('radiator living', 18, 15, 100)    
>>> toestel3 = Verwarming('radiator badkamer', 22, 18, 28)
>>> toestel1.print()
radiator keuken: huidige temperatuur: 20.0; toegelaten min: 0.0; toegelaten max: 100.0
>>> toestel2.print()
radiator living: huidige temperatuur: 18.0; toegelaten min: 15.0; toegelaten max: 100.0
>>> toestel2.wijzig_temperatuur(8)
>>> print(toestel2.temperatuur)
26.0
>>> toestel3.wijzig_temperatuur(-5)
>>> toestel3.print()
radiator badkamer: huidige temperatuur: 18.0; toegelaten min: 18.0; toegelaten max: 28.0
```

::::


