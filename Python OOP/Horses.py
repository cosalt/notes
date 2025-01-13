class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name # DECLARE Name : STRING
        self.__MaxFenceHeight = MaxFenceHeight # DECLARE MaxFenceHeight : INTEGER
        self.__PercentageSuccess = PercentageSuccess # DECLARE PercentageSuccess : INTEGER

    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success():
        pass


Horses = []   
Beauty = Horse('Beauty', 150, 72)
Horses.append(Beauty)

Jet = Horse('Jet', 160, 65)
Horses.append(Jet)

print(Horses[0].GetName())
print(Horses[1].GetName())




class Fense:
    def __init__(self, Height, Risk):
        self.__Height = Height
        self.__Risk = Risk

    def getheight(self):
        return self.__Height
    
    def getrisk(self):
        return self.__Risk
    
Course = []
for i in range(4):
    print("\n\n")

    height = int(input("Height: "))
    while height < 70 or height > 180:
        print("Must be within 70-180cm!")
        height = int(input("Height: "))

    risk = int(input("Risk: "))
    while risk < 1 or risk > 5:
        print("Must be within 1-5!")
        risk = int(input("Risk: "))
    
    Course.append([height, risk])

print(Course)
