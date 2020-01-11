import tkinter as tk
from choice_panel import *
from window import *


class Prad:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        # Bot frame

        self.stan_licznikow = tk.Button(self.frame, text="STAN LICZNIKOWp", width=15, highlightbackground='mistyrose',
                                        highlightthickness=2, command=lambda: self.stan_licznikow_prad).grid(row=1,
                                                                                                         column=0,
                                                                                                         pady=10)
        self.faktury = tk.Button(self.frame, text="FAKTURYp", width=15, highlightbackground='mistyrose',
                                 highlightthickness=2).grid(row=1, column=1)
        self.rozliczenia = tk.Button(self.frame, text="ROZLICZENIAp", width=15, highlightbackground='mistyrose',
                                     highlightthickness=2).grid(row=1, column=2)

    def stan_licznikow_prad(self):
        self.archiwum = tk.Button(self.frame, text="ARCHIWUMp", width=15).grid(row=3, column=0, pady=10)