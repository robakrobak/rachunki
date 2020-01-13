import tkinter as tk
from choice_panel import *
from tkinter import StringVar, Button
from window import *
import sqlite3


class Woda:
    def __init__(self, root, frame):
        self.list_of_input = []

        self.frame = frame
        self.root = root
        self.frame2 = tk.Frame(root, width=900, height=600)
        self.frame2.grid(row='1', column='0', sticky="nw", pady=40)

        self.stan_licznikow = tk.Button(frame, text="STAN LICZNIKOWw", width=15, highlightbackground='powderblue',
                                        highlightthickness=2, command=lambda: self.create_water_database_menu()).grid(
            row=1,
            column=0,
            pady=10)
        self.faktury = tk.Button(frame, text="FAKTURYw", width=15, highlightbackground='powderblue',
                                 highlightthickness=2).grid(row=1, column=1)
        self.rozliczenia = tk.Button(frame, text="ROZLICZENIAw", width=15, highlightbackground='powderblue',
                                     highlightthickness=2).grid(row=1, column=2)

        # obsługa bazy danych
        self.conn = sqlite3.connect("water.db")
        self.cursor = self.conn.cursor()

    def create_water_database_menu(self):
        # tworzymy grupę kolumn
        self.columns_first_group()
        # tworzymy nazwy kolumn
        self.columns_name_water()
        #

    def columns_first_group(self):
        #okres rozliczeniowy
        okres_rozliczeniowy_label = tk.Label(self.frame2, text='OKRES ROZLICZENIOWY', padx=10, pady=10, relief='raised',
                                             border='1',
                                             borderwidth=1, width = 29)
        okres_rozliczeniowy_label.config(font=("Courier", 8))
        okres_rozliczeniowy_label.grid(row=3, column=2, columnspan=2, pady = 5)

        # okres rozliczeniowy
        stan_licznikow_label = tk.Label(self.frame2, text='STAN LICZNIKÓW', padx=10, pady=10, relief='raised',
                                             border='1',
                                             borderwidth=1, width=46)
        stan_licznikow_label.config(font=("Courier", 8))
        stan_licznikow_label.grid(row=3, column=4, columnspan=3, pady=5)


    def columns_name_water(self):
        # display database columns names
        connection = sqlite3.connect('water.db')
        cursor = connection.execute('select * from water')
        names = [description[0] for description in cursor.description]
        n = 0
        for name in names[0:5]:
            name = tk.Label(self.frame2, text=name, padx=5, pady=15, relief='raised', border='1',
                            borderwidth=2, width=14)
            name.config(font=("Courier", 8))
            name.grid(row=4, column=0 + n, padx=5)
            n += 1
        for name in names[5:]:
            name = tk.Label(self.frame2, text=name, padx=5, pady=15, relief='raised', border='1',
                            borderwidth=3, width=14, highlightbackground='powderblue',
                            highlightthickness=2)
            name.config(font=("Courier", 8))
            name.grid(row=4, column=0 + n, padx=5)
            n += 1

    def get_input(self, n):
        text_input = []
        m = 0
        a = self.names[0]
        print('self.names: ', self.names)
        print('self.names[0]: ', self.names[0])

        for e in self.names:
            print('for e in self.names print e: ', e)
            get_input = self.names[0].get()
            text_input.append(get_input)
            m += 1
            print('get input:', get_input)
            print('text_input:', text_input)

    # def input(self, n):
    #     self.names = []
    #     for numb in range(n):
    #         self.names.append(numb)
    #     m = 0
    #
    #     for _ in range(n):
    #         self.names[0 + m] = StringVar()
    #         # self.names[0 + m].set()
    #         m += 1
    #     return

    def new_entry(self, n):
        names = []
        m = 0
        for numb in range(n):
            numb = tk.Entry(self.frame2, text=self.get_input(n), width=15)
            print(numb)
            numb.config(font=("Courier", 8))
            numb.grid(row=4, column=0 + m)
            m += 1
            names.append(numb)

        confirm_button = Button(self.frame2, text="ZAPISZ", command=lambda: self.get_input(n))
        confirm_button.grid(row=4, column=1 + m)

    def get_all_media_meter_ArCHIUM(self):
        list = ['id', 'okres rozliczeniowy', 'dzien dzisiejszy', 'woda licznik dom', 'woda licznik gora',
                'woda licznik gabinet', 'woda zuzycie caly dom', 'woda zuzycie gora', 'woda zuzycie gabinet',
                'woda zuzycie dol']

        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        for e in count:
            if e > 0:
                try:
                    sqlite_select_query = """SELECT * FROM water"""
                    self.cursor.execute(sqlite_select_query)
                    records = self.cursor.fetchall()
                    n = 0
                    for row in records:
                        print(f'ZUŻYCIE: ')
                        for e in row:
                            print(f'{list[n]}: {e}')
                            n += 1
                        n = 0
                        input('Wciśnij enter by kontynuować.')
                        print('\n' * 50)
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
            else:
                input('Nie ma jeszcze wpisów w "stany liczników\n'
                      'Wciśnij enter')

    def get_all_media_meter(self):
        list = ['id', 'okres rozliczeniowy', 'dzien dzisiejszy', 'woda licznik dom', 'woda licznik gora',
                'woda licznik gabinet', 'woda zuzycie caly dom', 'woda zuzycie gora', 'woda zuzycie gabinet',
                'woda zuzycie dol']

        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        for e in count:
            if e > 0:
                try:
                    sqlite_select_query = """SELECT * FROM water"""
                    self.cursor.execute(sqlite_select_query)
                    records = self.cursor.fetchall()
                    n = 0
                    for row in records:
                        print(f'ZUŻYCIE: ')
                        for e in row:
                            print(f'{list[n]}: {e}')
                            n += 1
                        n = 0
                        input('Wciśnij enter by kontynuować.')
                        print('\n' * 50)
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)
            else:
                input('Nie ma jeszcze wpisów w "stany liczników\n'
                      'Wciśnij enter')

    def create_table(self):
        pass
