import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
 nome text, cidade text, estrela real, diaria real)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hoteis', 'Nova Petropolis', 4.8, 309.95)"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()