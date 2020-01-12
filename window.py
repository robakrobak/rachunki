import tkinter as tk

import choice_panel


# import pandas as pd
# from database.database_water import water_database, water_invoice_database, payments_database


class Window:
    def __init__(self):  # wrzucam w mastera główną funkcję: tk.Tk(), czyli tkinter.Tk() - czyli ROOT
        self.root = tk.Tk()
        self.root.wm_title('ROZLICZENIE MEDIÓW - NA STOKU')
        self.root.geometry("2580x1200")

        self.choicePanel = choice_panel.ChoicePanel(self.root)

    def start(self):
        self.root.mainloop()
