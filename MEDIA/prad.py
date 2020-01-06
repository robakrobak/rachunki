import window
import tkinter as tk


class Prad:
    def stan_licznikow_prad(self):
        self.stan_licznikow = tk.Button(self.frame, text="STAN LICZNIKOW", width=15, highlightbackground='mistyrose').grid(row=1, column=0, pady=10)
        self.faktury = tk.Button(self.frame, text="FAKTURY", width=15, highlightbackground='mistyrose').grid(row=1, column=1)
        self.rozliczenia = tk.Button(self.frame, text="ROZLICZENIA", width=15, highlightbackground='mistyrose').grid(row=1, column=2)
