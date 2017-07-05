class Player(object):

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.dealer = False
    
    def removeChips(self, amount):
        if amount > self.chips:
            raise RuntimeError('Amount greater than avalible.')
        self.chips -= amount
        return self.amount

    def addChips(self, amount):
        self.chips += amount
        return self.chips

    def addCardToHand(self, card):
        self.hand.append(card)
    
    def switchCard(self, ioldcard, newcard):
        self.hand[ioldcard] = newcard

    def showHand(self):
        if not self.hand:
            print 'No tienes cartas en tu mano'
        else:
            print 'Tus cartas son: '
            for card in self.hand:
                print card

    def dropHand(self):
        del self.hand[:]

"""p1 = Player("Darby", 100)
print p1.name
print p1.chips
p1.addCardToHand("J")
p1.addCardToHand("K")
p1.switchCard(1, "A")
p1.dropHand()
p1.addCardToHand("Q")
p1.showHand()"""
