from razred_racuni import *
from razred_bankomati import *

#seznam racunov
racuni = []
racuni.extend((Racun(111, 1111), Racun(222, 2222), Racun(333, 3333), Racun(444, 4444)))

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
    if racuni[stevilke_racunov.index(int(izbrani_racun))].dvig(vneseni_dvig) and bankomati[lokacije_bankomatov.index(int(izbrani_bankomat))].dvig(vneseni_dvig) and vneseni_pin == racuni[stevilke_racunov.index(int(izbrani_racun))].pin:
        racuni[stevilke_racunov.index(int(izbrani_racun))].dvig(vneseni_dvig)
        bankomati[lokacije_bankomatov.index(int(izbrani_bankomat))].dvig(vneseni_dvig)
    else:
        return False

def polog_racun():
    if racuni[stevilke_racunov.index(int(izbrani_racun))].polog(vneseni_polog):
        racuni[stevilke_racunov.index(int(izbrani_racun))].polog(vneseni_polog)
    else:
        return False

    
#################################### UPORABNIŠKI VMESNIK ###################################################

import tkinter as tk

okno = tk.Tk()

naslov = tk.Label(okno, text='DOBRODOŠLI V SISTEM BANKOMATOV!')


izberi_racun = tk.Label(okno, text="Izberi račun")
izbrani_racun = tk.StringVar(okno)
racuni = tk.OptionMenu(okno, izbrani_racun, *stevilke_racunov)

izberi_bankomat = tk.Label(okno, text="Izberi bankomat")
izbrani_bankomat = tk.StringVar(okno)
bankomati = tk.OptionMenu(okno, izbrani_bankomat, *lokacije_bankomatov)

polog_naslov = tk.Label(okno, text='POLOG')
vneseni_polog = tk.DoubleVar(okno)
vnos_polog = tk.Entry(okno, textvariable=vneseni_polog)
vnesite_znesek_polog = tk.Label(okno, text="Vnesite znesek v EUR")
vnesite_pin_polog = tk.Label(okno, text="Vnesite PIN")
vneseni_pin_polog = tk.DoubleVar(okno)
vnos_pin_polog = tk.Entry(okno, textvariable=vneseni_pin_polog)
potrdi_polog = tk.Button(okno, text="POTRDI", command=polog_racun)

dvig_naslov = tk.Label(okno, text="DVIG")
vneseni_dvig = tk.DoubleVar(okno)
vnos_dvig = tk.Entry(okno, textvariable=vneseni_dvig)
vnesite_znesek_dvig = tk.Label(okno, text="Vnesite znesek v EUR")
vnesite_pin_dvig = tk.Label(okno, text="Vnesite PIN")
vneseni_pin_dvig = tk.DoubleVar(okno)
vnos_pin_dvig = tk.Entry(okno, textvariable=vneseni_pin_dvig)
potrdi_dvig = tk.Button(okno, text="POTRDI", command=dvig)

ustvari_racun = tk.Label(okno, text="NOV RAČUN")
nova_stevilka = tk.Label(okno, text="Številka novega računa je {}".format(stevilke_racunov[-1] + 1))
nastavite_pin = tk.Label(okno, text="Nastavite PIN")
potrdite_pin = tk.Label(okno, text="Potrdite PIN")
vneseni_novi_pin = tk.DoubleVar(okno)
novi_pin = tk.Entry(okno, textvariable=vneseni_novi_pin)
vneseni_potrdi_pin = tk.DoubleVar(okno)
potrdi_pin = tk.Entry(okno, textvariable=vneseni_potrdi_pin)
ustvari_racun = tk.Button(okno, text="Ustvari račun")


##SESTAVLJANJE

naslov.grid(column=1, row=1, columnspan=2)

izberi_racun.grid(column=1, row=2)
izberi_bankomat.grid(column=2, row=2)

racuni.grid(column=1, row=3)
bankomati.grid(column=2, row=3)

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

ustvari_racun.grid(column=1, row=12, columnspan=2)

nova_stevilka.grid(column=1, row=13, columnspan=2)

nastavite_pin.grid(column=1, row=14)
potrdite_pin.grid(column=2, row=14)

novi_pin.grid(column=1, row=15)
potrdi_pin.grid(column=2, row=15)

ustvari_racun.grid(column=1, row=16, columnspan=2)

okno.mainloop()
