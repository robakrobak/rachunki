import tkinter as tk
import woda
import prad
import gaz
import choice_panel


# import pandas as pd
# from database.database_water import water_database, water_invoice_database, payments_database


class Window:
    def __init__(self):  # wrzucam w mastera główną funkcję: tk.Tk(), czyli tkinter.Tk() - czyli ROOT
        self.root = tk.Tk()
        self.root.wm_title('ROZLICZENIE MEDIÓW - NA STOKU')
        self.root.geometry("1800x1200")

        self.topFrame = tk.Frame(self.root, width=900, height=600)
        self.topFrame.grid(row=0, column=0, padx=10, pady=2)

        self.botFrame = tk.Frame(self.root, width=900, height=600)
        self.botFrame.grid(row=1, column=0, padx=10, pady=2)

        self.choicePanel = choice_panel.ChoicePanel(self.root, self.topFrame)
        self.wodaPanel = woda.Woda(self.root, self.botFrame)
        # self.pradPanel = prad.Prad(self.root, self.botFrame)
        # self.gazPanel = gaz.Gaz(self.root, self.botFrame)

    def start(self):
        self.root.mainloop()
