# Verwarming = Heating

An architect needs to place several heating devices in a large building. In order to create a computer simulation of the building's heat control, he must be able to propose a series of heating devices. Here, each individual heating device is described using the following information fields: the name of the device, the current temperature setting, the minimum allowed temperature and the maximum allowed temperature. Within the simulation, the temperature of a particular device shall be able to be increased or decreased, and the current temperature of each device shall be retrievable at any time.


::::TASK
Define a class `Heating` that supports at least the following methods:

* An initialization method `__init__` to which the name of the device (str) must be passed. In addition, three more parameters to which the following information is passed: i) the current temperature setting (int or float), ii) the minimum allowed temperature (int or float) and iii) the maximum allowed temperature (int or float).
* A method `__str__` that returns a string representation of the heating device (str). Consider the example below to determine what this string representation should look like. All numbers should be represented by one decimal digit (use rounding).
* A method `change_temperature` that allows the current temperature setting to be changed. The temperature increment (int or float; or temperature decrement if it is a negative number) must be passed to this method. The method must ensure that the temperature remains within the allowed interval. For example, if the new temperature were lower than the minimum temperature, then the new temperature becomes the minimum temperature. Analog for exceeding the maximum temperature.
* A method `temperature` to which no arguments must be passed. The method should return the current temperature setting (float).
::::

::::USAGE
```python
>>> device1 = Heating('radiator kitchen', 20, 0, 100)
>>> device2 = Heating('radiator living room', 18, 15, 100)    
>>> device3 = Heating('radiator bathroom', 22, 18, 28)
>>> device1.print()
radiator kitchen: current temperature: 20.0; allowed min: 0.0; allowed max: 100.0
>>> device2.print()
radiator living room: current temperature: 18.0; allowed min: 15.0; allowed max: 100.0
>>> device2.change_temperature(8)
>>> print(device2.temperature)
26.0
>>> device3.change_temperature(-5)
>>> device3.print()
radiator bathroom: current temperature: 18.0; allowed min: 18.0; allowed max: 28.0
```
::::


