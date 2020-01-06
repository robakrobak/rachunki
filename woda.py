# każde media mają swoje przyciski w __init__, a __init__w window, powinien mieć rozwijane menu, które będzie odwoływać się do odpowiednich

import window
from tkinter import *
import tkinter as tk


class Woda(tk.Toplevel):
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Right Frame and its contents

        self.circleCanvas = Canvas(self.frame, width=100, height=100, bg='white')
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

        self.redBtn = Button(self.btnFrame, text="Red", command=lambda: self.makeCircle("red"))
        self.redBtn.grid(row=0, column=0, padx=10, pady=2)

        self.yellowBtn = Button(self.btnFrame, text="Yellow", command=lambda: self.makeCircle("yellow"))
        self.yellowBtn.grid(row=0, column=1, padx=10, pady=2)

        self.greenBtn = Button(self.btnFrame, text="Green", command=lambda: self.makeCircle("green"))
        self.greenBtn.grid(row=0, column=2, padx=10, pady=2)

        self.colorLog = Text(self.frame, width=30, height=10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)

    def makeCircle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert(0.0, color.capitalize() + "\n")

    def stan_licznikow_woda(self):
        self.stan_licznikow = tk.Button(self.frame, text="STAN LICZNIKOW", width=15, highlightbackground='powderblue',
                                        highlightthickness=2, command= lambda: self.stan_licznikow1).grid(row=1, column=0, pady=10)
        self.faktury = tk.Button(self.frame, text="FAKTURY", width=15, highlightbackground='powderblue',
                                 highlightthickness=2).grid(row=1, column=1)
        self.rozliczenia = tk.Button(self.frame, text="ROZLICZENIA", width=15, highlightbackground='powderblue',
                                     highlightthickness=2).grid(row=1, column=2)

    def stan_licznikow1(self):
        self.archiwum = tk.Button(self.frame1, text="ARCHIWUM", width=15).grid(row=3, column=0, pady=10)