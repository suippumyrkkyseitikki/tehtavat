import mysql.connector

icao = input("Anna lentoaseman ICAO-koodi: ").upper()
yhteys = mysql.connector.connect(
    host="localhost",
    database="flight_game",
    user="root",
    password="6969"
)
kursori = yhteys.cursor()
sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""
kursori.execute(sql, (icao,))
tulos = kursori.fetchone()
if tulos:
    print(f"Lentokenttä: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentokenttää ei löytynyt.")