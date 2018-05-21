from razred_racuni import *
from razred_bankomati import *

#seznam racunov
racuni = []
racuni.append(Racun(123, 1234))

#seznam stevilk racunov:
seznam_stevilk_racunov = []
for racun in racuni:
    seznam_stevilk_racunov.append(racun.stevilka)
    
    
#seznam bankomatov
bankomati = []
bankomati.append(Bankomat("Ljubljana", 1000))




####################################   UPORABNIŠKI VMESNIK ###################################################

import tkinter as tk

okno = tk.Tk()

ustvari_racun = tk.Button(okno, text="Ustvari račun")
izberi_racun = tk.Label(okno, text="Izberi račun")
izbrani_racun = tk.StringVar(okno)
racuni = tk.OptionMenu(okno, izbrani_racun, *seznam_stevilk_racunov)
izberi_bankomat = tk.Label(okno, text="Izberi bankomat")


ustvari_racun.pack()
izberi_racun.pack()
racuni.pack()
izberi_bankomat.pack()

okno.mainloop()
