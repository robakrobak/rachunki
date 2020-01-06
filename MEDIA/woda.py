# każde media mają swoje przyciski w __init__, a __init__w window, powinien mieć rozwijane menu, które będzie odwoływać się do odpowiednich

import window
import tkinter as tk


class Woda(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self) #zamiast super super().__init__()


    def stan_licznikow_woda(self):
        self.stan_licznikow = tk.Button(self.frame, text="STAN LICZNIKOW", width=15, highlightbackground='powderblue',
                                        highlightthickness=2, command=lambda: self.stan_licznikow()).grid(row=1, column=0,
                                                                                                        pady=10)
        self.faktury = tk.Button(self.frame, text="FAKTURY", width=15, highlightbackground='powderblue',
                                 highlightthickness=2).grid(row=1, column=1)
        self.rozliczenia = tk.Button(self.frame, text="ROZLICZENIA", width=15, highlightbackground='powderblue',
                                     highlightthickness=2).grid(row=1, column=2)

    def stan_licznikow(self):
        self.archiwum = tk.Button(self.frame, text="ARCHIWUM", width=15).grid(row=2, column=0, pady=10)
        self.archiwum = tk.Button(self.frame, text="ARCHIWUM", width=15).grid(row=2, column=0, pady=10)

