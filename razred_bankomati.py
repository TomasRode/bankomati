from pathlib import Path

class Bankomat:

    def __init__(self, lokacija):
        self.lokacija = lokacija
        self.stanje = 1000
        if Path(str(self.lokacija) + ".txt").exists():
            with open(str(self.lokacija) + ".txt") as dat:
                for vrstica in dat:
                    self.stanje = int(vrstica.split(",")[-1][: -3])

    def __str__(self):
        return "Bankomat, ki se nahaja na lokaciji: {}".format(self.lokacija)

    def __repr__(self):
        return "Bankomat {}".format(self.lokacija)

    def polnjenje(self, znesek):
        self.stanje += znesek

    def dvig(self, racun, znesek):
        if 0 <= znesek <= self.stanje:
            self.stanje -= znesek
            with open(str(self.lokacija) + ".txt" , "a") as dat:
                print("dvig,{},{},{}".format(racun, znesek, self.stanje), file=dat)
            return True
        else:
            return False

    def polog(self, racun, znesek):
        if znesek >= 0:
            self.stanje += znesek
            with open(str(self.lokacija) + ".txt", "a") as dat:
                print("polog,{},{},{}".format(racun, znesek, self.stanje), file=dat)
            return True
        else:
            return False

