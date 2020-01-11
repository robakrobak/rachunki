import tkinter as tk
from choice_panel import *
from window import *


class Gaz:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        # Bot frame

        self.stan_licznikow = tk.Button(self.frame, text="STAN LICZNIKOWg", width=15, highlightbackground='lemonchiffon',
                                        highlightthickness=2, command=lambda: self.stan_licznikow_gaz).grid(row=1,
                                                                                                         column=0,
                                                                                                         pady=10)
        self.faktury = tk.Button(self.frame, text="FAKTURYg", width=15, highlightbackground='lemonchiffon',
                                 highlightthickness=2).grid(row=1, column=1)
        self.rozliczenia = tk.Button(self.frame, text="ROZLICZENIAg", width=15, highlightbackground='lemonchiffon',
                                     highlightthickness=2).grid(row=1, column=2)

    def stan_licznikow_gaz(self):
        self.archiwum = tk.Button(self.frame, text="ARCHIWUM", width=15).grid(row=3, column=0, pady=10)