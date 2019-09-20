#Python OOP Tutorial 5: Special (Magic/Dunder) Methods

class Employee:
  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + ''