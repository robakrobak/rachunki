import tkinter as tk
from choice_panel import *
from tkinter import StringVar, Button
from tkinter.ttk import Combobox
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

    def fetchone(self):
        sqlite_count_query = """SELECT COUNT(*) FROM water"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        return count

    def fetchall(self):
        last_row_water1 = """SELECT * FROM water ORDER BY id DESC LIMIT 0, 1;"""
        self.cursor.execute(last_row_water1)
        record = self.cursor.fetchall()
        return record

    def get_data_from_queries_last_water(self):
        try:
            record = Woda.fetchall(self)
            for row in record:
                last_row_water = row
            self.last_row_water = list(last_row_water)

        except UnboundLocalError as error:
            input('Błąd z get_data_from_queries_last_water')

    def create_water_database_menu(self):
        # tworzymy grupy kolumn
        self.columns_first_group()
        # tworzymy nazwy kolumn
        self.columns_name_water()
        # ciągniemy z bazy danych archiwalne wpisy
        sqlite_count_query = """SELECT COUNT(*) FROM water LIMIT 10"""
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

    def new_entry(self):
        # sprawdzam czy mam wiecej niz 1 wpis i moge wyliczać stan licznikow
        count = Woda.fetchone(self)

        # pola do wpisywania danych
        data_odczytu = tk.Entry(self.frame2, width=5)
        data_odczytu.config(font=("Courier", 8))
        data_odczytu.grid(row=5, column=1, padx=4, sticky='WE')

        rok = tk.Entry(self.frame2, width=5)
        rok.config(font=("Courier", 8))
        rok.grid(row=5, column=2, padx=4, sticky='WE')

        choices = ['Grudzień/Styczeń', 'Luty/Marzec', 'Kwiecień/Maj', 'Czerwiec/Lipiec', 'Sierpień/Wrzesień',
                   'Październik/Listopad']
        # variable = StringVar(self.root)
        #
        # variable.set('Grudzień/Styczeń')
        miesiace = Combobox(self.frame2, width=5, values=choices)
        miesiace.current(0)
        miesiace.config(font=("Courier", 8))
        miesiace.grid(row=5, column=3, padx=4, sticky='WE')

        ldom = tk.Entry(self.frame2, width=5)
        ldom.config(font=("Courier", 8))
        ldom.grid(row=5, column=4, padx=4, sticky='WE')

        lgora = tk.Entry(self.frame2, width=5)
        lgora.config(font=("Courier", 8))
        lgora.grid(row=5, column=5, padx=4, sticky='WE')

        lgabinet = tk.Entry(self.frame2, width=5)
        lgabinet.config(font=("Courier", 8))
        lgabinet.grid(row=5, column=6, padx=4, sticky='WE')

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

            confirm_button = Button(self.frame2, text="ZAPISZ",
                                    command=lambda: self.submit(data_odczytu, rok, miesiace, ldom, lgora, lgabinet))
        else:
            confirm_button = Button(self.frame2, text="ZAPISZ",
                                    command=lambda: self.submit(data_odczytu, rok, miesiace, ldom, lgora, lgabinet))
        confirm_button.grid(row=5, column=11)

        # modify entry
        modify_button = tk.Button(self.frame2, text='NR ID DO ZMIANY', width=14,
                                  command=lambda: self.change_entry('water'))
        modify_button.config(font=("Courier", 8))
        modify_button.grid(row=18, column=1, sticky='WE', padx=4)

        self.modify_entry = tk.Entry(self.frame2, text='ZMIEŃ', width=6)
        self.modify_entry.config(font=("Courier", 8))
        self.modify_entry.grid(row=18, column=0, sticky='WE', padx=4)

    def submit(self, *args):
        names = []

        names.append(args[0].get())
        names.append(args[1].get())
        names.append(args[2].get())
        names.append(args[3].get())
        names.append(args[4].get())
        names.append(args[5].get())

        count = Woda.fetchone(self)
        if count[0] == 0:
            names.append(self.gora.get())
            names.append(self.gabinet.get())
            names.append(self.dol.get())
            names.append(self.dom.get())

        self.water_db_insert_values(names)

    def change_entry(self, database_name):
        notice = tk.Label(self.frame2, text='DO ZROBIENIA')
        notice.config(font=("Courier", 8))
        notice.grid(row=18, column=1, sticky='WE', padx=4)

    def water_db_insert_values(self, names):
        count = Woda.fetchone(self)

        if count[0] != 0:
            self.get_data_from_queries_last_water()

            # gora zuzycie
            names.append(int(names[4]) - self.last_row_water[5])
            # gabinet zuzycie
            names.append(int(names[5]) - self.last_row_water[6])
            # doł zuzycie
            names.append((int(names[3]) - self.last_row_water[4]) - (
                    (int(names[4]) - self.last_row_water[5]) + (int(names[5]) - self.last_row_water[6])))
            # dom_zuzycie
            names.append(int(names[3]) - self.last_row_water[4])

        data_tuple = tuple(names)

        sqlite_insert_query = """INSERT INTO water (DATA_ODCZYTU, ROK, OKRES, DOM_LICZNIK, GÓRA_LICZNIK, 
                    GABINET_LICZNIK, GÓRA_ZUŻYCIE, GABINET_ZUŻYCIE, DÓŁ_ZUŻYCIE, DOM_ZUŻYCIE) 
                    VALUES (?,?,?,?,?,?,?,?,?,?);"""

        self.cursor.execute(sqlite_insert_query, data_tuple)
        self.conn.commit()

        try:
            self.gora.destroy()
            self.gabinet.destroy()
            self.dol.destroy()
            self.dom.destroy()
        except:
            pass

        self.get_all_media_meter()
        # self.water_payment_values()

    def get_all_media_meter(self):
        count = Woda.fetchone(self)

        for e in count:
            if e > 0:
                try:
                    sqlite_select_query = """SELECT * FROM water ORDER BY id DESC LIMIT 10;"""
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

    # def modify(self):
    #     info = modify_button.grid_info()
    #     print((info["row"], info["column"]))
