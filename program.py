from razred_racuni import *
from razred_bankomati import *

#ustvari nov račun, rabiš file z računi
#da ti bere stanje računa
#da ti errorje vrže, ko je treba

#seznam racunov
racuni = [Racun(111, 1111), Racun(222, 2222), Racun(333, 3333), Racun(444, 4444)]

#seznam stevilk racunov:
stevilke_racunov = []
for racun in racuni:
    stevilke_racunov.append(racun.stevilka)
    
    
#seznam bankomatov
bankomati = []
bankomati.extend((Bankomat("Ljubljana", 1000), Bankomat("Koper", 1000), Bankomat("Maribor", 1000), Bankomat("Celje", 1000)))

#seznam lokacij bankomatov
lokacije_bankomatov = []
for bankomat in bankomati:
    lokacije_bankomatov.append(bankomat.lokacija)

#################################### FUNKCIJE  ####################################
def dvig():
    indeks_stevilke = stevilke_racunov.index(izbrani_racun.get())
    indeks_lokacije = lokacije_bankomatov.index(izbrani_bankomat.get())
    znesek = vneseni_dvig.get()
    racun = racuni[indeks_stevilke]
    bankomat = bankomati[indeks_lokacije]
    if racun.dvig(znesek) and bankomat.dvig(racun, znesek) and vneseni_pin_dvig.get() == racun.pin:
        print("uspešno")
        vnos_pin_dvig.delete(0, "end")
        return True
    else:
        print("neuspešno")
        vnos_pin_dvig.delete(0, "end")
        return False


def polog_racun():
    indeks_stevilke = stevilke_racunov.index(izbrani_racun.get())
    indeks_lokacije = lokacije_bankomatov.index(izbrani_bankomat.get())
    znesek = vneseni_polog.get()
    racun = racuni[indeks_stevilke]
    bankomat = bankomati[indeks_lokacije]
    if racun.polog(znesek) and vneseni_pin_polog.get() == racun.pin:
        print("uspešno")
        vnos_pin_polog.delete(0, "end")
        return True
    else:
        print("neuspešno")
        vnos_pin_polog.delete(0, "end")
        return False
    
def nov_racun():
    if novi_pin == potrdi_pin:
        racuni.append(Racun(stevilke_racunov[-1] + 1, novi_pin))
        return True
    else:
        return False
#################################### UPORABNIŠKI VMESNIK ###################################################

import tkinter as tk
from tkinter import ttk

okno = tk.Tk()

zvezek = ttk.Notebook(okno)
z_domov = ttk.Frame(zvezek)
z_polog = ttk.Frame(zvezek)
z_dvig = ttk.Frame(zvezek)
z_nov_racun = ttk.Frame(zvezek)

zvezek.add(z_domov, text="Domov")
zvezek.add(z_polog, text="Polog")
zvezek.add(z_dvig, text="Dvig")
zvezek.add(z_nov_racun, text="Nov Račun")

naslov = tk.Label(z_domov, text='DOBRODOŠLI V SISTEM BANKE')
izberi_racun = tk.Label(z_domov, text="Izberi račun")
izbrani_racun = tk.IntVar(z_domov)
lista_racuni = tk.OptionMenu(z_domov, izbrani_racun, *stevilke_racunov)

izberi_bankomat = tk.Label(z_domov, text="Izberi bankomat")
izbrani_bankomat = tk.StringVar(z_domov)
lista_bankomati = tk.OptionMenu(z_domov, izbrani_bankomat, *lokacije_bankomatov)

polog_naslov = tk.Label(z_polog, text='POLOG')
vneseni_polog = tk.DoubleVar(z_polog)
vnos_polog = tk.Entry(z_polog, textvariable=vneseni_polog, justify="center")
vnesite_znesek_polog = tk.Label(z_polog, text="Vnesite znesek v EUR")
vnesite_pin_polog = tk.Label(z_polog, text="Vnesite PIN")
vneseni_pin_polog = tk.IntVar(z_polog)
vnos_pin_polog = tk.Entry(z_polog, textvariable=vneseni_pin_polog, show="*", justify="center")
potrdi_polog = tk.Button(z_polog, text="POTRDI", command=polog_racun)

dvig_naslov = tk.Label(z_dvig, text="DVIG")
vneseni_dvig = tk.DoubleVar(z_dvig)
vnos_dvig = tk.Entry(z_dvig, textvariable=vneseni_dvig, justify="center")
vnesite_znesek_dvig = tk.Label(z_dvig, text="Vnesite znesek v EUR", justify="center")
vnesite_pin_dvig = tk.Label(z_dvig, text="Vnesite PIN")
vneseni_pin_dvig = tk.IntVar(z_dvig)
vnos_pin_dvig = tk.Entry(z_dvig, textvariable=vneseni_pin_dvig, show="*", justify="center")
potrdi_dvig = tk.Button(z_dvig, text="POTRDI", command=dvig)

nov_racun = tk.Label(z_nov_racun, text="NOV RAČUN")
nova_stevilka = tk.Label(z_nov_racun, text="Številka novega računa je {}".format(stevilke_racunov[-1] + 1))
nastavite_pin = tk.Label(z_nov_racun, text="Nastavite PIN")
potrdite_pin = tk.Label(z_nov_racun, text="Potrdite PIN")
vneseni_novi_pin = tk.IntVar(z_nov_racun)
novi_pin = tk.Entry(z_nov_racun, textvariable=vneseni_novi_pin, show="*", justify="center")
vneseni_potrdi_pin = tk.IntVar(z_nov_racun)
potrdi_pin = tk.Entry(z_nov_racun, textvariable=vneseni_potrdi_pin, show="*", justify="center")
ustvari_racun = tk.Button(z_nov_racun, text="Ustvari račun", command=nov_racun)

# dokapitalizacija = tk.Button(z_nov_racun, text="DOKAPITALIZACIJA")


##SESTAVLJANJE

zvezek.pack()

naslov.grid(column=1, row=1, columnspan=2)

izberi_racun.grid(column=1, row=2)
izberi_bankomat.grid(column=2, row=2)

lista_racuni.grid(column=1, row=3)
lista_bankomati.grid(column=2, row=3)

polog_naslov.grid(column=1, row=4, columnspan=2)

vnesite_znesek_polog.grid(column=1, row=5)
vnesite_pin_polog.grid(column=2, row=5)

vnos_polog.grid(column=1, row=6)
vnos_pin_polog.grid(column=2, row=6)

potrdi_polog.grid(column=1, row=7, columnspan=2)

dvig_naslov.grid(column=1, row=8, columnspan=2)

vnesite_znesek_dvig.grid(column=1, row=9)
vnesite_pin_dvig.grid(column=2, row=9)

vnos_dvig.grid(column=1, row=10)
vnos_pin_dvig.grid(column=2, row=10)

potrdi_dvig.grid(column=1, row=11, columnspan=2)

nov_racun.grid(column=1, row=12, columnspan=2)

nova_stevilka.grid(column=1, row=13, columnspan=2)

nastavite_pin.grid(column=1, row=14)
potrdite_pin.grid(column=2, row=14)

novi_pin.grid(column=1, row=15)
potrdi_pin.grid(column=2, row=15)

ustvari_racun.grid(column=1, row=16, columnspan=2)

# dokapitalizacija.grid(column=1, row=18, columnspan=2)

okno.mainloop()
