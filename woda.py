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

    def get_data_from_queries_last_water(self):
        try:
            last_row_water1 = """SELECT * FROM water ORDER BY id DESC LIMIT 0, 1;"""
            self.cursor.execute(last_row_water1)
            record = self.cursor.fetchall()
            for row in record:
                last_row_water = row
            self.last_row_water = list(last_row_water)


        except UnboundLocalError as error:
            input('Błąd z get_data_from_queries_last_water')

    def get_data_from_queries_before_last_water(self):
        try:
            before_last_row_water1 = """SELECT * FROM water ORDER BY id DESC LIMIT 0, 2;"""
            self.cursor.execute(before_last_row_water1)
            record = self.cursor.fetchall()
            for row in record:
                before_last_row_water = row
            self.before_last_row_water = list(before_last_row_water)

        except UnboundLocalError as error:
            print('Pewnie nie ma jeszcze wpisów w bazie danych, które umożliwią wykonanie polecenia.\n'
                  'Lub błąd z get data from queries before last water')

    def create_water_database_menu(self):
        # tworzymy grupę kolumn
        self.columns_first_group()
        # tworzymy nazwy kolumn
        self.columns_name_water()
        # ciągniemy z bazy danych archiwalne wpisy
        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        if count != 0:
            self.get_all_media_meter()
        # wpisujemy dane - zdobywamy dane
        self.new_entry()

    def columns_first_group(self):
        # okres rozliczeniowy
        okres_rozliczeniowy_label = tk.Label(self.frame2, text='OKRES ROZLICZENIOWY', padx=10, pady=10, relief='raised',
                                             highlightbackground='dark olive green',
                                             highlightthickness=1,
                                             border='1',
                                             borderwidth=1, width=29)
        okres_rozliczeniowy_label.config(font=("Courier", 8))
        okres_rozliczeniowy_label.grid(row=3, column=2, columnspan=2, pady=4)

        # stan licznikow
        stan_licznikow_label = tk.Label(self.frame2, text='STAN LICZNIKÓW', padx=10, pady=10, relief='raised',
                                        highlightbackground='salmon',
                                        highlightthickness=1,
                                        border='1',
                                        borderwidth=1, width=35)
        stan_licznikow_label.config(font=("Courier", 8))
        stan_licznikow_label.grid(row=3, column=4, columnspan=3, pady=4)

        # ZUŻYCIE
        zuzycie_mediow_label = tk.Label(self.frame2, text='ZUŻYCIE WODY', padx=10, pady=10, relief='raised',
                                        highlightbackground='DeepSkyBlue2',
                                        highlightthickness=1,
                                        border='1',
                                        borderwidth=1, width=47)
        zuzycie_mediow_label.config(font=("Courier", 8))
        zuzycie_mediow_label.grid(row=3, column=7, columnspan=4, pady=4)

    def columns_name_water(self):
        # ID
        column_id = tk.Label(self.frame2, text='ID', padx=4, pady=10, relief='raised', border='1', borderwidth=2,
                             width=6)
        column_id.config(font=('Tahoma', 8))
        column_id.grid(row=4, column=0, padx=4, pady=4)

        # DATA ODCZYTU
        column_data_odczytu = tk.Label(self.frame2, text='DATA ODCZYTU', padx=4, pady=10, relief='raised', border='1',
                                       borderwidth=2,
                                       width=14)
        column_data_odczytu.config(font=('Tahoma', 8))
        column_data_odczytu.grid(row=4, column=1, padx=4)

        # ROK
        column_rok = tk.Label(self.frame2, text='ROK', padx=4, pady=10, relief='raised', border='1',
                              borderwidth=2, highlightbackground='dark olive green',
                              highlightthickness=1,
                              width=10)
        column_rok.config(font=('Tahoma', 8))
        column_rok.grid(row=4, column=2, padx=4)

        # MIESIĄCE
        column_data_miesiace = tk.Label(self.frame2, text='MIESIĄCE', padx=4, pady=10, relief='raised', border='1',
                                        borderwidth=2, highlightbackground='dark olive green',
                                        highlightthickness=1,
                                        width=16)
        column_data_miesiace.config(font=('Tahoma', 8))
        column_data_miesiace.grid(row=4, column=3, padx=4)

        # DOM STAN LICZNIKÓW
        column_dom_stan_licznikow = tk.Label(self.frame2, text='DOM', padx=4, pady=10, relief='raised', border='1',
                                             borderwidth=2, highlightbackground='salmon',
                                             highlightthickness=1,
                                             width=10)
        column_dom_stan_licznikow.config(font=('Tahoma', 8))
        column_dom_stan_licznikow.grid(row=4, column=4, padx=4)

        # GÓRA STAN LICZNIKÓW
        column_gora_stan_licznikow = tk.Label(self.frame2, text='GÓRA', padx=4, pady=10, relief='raised', border='1',
                                              borderwidth=2, highlightbackground='salmon',
                                              highlightthickness=1,
                                              width=10)
        column_gora_stan_licznikow.config(font=('Tahoma', 8))
        column_gora_stan_licznikow.grid(row=4, column=5, padx=4)

        # GABINET STAN LICZNIKÓW
        column_gabinet_stan_licznikow = tk.Label(self.frame2, text='GABINET', padx=4, pady=10, relief='raised',
                                                 border='1',
                                                 borderwidth=2, highlightbackground='salmon',
                                                 highlightthickness=1,
                                                 width=10)
        column_gabinet_stan_licznikow.config(font=('Tahoma', 8))
        column_gabinet_stan_licznikow.grid(row=4, column=6, padx=4)

        # GÓRA ZUZYCIE
        column_gora_zuzycie = tk.Label(self.frame2, text='GÓRA', padx=4, pady=10, relief='raised', border='1',
                                       borderwidth=2, highlightbackground='DeepSkyBlue2',
                                       highlightthickness=1,
                                       width=10)
        column_gora_zuzycie.config(font=('Tahoma', 8))
        column_gora_zuzycie.grid(row=4, column=7, padx=4)

        # GABINET ZUZYCIE
        column_gabinet_zuzycie = tk.Label(self.frame2, text='GABINET', padx=4, pady=10, relief='raised',
                                          border='1',
                                          borderwidth=2, highlightbackground='DeepSkyBlue2',
                                          highlightthickness=1,
                                          width=10)
        column_gabinet_zuzycie.config(font=('Tahoma', 8))
        column_gabinet_zuzycie.grid(row=4, column=8, padx=4)

        # DOL ZUZYCIE
        column_dol = tk.Label(self.frame2, text='DÓŁ', padx=4, pady=10, relief='raised',
                              border='1',
                              borderwidth=2, highlightbackground='DeepSkyBlue2',
                              highlightthickness=1,
                              width=10)
        column_dol.config(font=('Tahoma', 8))
        column_dol.grid(row=4, column=9, padx=4)

        # DOM ZUZYCIE
        column_dom_zuzycie = tk.Label(self.frame2, text='DOM', padx=4, pady=10, relief='raised', border='1',
                                      borderwidth=2, highlightbackground='SteelBlue4',
                                      highlightthickness=1,
                                      width=10)
        column_dom_zuzycie.config(font=('Tahoma', 8))
        column_dom_zuzycie.grid(row=4, column=10, padx=4)

    # def get_input(self, n):
    #     text_input = []
    #     m = 0
    #     a = self.names[0]
    #     print('self.names: ', self.names)
    #     print('self.names[0]: ', self.names[0])
    #
    #     for e in self.names:
    #         print('for e in self.names print e: ', e)
    #         get_input = self.names[0].get()
    #         text_input.append(get_input)
    #         m += 1
    #         print('get input:', get_input)
    #         print('text_input:', text_input)

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

    def new_entry(self):
        # sprawdzam czy mam wiecej niz 1 wpis i moge wyliczać stan licznikow
        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        print('count', count)

        # pola do wpisywania danych
        self.data_odczytu = tk.Entry(self.frame2, width=5)
        self.data_odczytu.config(font=("Courier", 8))
        self.data_odczytu.grid(row=5, column=1, padx=4, sticky='WE')

        self.rok = tk.Entry(self.frame2, width=5)
        self.rok.config(font=("Courier", 8))
        self.rok.grid(row=5, column=2, padx=4, sticky='WE')

        self.miesiace = tk.Entry(self.frame2, width=5)
        self.miesiace.config(font=("Courier", 8))
        self.miesiace.grid(row=5, column=3, padx=4, sticky='WE')

        self.ldom = tk.Entry(self.frame2, width=5)
        self.ldom.config(font=("Courier", 8))
        self.ldom.grid(row=5, column=4, padx=4, sticky='WE')

        self.lgora = tk.Entry(self.frame2, width=5)
        self.lgora.config(font=("Courier", 8))
        self.lgora.grid(row=5, column=5, padx=4, sticky='WE')

        self.lgabinet = tk.Entry(self.frame2, width=5)
        self.lgabinet.config(font=("Courier", 8))
        self.lgabinet.grid(row=5, column=6, padx=4, sticky='WE')

        if count[0] == 0:
            self.gora = tk.Entry(self.frame2, width=5)
            self.gora.config(font=("Courier", 8))
            self.gora.grid(row=5, column=7, padx=4, sticky='WE')

            self.gabinet = tk.Entry(self.frame2, width=5)
            self.gabinet.config(font=("Courier", 8))
            self.gabinet.grid(row=5, column=8, padx=4, sticky='WE')

            self.dol = tk.Entry(self.frame2, width=5)
            self.dol.config(font=("Courier", 8))
            self.dol.grid(row=5, column=9, padx=4, sticky='WE')

            self.dom = tk.Entry(self.frame2, width=5)
            self.dom.config(font=("Courier", 8))
            self.dom.grid(row=5, column=10, padx=4, sticky='WE')

        confirm_button = Button(self.frame2, text="ZAPISZ", command=lambda: self.submit())
        confirm_button.grid(row=5, column=11)

    def submit(self):
        names = []

        names.append(self.data_odczytu.get())
        names.append(self.rok.get())
        names.append(self.miesiace.get())
        names.append(self.ldom.get())
        names.append(self.lgora.get())
        names.append(self.lgabinet.get())

        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        if count[0] == 0:
            names.append(self.gora.get())
            self.gora.destroy()
            names.append(self.gabinet.get())
            self.gabinet.destroy()
            names.append(self.dol.get())
            self.dol.destroy()
            names.append(self.dom.get())
            self.dom.destroy()

        self.water_db_insert_values(names)

    def water_db_insert_values(self, names):
        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()

        if count[0] != 0:
            self.get_data_from_queries_last_water()

            # gora zuzycie
            names.append(int(names[4]) - self.last_row_water[5])
            # gabinet zuzycie
            names.append(int(names[5]) - self.last_row_water[6])
            # doł zuzycie
            names.append((int(names[6]) + int(names[7])) - self.last_row_water[9])
            # dom_zuzycie
            names.append(int(names[3])-self.last_row_water[4])

        data_tuple = tuple(names)

        sqlite_insert_query = """INSERT INTO water (DATA_ODCZYTU, ROK, OKRES, DOM_LICZNIK, GÓRA_LICZNIK, 
                    GABINET_LICZNIK, GÓRA_ZUŻYCIE, GABINET_ZUŻYCIE, DÓŁ_ZUŻYCIE, DOM_ZUŻYCIE) 
                    VALUES (?,?,?,?,?,?,?,?,?,?);"""

        self.cursor.execute(sqlite_insert_query, data_tuple)
        self.conn.commit()

        self.get_all_media_meter()
        # self.water_payment_values()

    def get_all_media_meter(self):
        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()

        for e in count:
            if e > 0:
                try:
                    sqlite_select_query = """SELECT * FROM water ORDER BY id DESC;"""
                    self.cursor.execute(sqlite_select_query)
                    records = self.cursor.fetchall()
                    n = 0
                    m = 0
                    for row in records:
                        for e in row:
                            label = tk.Label(self.frame2, text=e, padx=4, pady=10, relief='raised', border='1',
                                             borderwidth=2,
                                             width=6)
                            label.config(font=('Courier', 8))
                            label.grid(row=6 + m, column=0 + n, padx=4, sticky='WE')
                            n += 1
                        m += 1
                        n = 0
                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)

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

    # def water_meter_values(self):
    #     # pobieram dane z poprzednich faktur, by obliczyć faktyczne zużycie mediów
    #     self.get_data_from_queries_last_water()
    #     # NADAJĘ ZMIENNE BY WPISAĆ DO BAZY DANYCH
    #     # okres_rozliczeniowy = MediaMeter.okres_rozliczeniowy(self)
    #     # dzień dzisiejszy
    #     # dzien_dzisiejszy = self.todays_date
    #     # DOM WODA LICZNIK
    #     dom_woda_licznik = int(input('Wpisz stan licznika DOM: '))
    #     # GORA WODA LICZNIK
    #     gora_woda_licznik = int(input('Wpisz stan licznika GÓRA: '))
    #     # GABINET WODA LICZNIK
    #     gabinet_woda_licznik = int(input('Wpisz stan licznika GABINET: '))
    #     # DOM_WODA_ZUZYCIE
    #
    #     try:
    #         ab = self.last_row_water[3]
    #         print('ab', ab)
    #         print('dom woda licznik', dom_woda_licznik)
    #         dom_woda_zuzycie = dom_woda_licznik - ab
    #         # GORA_WODA_ZUZYCIE
    #         bb = self.last_row_water[4]
    #         gora_woda_zuzycie = gora_woda_licznik - bb
    #         # GABINET WODA ZUZYCIE
    #         cb = self.last_row_water[5]
    #         gabinet_woda_zuzycie = gabinet_woda_licznik - cb
    #         # DÓŁ WODA ZUZYCIE
    #         dol_woda_zuzycie = dom_woda_zuzycie - (gora_woda_zuzycie + gabinet_woda_zuzycie)
    #     except AttributeError as error:
    #         dom_woda_zuzycie = input('Podaj zużycie wody dla całego domu.')
    #         gora_woda_zuzycie = input('Podaj zużycie wody dla gory.')
    #         gabinet_woda_zuzycie = input('Podaj zużycie wody dla gabinetu.')
    #         dol_woda_zuzycie = input('Podaj zużycie wody dla dołu - Mikołaj.')
    #
    #     check = str(input('Czy dane zostały wprowadzone poprawnie? T/N: '))
    #     if check == 'T' or check == 't':
    #         MediaMeter.water_db_insert_values(self, okres_rozliczeniowy, dzien_dzisiejszy, dom_woda_licznik,
    #                                           gora_woda_licznik, gabinet_woda_licznik, dom_woda_zuzycie,
    #                                           gora_woda_zuzycie, gabinet_woda_zuzycie, dol_woda_zuzycie)
    #     elif check == 'N' or check == 'n':
    #         MediaMeter.water_meter_values()
