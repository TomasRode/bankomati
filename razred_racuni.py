from pathlib import Path

class Racun:

    def __init__(self, stevilka, pin):
        self.stanje = 0
        self.pin = pin
        self.stevilka = stevilka
        if Path(str(self.stevilka) + ".txt").exists():
            with open(str(self.stevilka) + ".txt") as dat:
                for vrstica in dat:
                    self.stanje = int(vrstica.split(",")[-1][: -3])

    def __str__(self):
        return "Račun {} s stanjem {}".format(self.stevilka, self.stanje)

    def __repr__(self):
        return "Racun({},{})".format(self.stevilka, self.pin)

    def polog(self, znesek):
        if znesek >= 0:
            self.stanje += znesek
            with open(str(self.stevilka) + ".txt", "a") as dat:
                print("polog,{},{}".format(znesek, self.stanje), file=dat)
            return True
        else:
            return False
        
    def dvig(self, znesek):
        if znesek <= self.stanje and znesek >= 0:
            self.stanje -= znesek
            with open(str(self.stevilka) + ".txt" , "a") as dat:
                print("dvig,{},{}".format(znesek, self.stanje), file=dat)
            return True
        else:
            return False
    

    
        
