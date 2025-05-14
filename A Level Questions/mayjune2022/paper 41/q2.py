class Balloon:
    def __init__(self, defenceitem, colour):
        self.__defenceitem = defenceitem # DECLARE defenceitem : STRING
        self.__colour = colour # DECLARE colour : STRING
        self.__health = 100 # DECLARE health : INTEGER

    def GetDefenceItem(self):
        return self.__defenceitem
    
    def ChangeHealth(self, hp):
        self.__health = self.__health + hp

    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False
        


defenceitem = input("Defence item: ")
colour = input("Colour: ")

Balloon1 = Balloon(defenceitem, colour)

def Defend(balloon):
    strength = int(input("Strength: "))
    Balloon1.ChangeHealth(int(strength * -1))
    print(Balloon1.GetDefenceItem())
    if Balloon1.CheckHealth():
        print("Dead. ")
    else:
        print("Remaining health!")
    return(Balloon1)

Defend(Balloon1)
