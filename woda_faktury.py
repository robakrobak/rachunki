import tkinter as tk
from choice_panel import *
from tkinter import StringVar, Button
from tkinter.ttk import Combobox
from window import *
import sqlite3
from woda import *


class WodaFaktury:
    def __init__(self, root):
        self.frame3 = tk.Frame(root, width=1900, height=600)
        self.frame3.grid(row='1', column='0', sticky="nw", pady=40)

        # obsługa bazy danych
        self.conn = sqlite3.connect("water.db")
        self.cursor = self.conn.cursor()

        self.create_water_invoice_menu()

    def close_all_buttons_frame2(self):
        for widget in Woda.close_all_buttons_frame2():
            widget.destroy()

    def count_rows(self):
        sqlite_count_query = """SELECT COUNT(*) FROM water_invoice"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        return count

    def select_last_record_from_database(self):
        last_row_water1 = """SELECT * FROM water_invoice ORDER BY id DESC LIMIT 0, 1;"""
        self.cursor.execute(last_row_water1)
        record = self.cursor.fetchall()
        return record

    def create_water_invoice_menu(self):
        # tworzymy grupy kolumn
        self.columns_first_group()
        # tworzymy nazwy kolumn
        self.columns_name_invoice()
        # ciągniemy z bazy danych archiwalne wpisy
        sqlite_count_query = """SELECT COUNT(*) FROM water LIMIT 10"""
        self.cursor.execute(sqlite_count_query)
        count = self.cursor.fetchone()
        if count != 0:
            self.get_all_invoice_meter()
        # wpisujemy dane - zdobywamy dane
        self.new_entry()

    def columns_first_group(self):
        # okres rozliczeniowy
        okres_rozliczeniowy_label = tk.Label(self.frame3, text='OKRES ROZLICZENIOWY', padx=10, pady=10, relief='raised',
                                             highlightbackground='dark olive green',
                                             highlightthickness=1,
                                             border='1',
                                             borderwidth=1, width=29)
        okres_rozliczeniowy_label.config(font=("Courier", 8))
        okres_rozliczeniowy_label.grid(row=3, column=1, columnspan=2, pady=4)

        # stan licznikow
        stan_licznikow_label = tk.Label(self.frame3, text='ROZLICZENIA WODA', padx=10, pady=10, relief='raised',
                                        highlightbackground='DeepSkyBlue2',
                                        highlightthickness=1,
                                        border='1',
                                        borderwidth=1, width=47)
        stan_licznikow_label.config(font=("Courier", 8))
        stan_licznikow_label.grid(row=3, column=4, columnspan=4, pady=4)

        # ZUŻYCIE
        zuzycie_mediow_label = tk.Label(self.frame3, text='ROZLICZENIA ŚCIEKI', padx=10, pady=10, relief='raised',
                                        highlightbackground='salmon',
                                        highlightthickness=1,
                                        border='1',
                                        borderwidth=1, width=47)
        zuzycie_mediow_label.config(font=("Courier", 8))
        zuzycie_mediow_label.grid(row=3, column=8, columnspan=4, pady=4)

    def columns_name_invoice(self):
        # ID
        column_id = tk.Label(self.frame3, text='ID', padx=4, pady=10, relief='raised', border='1', borderwidth=2,
                             width=6)
        column_id.config(font=('Tahoma', 8))
        column_id.grid(row=4, column=0, padx=4, pady=4)

        # ROK
        column_rok = tk.Label(self.frame3, text='ROK', padx=4, pady=10, relief='raised', border='1',
                              borderwidth=2, highlightbackground='dark olive green',
                              highlightthickness=1,
                              width=10)
        column_rok.config(font=('Tahoma', 8))
        column_rok.grid(row=4, column=1, padx=4)

        # MIESIĄCE
        column_data_miesiace = tk.Label(self.frame3, text='MIESIĄCE', padx=4, pady=10, relief='raised', border='1',
                                        borderwidth=2, highlightbackground='dark olive green',
                                        highlightthickness=1,
                                        width=16)
        column_data_miesiace.config(font=('Tahoma', 8))
        column_data_miesiace.grid(row=4, column=2, padx=4)

        # DATA FAKTURY
        column_dom_stan_licznikow = tk.Label(self.frame3, text='DATA FAKTURY', padx=4, pady=10, relief='raised',
                                             border='1',
                                             borderwidth=2, highlightbackground='green',
                                             highlightthickness=1,
                                             width=14)
        column_dom_stan_licznikow.config(font=('Tahoma', 8))
        column_dom_stan_licznikow.grid(row=4, column=3, padx=4)

        # WODA ZUŻYCIE
        column_gora_stan_licznikow = tk.Label(self.frame3, text='ZUŻYCIE', padx=4, pady=10, relief='raised', border='1',
                                              borderwidth=2, highlightbackground='DeepSkyBlue2',
                                              highlightthickness=1,
                                              width=10)
        column_gora_stan_licznikow.config(font=('Tahoma', 8))
        column_gora_stan_licznikow.grid(row=4, column=4, padx=4)

        # WODA KOSZT 1M3
        column_gabinet_stan_licznikow = tk.Label(self.frame3, text='KOSZT 1m3', padx=4, pady=10, relief='raised',
                                                 border='1',
                                                 borderwidth=2, highlightbackground='DeepSkyBlue2',
                                                 highlightthickness=1,
                                                 width=10)
        column_gabinet_stan_licznikow.config(font=('Tahoma', 8))
        column_gabinet_stan_licznikow.grid(row=4, column=5, padx=4)

        # ILOŚĆ ABONAMENTÓW
        column_gora_zuzycie = tk.Label(self.frame3, text='IL.ABON.', padx=4, pady=10, relief='raised', border='1',
                                       borderwidth=2, highlightbackground='DeepSkyBlue2',
                                       highlightthickness=1,
                                       width=10)
        column_gora_zuzycie.config(font=('Tahoma', 8))
        column_gora_zuzycie.grid(row=4, column=6, padx=4)

        # WODA KOSZT ABONAMENT X1
        column_gabinet_zuzycie = tk.Label(self.frame3, text='1 ABON.', padx=4, pady=10, relief='raised',
                                          border='1',
                                          borderwidth=2, highlightbackground='DeepSkyBlue2',
                                          highlightthickness=1,
                                          width=10)
        column_gabinet_zuzycie.config(font=('Tahoma', 8))
        column_gabinet_zuzycie.grid(row=4, column=7, padx=4)

        # SCIEKI ZUŻYCIE
        column_gora_stan_licznikow = tk.Label(self.frame3, text='ZUŻYCIE', padx=4, pady=10, relief='raised', border='1',
                                              borderwidth=2, highlightbackground='salmon',
                                              highlightthickness=1,
                                              width=10)
        column_gora_stan_licznikow.config(font=('Tahoma', 8))
        column_gora_stan_licznikow.grid(row=4, column=8, padx=4)

        # SCIEKI KOSZT 1M3
        column_gabinet_stan_licznikow = tk.Label(self.frame3, text='KOSZT 1m3', padx=4, pady=10, relief='raised',
                                                 border='1',
                                                 borderwidth=2, highlightbackground='salmon',
                                                 highlightthickness=1,
                                                 width=10)
        column_gabinet_stan_licznikow.config(font=('Tahoma', 8))
        column_gabinet_stan_licznikow.grid(row=4, column=9, padx=4)

        # SCIEKI ILOŚĆ ABONAMENTÓW
        column_gora_zuzycie = tk.Label(self.frame3, text='IL.ABON.', padx=4, pady=10, relief='raised', border='1',
                                       borderwidth=2, highlightbackground='salmon',
                                       highlightthickness=1,
                                       width=10)
        column_gora_zuzycie.config(font=('Tahoma', 8))
        column_gora_zuzycie.grid(row=4, column=10, padx=4)

        # SCIEKI KOSZT ABONAMENT X1
        column_gabinet_zuzycie = tk.Label(self.frame3, text='1 ABON.', padx=4, pady=10, relief='raised',
                                          border='1',
                                          borderwidth=2, highlightbackground='salmon',
                                          highlightthickness=1,
                                          width=10)
        column_gabinet_zuzycie.config(font=('Tahoma', 8))
        column_gabinet_zuzycie.grid(row=4, column=11, padx=4)

        # DO ZAPŁATY
        do_zaplaty = tk.Label(self.frame3, text='DO ZAPŁATY', padx=4, pady=10, relief='raised',
                              border='1',
                              borderwidth=2, highlightbackground='green',
                              highlightthickness=1,
                              width=10)
        do_zaplaty.config(font=('Tahoma', 8))
        do_zaplaty.grid(row=4, column=12, padx=4)

        # OPLACONA
        oplacona = tk.Label(self.frame3, text='OPŁACONA', padx=4, pady=10, relief='raised',
                            border='1',
                            borderwidth=2, highlightbackground='salmon',
                            highlightthickness=1,
                            width=10)
        oplacona.config(font=('Tahoma', 8))
        oplacona.grid(row=4, column=13, padx=4)

    def get_all_invoice_meter(self):
        count = self.count_rows()

        for e in count:
            if e > 0:
                try:
                    sqlite_select_query = """SELECT * FROM water_invoice ORDER BY id DESC LIMIT 10;"""
                    self.cursor.execute(sqlite_select_query)
                    records = self.cursor.fetchall()
                    n = 0
                    m = 0
                    for row in records:
                        for e in row:
                            label = tk.Label(self.frame3, text=e, padx=4, pady=10, relief='raised', border='1',
                                             borderwidth=2,
                                             width=6)
                            label.config(font=('Courier', 8))
                            label.grid(row=6 + m, column=0 + n, padx=4, sticky='WE')
                            n += 1
                        m += 1
                        n = 0


                except sqlite3.Error as error:
                    print("Failed to read data from sqlite table", error)

    def new_entry(self):

        rok = tk.Entry(self.frame3, width=5)
        rok.config(font=("Courier", 8))
        rok.grid(row=5, column=1, padx=4, sticky='WE')

        choices = ['Grudzień/Styczeń', 'Luty/Marzec', 'Kwiecień/Maj', 'Czerwiec/Lipiec', 'Sierpień/Wrzesień',
                   'Październik/Listopad']

        miesiace = Combobox(self.frame3, width=5, values=choices)
        miesiace.current(0)
        miesiace.config(font=("Courier", 8))
        miesiace.grid(row=5, column=2, padx=4, sticky='WE')

        data_faktura = tk.Entry(self.frame3, width=5)
        data_faktura.config(font=("Courier", 8))
        data_faktura.grid(row=5, column=3, padx=4, sticky='WE')

        # woda
        woda_zuzycie = tk.Entry(self.frame3, width=5)
        woda_zuzycie.config(font=("Courier", 8))
        woda_zuzycie.grid(row=5, column=4, padx=4, sticky='WE')

        woda_koszt_1_m3 = tk.Entry(self.frame3, width=5)
        woda_koszt_1_m3.config(font=("Courier", 8))
        woda_koszt_1_m3.grid(row=5, column=5, padx=4, sticky='WE')

        woda_ilosc_abon = tk.Entry(self.frame3, width=5)
        woda_ilosc_abon.config(font=("Courier", 8))
        woda_ilosc_abon.grid(row=5, column=6, padx=4, sticky='WE')

        woda_koszt_abon = tk.Entry(self.frame3, width=5)
        woda_koszt_abon.config(font=("Courier", 8))
        woda_koszt_abon.grid(row=5, column=7, padx=4, sticky='WE')

        # scieki
        scieki_zuzycie = tk.Entry(self.frame3, width=5)
        scieki_zuzycie.config(font=("Courier", 8))
        scieki_zuzycie.grid(row=5, column=8, padx=4, sticky='WE')

        scieki_koszt_1_m3 = tk.Entry(self.frame3, width=5)
        scieki_koszt_1_m3.config(font=("Courier", 8))
        scieki_koszt_1_m3.grid(row=5, column=9, padx=4, sticky='WE')

        scieki_ilosc_abon = tk.Entry(self.frame3, width=5)
        scieki_ilosc_abon.config(font=("Courier", 8))
        scieki_ilosc_abon.grid(row=5, column=10, padx=4, sticky='WE')

        scieki_koszt_abon = tk.Entry(self.frame3, width=5)
        scieki_koszt_abon.config(font=("Courier", 8))
        scieki_koszt_abon.grid(row=5, column=11, padx=4, sticky='WE')

        # do zapłaty
        do_zaplaty = tk.Entry(self.frame3, width=5)
        do_zaplaty.config(font=("Courier", 8))
        do_zaplaty.grid(row=5, column=12, padx=4, sticky='WE')

        # czy oplacona
        choices_bool = ['NIE', 'TAK']

        oplacona = Combobox(self.frame3, width=5, values=choices_bool)
        oplacona.current(0)
        oplacona.config(font=("Courier", 8))
        oplacona.grid(row=5, column=13, padx=4, sticky='WE')

        confirm_button = Button(self.frame3, text="ZAPISZ",
                                command=lambda: self.submit(rok, miesiace, data_faktura, woda_zuzycie, woda_koszt_1_m3,
                                                            woda_ilosc_abon, woda_koszt_abon, scieki_zuzycie,
                                                            scieki_koszt_1_m3, scieki_ilosc_abon, scieki_koszt_abon,
                                                            do_zaplaty, oplacona))

        confirm_button.grid(row=5, column=14)

        # modify entry
        modify_button = tk.Button(self.frame3, text='NR ID DO ZMIANY', width=14,
                                  command=lambda: self.change_entry('water'))
        modify_button.config(font=("Courier", 8))
        modify_button.grid(row=18, column=1, sticky='WE', padx=4)

        self.modify_entry = tk.Entry(self.frame3, text='ZMIEŃ', width=6)
        self.modify_entry.config(font=("Courier", 8))
        self.modify_entry.grid(row=18, column=0, sticky='WE', padx=4)

    def submit(self, *args):
        names = []
        for n in args:
            names.append(n.get())

        self.water_invoice_db_insert_values(names)

    def water_invoice_db_insert_values(self, names):

        data_tuple = tuple(names)

        sqlite_insert_query = """INSERT INTO water_invoice (ROK, OKRES, DATA_FAKTURA, WODA_ZUŻYCIE, WODA_KOSZT_1M3,
        ILOŚĆ_ABONAM_W, WODA_KOSZT_1xABON, ŚCIEKI_ZUŻYCIE, ŚCIEKI_KOSZT_1M3, ILOŚĆ_ABONAM_S, ŚCIEKI_KOSZT_1xABON,
        DO_ZAPŁATY, OPŁACONA) 
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"""

        self.cursor.execute(sqlite_insert_query, data_tuple)
        self.conn.commit()

        self.get_all_invoice_meter()

