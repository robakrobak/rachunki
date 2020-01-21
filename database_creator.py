import sqlite3


def payments_database():
    conn = sqlite3.connect(("water.db"))
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS payments(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ROK INTEGER,
        OKRES VARCHAR,
        GÓRA INTEGER,
        GÓRA_OPŁACONO BOOLEAN,
        GABINET INTEGER,
        GAB_OPŁACONO BOOLEAN,
        DÓŁ INTEGER,
        DÓŁ_OPŁACONO BOOLEAN)
        """)


def water_database():
    conn = sqlite3.connect("water.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS water(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DATA_ODCZYTU DATE,
        ROK INTEGER,
        OKRES VARCHAR,
        DOM_LICZNIK INTEGER,
        GÓRA_LICZNIK INTEGER,
        GABINET_LICZNIK INTEGER,
        GÓRA_ZUŻYCIE INTEGER,
        GABINET_ZUŻYCIE INTEGER,
        DÓŁ_ZUŻYCIE INTEGER,
        DOM_ZUŻYCIE INTEGER)
        """)


def water_invoice_database():
    conn = sqlite3.connect("water.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS water_invoice(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ROK INTEGER, 
        OKRES VARCHAR,
        DATA_FAKTURA DATE, 
        WODA_ZUŻYCIE INTEGER,
        WODA_KOSZT_1M3 FLOAT,
        ILOŚĆ_ABONAM_W INTEGER,
        WODA_KOSZT_1xABON FLOAT,
        ŚCIEKI_ZUŻYCIE INTEGER,
        ŚCIEKI_KOSZT_1M3 FLOAT,
        ILOŚĆ_ABONAM_S INTEGER,
        ŚCIEKI_KOSZT_1xABON FLOAT,
        DO_ZAPŁATY FLOAT,
        OPŁACONA BOOLEAN
        )
        """)
