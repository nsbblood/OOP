class Superman:
  def fly(self):
    print("I can fly!")
  def super_strength(self):
    print("I have super strength!")

class Batman:
  def smart(self):
    print("I am super smart!")
  def gadgets(self):
    print("I have cool gadgets!")

class SuperBat(Superman, Batman):
  pass

superbat=SuperBat()

#print(superbat.smart()) we have already used print above...
superbat.gadgets()