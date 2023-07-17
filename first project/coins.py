
class USD:
    # A function gets the value of the Dollar
    def get_value(self):
        return 3.52

    # A function calculates the user's requested value according to the Dollar value
    def calculate(self,value_to_convert):
        return value_to_convert*self.get_value()


class ILS:
    # A function gets the value of the Shekel
    def get_value(self):  #
        return 0.28

    # A function calculates the user's requested value according to the Shekel value
    def calculate(self, value_to_convert):
        return value_to_convert * self.get_value()

class EUR:
    # A function gets the value of the Euro

   def get_value(self):
       return 4.23

    # A function calculates the user's requested value according to the Euro value
   def calculate(self, value_to_convert):
       return value_to_convert * self.get_value()