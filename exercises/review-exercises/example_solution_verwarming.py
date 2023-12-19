class Heating:
    def __init__(self, name, current_temp, min_temp, max_temp):
        self.name = name
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.current_temp = current_temp

    def __str__(self):
        return self.name + ': current temperature: ' + str(self.current_temp) + "; allowed min: " + str(self.min_temp) + "; allowed max: " + str(self.max_temp)
    
    def change_temperature(self, temp_change):
        new_temp = self.current_temp + temp_change
        self.current_temp = new_temp

    @property
    def current_temp(self):
        return self.__current_temp
    
    @current_temp.setter
    def current_temp(self,temp):
        new_temp = temp
        if temp < self.min_temp:
            new_temp = self.min_temp
        elif temp > self.max_temp:
            new_temp = self.max_temp
        self.__current_temp = new_temp