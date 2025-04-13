import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="snake_game_db",   # создадим такую базу, если ещё нет
    user="postgres",
    password="qazplm123"
)

cur = conn.cursor()

#user
cur.execute("""
CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE
)
""")

#user_score
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user"(id),
    score INTEGER,
    level INTEGER,
    date_played TIMESTAMP DEFAULT current_timestamp
)
""")

conn.commit()
cur.close()
conn.close()

print("Таблицы созданы!")