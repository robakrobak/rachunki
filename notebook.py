# generator z bazy danych zrób

import sqlite3
import tkinter as tk
from tkinter import Frame, Label, Button
from tkinter.ttk import Notebook

import database_creator


class Window:
    def __init__(self):
        # window
        self.window = tk.Tk()
        self.window.title('ROZLICZENIE MEDIÓW - NA STOKU')
        self.window.geometry("2585x1200")

        # frame
        self.frame_1 = Frame(self.window, width=500, height=500)
        self.frame_1.grid(row=0, column=0)
        self.frame_2 = Frame(self.window, width=500, height=500)
        self.frame_2.grid(row=1, column=0)

        # table layout
        self.tablayout = Notebook(self.frame_1)
        self.tablayout_liczniki = Notebook(self.frame_2)


        self.media()
        self.start()
        self.window.mainloop()

        # obsługa bazy danych
        # self.conn = sqlite3.connect("water.db")
        # self.cursor = self.conn.cursor()

    def media(self):
        self.woda()
        self.gaz()
        self.prad()
        self.tablayout.grid()

    def woda(self):
        # tab_WODA
        tab_woda = Frame(self.tablayout)
        tab_woda.grid()
        self.tablayout.add(tab_woda, text="WODA")

        tab_stan_licznikow = Frame(self.tablayout_liczniki)
        tab_stan_licznikow.grid()
        self.tablayout_liczniki.add(tab_stan_licznikow, text="STAN LICZNIKÓW")

        # self.stan_licznikow_woda(tab_woda)

    def prad(self):
        # tab_PRĄD
        tab_prad = Frame(self.tablayout)
        tab_prad.grid()

        for row in range(5):
            for column in range(8):
                label2 = Label(tab_prad, text='Row: ' + str(row) + "Column: " + str(column))
                label2.grid(row=row, column=column)

        self.tablayout.add(tab_prad, text="PRĄD")

    def gaz(self):
        # tab_GAZ
        tab_gaz = Frame(self.tablayout)
        tab_gaz.grid()

        for row in range(5):
            for column in range(6):
                label3 = Label(tab_gaz, text='Row: ' + str(row) + "Column: " + str(column))
                label3.grid(row=row, column=column)

        self.tablayout.add(tab_gaz, text="GAZ")

    def stan_licznikow_woda(self, tab_woda):
        connection = sqlite3.connect('water.db')
        cursor = connection.execute('select * from water')
        names = [description[0] for description in cursor.description]
        n = 0
        for name in names:
            name = tk.Label(tab_woda, text=name, padx=10, pady=10, relief='raised', border='1',
                            borderwidth=1)
            name.grid(row=4, column=0 + n, padx=5)
            n += 1

    def start(self):
        database_creator.payments_database()
        database_creator.water_invoice_database()
        database_creator.water_database()


if __name__ == "__main__":
    Window()
