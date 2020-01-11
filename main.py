from window import *
import database_creator


def main():
    database_creator.payments_database()
    database_creator.water_invoice_database()
    database_creator.water_database()
    rach_window = Window()
    rach_window.start()


if __name__ == "__main__":
    main()
