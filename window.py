import tkinter as tk
import woda


# import pandas as pd
# from database.database_water import water_database, water_invoice_database, payments_database


class Window:
    def __init__(self, master):  # wrzucam w mastera główną funkcję: tk.Tk(), czyli tkinter.Tk() - czyli ROOT
        self.master = master  # self.master jest tkinter.Tk()
        self.window_name = master.wm_title('ROZLICZENIE MEDIÓW - NA STOKU')
        self.master.geometry("1800x1200")
        self.frame = tk.Frame(self.master)

        # self.button_MEDIA = tk.Button(self.frame, text="MEDIA", width=15,
        #                               command=lambda: [self.prad_woda_gaz_buttons()]).grid(row=0, column=0)
        self.media_button()
        self.frame.grid()

    def close_all_buttons(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def media_button(self):
        self.button_MEDIA = tk.Button(self.frame, text="MEDIA", width=15,
                                      command=lambda: [self.close_all_buttons(), self.media_button(),
                                                       self.prad_woda_gaz_buttons()]).grid(row=0,
                                                                                           column=0)

    def prad_woda_gaz_buttons(self):
        self.sub_button_WODA = tk.Button(
            self.frame, text="WODA", width=15, highlightbackground='powderblue', highlightthickness=2,
            command=lambda: [self.woda_main_button(),
                             self.stan_licznikow_rozliczenia(
                                 'woda')]).grid(row=1, column=0, pady=10, padx=5)
        self.sub_button_PRAD = tk.Button(
            self.frame, text="PRĄD", width=15, highlightbackground='mistyrose', highlightthickness=2,
            command=lambda: [self.prad_main_button(),
                             self.stan_licznikow_rozliczenia(
                                 'prad')]).grid(row=1, column=1, pady=10, padx=5)

        self.sub_button_GAZ = tk.Button(
            self.frame, text="GAZ", width=15, highlightbackground='lemonchiffon', highlightthickness=2,
            command=lambda: [self.gaz_main_button(),
                             self.stan_licznikow_rozliczenia(
                                 'gaz')]).grid(row=1, column=2, pady=10, padx=5)

    def woda_main_button(self):
        self.button_WODA = tk.Button(self.frame, text='WODAa', width=15, highlightbackground='powderblue',
                                     highlightthickness=2,
                                     command=lambda: [self.close_all_buttons(), self.media_button(),
                                                      self.stan_licznikow_rozliczenia('woda')]).grid(row=0, column=1)

    def prad_main_button(self):
        self.button_PRAD = tk.Button(self.frame, text='PRADa', width=15, highlightbackground='mistyrose',
                                     highlightthickness=2,
                                     command=lambda: [self.close_all_buttons(), self.media_button(),
                                                      self.stan_licznikow_rozliczenia('prad')]).grid(row=0, column=1)

    def gaz_main_button(self):
        self.button_GAZ = tk.Button(self.frame, text='GAZa', width=15, highlightbackground='lemonchiffon',
                                    highlightthickness=2,
                                    command=lambda: [self.close_all_buttons(), self.media_button(),
                                                      self.stan_licznikow_rozliczenia('gaz')]).grid(row=0, column=1)

    def stan_licznikow_rozliczenia(self,
                                   media):  # media wejdzie do commands: będzie to przeniesienie do pliku woda, prad, lub gaz
        if media == 'gaz':
            gaz.Gaz.stan_licznikow_gaz(self)
        elif media == 'woda':
            woda.Woda.stan_licznikow_woda(self)
        elif media == 'prad':
            prad.Prad.stan_licznikow_prad(self)


