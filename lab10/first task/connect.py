import psycopg2

# Подключаемся к базе данных
conn = psycopg2.connect(
    host="localhost",         # База на твоём компьютере
    dbname="phonebook_db",    # Имя твоей базы данных
    user="postgres",          # Имя пользователя (обычно postgres)
    password="qazplm123"  # Твой пароль от PostgreSQL
)

# Проверка соединения
print("Успешное подключение к базе данных!")

# Закрываем соединение
conn.close()
