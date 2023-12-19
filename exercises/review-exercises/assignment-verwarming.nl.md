# Verwarming = Heating

Een architect moet verschillende verwarmingstoestellen plaatsen in een groot gebouw. Om een computersimulatie te kunnen maken van de warmteregeling van het gebouw, moet hij een reeks verwarmingstoestellen kunnen voorstellen. Hierbij wordt elk individueel verwarmingstoestel beschreven aan de hand van volgende informatievelden: de naam van het toestel, de huidige instelling van de temperatuur, de minimum toegelaten temperatuur en de maximum toegelaten temperatuur. Binnen de simulatie moet de temperatuur van een bepaald toestel verhoogd of verlaagd kunnen worden, en moet de huidige temperatuur van elke toestel te allen tijden kunnen opgevraagd worden.


::::TASK
Definieer een klasse `Heating` die minstens de volgende methoden ondersteunt:

* Een constructormethode `__init__`, die vier parameters neemt:
  * `name`: de naam van het apparaat (een string)
  * `current_temp`: de huidige temperatuurinstelling (int of float)
  * `min_temp`: de minimaal toegestane temperatuur (int of float) 
  * `max_temp`: de maximaal toegestane temperatuur (int of float)
  * `name`, `min_temp`, en `max_temp` kunnen worden opgeslagen als openbare velden
  * `current_temp` moet privaat zijn en toegankelijk via een property (eigenschap) met een setter-methode
    * De `current_temp` moet tussen `min_temp` en `max_temp` liggen.
    * Als de temperatuur lager zou zijn dan de minimumtemperatuur, dan moet de temperatuur worden ingesteld op de minimumtemperatuur. Evenzo, als de temperatuur hoger zou zijn dan de maximumtemperatuur, dan moet de temperatuur worden ingesteld op de maximumtemperatuur.
* Een methode `__str__` die een tekenreeksrepresentatie van het verwarmingsapparaat (str) retourneert. Bekijk het onderstaande voorbeeld om te bepalen hoe deze tekenreeksweergave eruit moet zien. Alle getallen moeten worden weergegeven met één decimaal cijfer (gebruik afronding).
* Een methode `change_temperature` waarmee de huidige temperatuurinstelling kan worden gewijzigd. Een parameter, `temp_change` geeft aan hoeveel de huidige temperatuur moet worden gewijzigd. Als `temp_change` een positief getal is (int of float), wordt de huidige temperatuur verhoogd met de opgegeven hoeveelheid. Als `temp_change` negatief is, wordt de huidige temperatuur verlaagd. Natuurlijk moet de huidige temperatuur binnen het toegestane bereik blijven.

::::USAGE
```python
>>> toestel1 = Heating('radiator keuken', 20, 0, 100)
>>> toestel2 = Heating('radiator living', 18, 15, 100)    
>>> toestel3 = Heating('radiator badkamer', 22, 18, 28)
>>> print(toestel1)
radiator keuken: huidige temperatuur: 20.0; toegelaten min: 0.0; toegelaten max: 100.0
>>> print(toestel2)
radiator living: huidige temperatuur: 18.0; toegelaten min: 15.0; toegelaten max: 100.0
>>> toestel2.change_temperature(8)
>>> print(toestel2.current_temp)
26.0
>>> toestel3.change_temperature(-5)
>>> print(toestel3)
radiator badkamer: huidige temperatuur: 18.0; toegelaten min: 18.0; toegelaten max: 28.0
```
::::