# Verwarming = Heating

An architect needs to place several heating devices in a large building. In order to create a computer simulation of the building's heat control, he must be able to propose a series of heating devices. Here, each individual heating device is described using the following information fields: the name of the device, the current temperature setting, the minimum allowed temperature and the maximum allowed temperature. Within the simulation, the temperature of a particular device shall be able to be increased or decreased, and the current temperature of each device shall be retrievable at any time.


::::TASK
Define a class `Heating` that supports at least the following methods:

* An constructor method `__init__`, which takes four parameters:
  * `name`: the name of the device (a string)
  * `current_temp`: the current temperature setting (int or float)
  * `min_temp`: the minimum allowed temperature (int or float) 
  * `max_temp`: the maximum allowed temperature (int or float)
  * `name`, `min_temp`, and `max_temp` can be stored as public fields
  * `current_temp` should be private and accessed via a property with a setter method
    * The `current_temp` must be between `min_temp` and `max_temp`.
    * If the temperature would be lower than the minimum temperature, then the temperature should be set to the minimum temperature. Similarly, if the temperature would be higher than the maximum temperature, the temperature should be set to the maximum temperature.
* A method `__str__` that returns a string representation of the heating device (str). Consider the example below to determine what this string representation should look like. All numbers should be represented by one decimal digit (use rounding).
* A method `change_temperature` that allows the current temperature setting to be changed. One parameter, 'temp_change' indicates how much the current temperature should be changed. If temp_change is a positive number (int or float), the current temperature will be increased by the given amount. If temp_change is negative, the current temperature will be decreased. Of course, the current temperature must stay within the allowed range.

::::USAGE
```python
>>> device1 = Heating('radiator kitchen', 20, 0, 100)
>>> device2 = Heating('radiator living room', 18, 15, 100)    
>>> device3 = Heating('radiator bathroom', 22, 18, 28)
>>> print(device1)
radiator kitchen: current temperature: 20.0; allowed min: 0.0; allowed max: 100.0
>>> print(device2)
radiator living room: current temperature: 18.0; allowed min: 15.0; allowed max: 100.0
>>> device2.change_temperature(8)
>>> print(device2.current_temp)
26.0
>>> device3.change_temperature(-5)
>>> print(device3)
radiator bathroom: current temperature: 18.0; allowed min: 18.0; allowed max: 28.0
```
::::