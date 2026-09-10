import mysql.connector

maakoodi = input("Anna maakoodi (esim. FI): ").upper()
yhteys = mysql.connector.connect(
    host="localhost",
    database="flight_game",
    user="root",
    password="6969"
)
kursori = yhteys.cursor()
sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
"""
kursori.execute(sql, (maakoodi,))
tulokset = kursori.fetchall()
for tyyppi, maara in tulokset:
    print(f"{tyyppi}: {maara} kappaletta")
