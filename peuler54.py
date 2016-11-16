# project euler 55
# poker hands


class card:
    # create a card with color, number, and chosenColor (...) 
    def __init__(self,cardstr):
        self.color= cardstr[1]
        self.num= cardstr[0]

    def getColor(self):
        return self.color

    def getNumber(self):
        return self.num

    # get a description of a card
    def getPrintable(self):
        if self.color=="Black":
            if self.num==1:
                return "Wild card"
            elif self.num==2:
                return "Wild draw four"
        else:
            return self.color + str(self.num)
    def chooseColor(self,color):
        self.chosenColor=color
    def reportWildColor(self):
        return self.chosenColor
