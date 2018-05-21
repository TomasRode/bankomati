class Racun:

    def __init__(self, stevilka, pin):
        self.stanje = 0
        self.pin = pin
        self.stevilka = stevilka

    def __str__(self):
        return "Račun {} s stanjem {}".format(self.stevilka, self.stanje)

    def __repr__(self):
        return "Račun({},{})".format(self.stevilka, self.pin)

    def preveri_pin(self, poizkus):
        if poizkus == self.pin:
            return True
        else:
            return False

    def polog(self, znesek):
        if znesek >= 0:
            self.stanje += znesek
            with open(str(self.stevilka) + ".txt", "a") as dat:
                print("polog, {}, {}".format(znesek, self.stanje), file=dat)
            return True
        else:
            return False
        
    def dvig(self, znesek):
        if znesek <= self.stanje:
            self.stanje -= znesek
            with open(str(self.stevilka) + ".txt" , "a") as dat:
                print("dvig, {}, {}".format(znesek, self.stanje))
            return True
        else:
            return False
    

    
        
