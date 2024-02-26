#OOP
class Champ:
  
  def __init__(self,name,health,attack):
    self.__name = name
    self.__health = health
    self.__attack = attack
    
  #getter
  def getName(self):
    return self.__name
    
  def getHealth(self):
    return self.__health
    
  #setter
  def diserang(self,damage):
    self.__health -= damage
    
  def setAttack(self):
    self.__attack = dmgoutput
    
#awal dari game 
yanto = Champ("yanto",100,20)

#game berjalan
print(yanto.getName())
print(f"Health yanto sekarang = {yanto.getHealth()}")
yanto.diserang(9)
print(f"Health yanto setelah diserang = {yanto.getHealth()}")