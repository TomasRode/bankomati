class Bankomat:

    def __init__(self, lokacija, stanje):
        self.lokacija = lokacija
        self.stanje = stanje

    def __str__(self):
        return "Bankomat, ki se nahaja na lokaciji: {}".format(self.lokacija)

    def __repr__(self):
        return "Bankomat {}".format(self.lokacija)

    def polnjenje(self, znesek):
        self.stanje += znesek

    def dvig(self, racun, znesek):
        if znesek <= self.stanje:
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
                print("polog,{},{},{}".format(print(racun), znesek, self.stanje), file=dat)
            return True
        else:
            return False

