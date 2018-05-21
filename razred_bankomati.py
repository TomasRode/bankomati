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
        if racun.dvig(znesek) and znesek <= self.stanje:
            return True
        else:
            return False

    def polog(self, racun, znesek):
        if racun.polog(znesek):
            return True
        else:
            return False

