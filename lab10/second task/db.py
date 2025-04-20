import psycopg2

# Variable to store current user's name
current_user = ''

# Connect to PostgreSQL database 'snake_db'
connection = psycopg2.connect(
    database="phonebook_db",
    user="postgres",
    password="qazplm123",
    host="localhost"
)

query_create_table_users = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) UNIQUE
    )
"""

query_create_table_user_scores = """
    CREATE TABLE IF NOT EXISTS user_scores(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255),
        score INT,
        level INT
    )
"""

# Function to execute any SQL command
def execute_query(query):
    try:
        with connection.cursor() as cur:
            cur.execute(query)
            connection.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Ask user to enter their name
def input_user():
    global current_user
    current_user = input("Enter user name: ")

# Add a new user to the database
def add_user(name):
    command = "INSERT INTO users(user_name) VALUES(%s)"
    try:
        with connection.cursor() as cur:
            cur.execute(command, (name,))
            connection.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Check if user already exists in the database
def check_if_user_exists(name):
    command = "SELECT user_name FROM users WHERE user_name = %s"
    try:
        with connection.cursor() as cur:
            cur.execute(command, (name,))
            result = cur.fetchone()
            return result is not None
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Save or update the current score and level to the database
def add_or_update_score(score, level):
    command_check = "SELECT * FROM user_scores WHERE user_name = %s"
    command_insert = "INSERT INTO user_scores (user_name, score, level) VALUES (%s, %s, %s)"
    command_update = "UPDATE user_scores SET score = %s, level = %s WHERE user_name = %s"
    try:
        with connection.cursor() as cur:
            cur.execute(command_check, (current_user,))
            result = cur.fetchone()
            if result:
                cur.execute(command_update, (score, level, current_user))
            else:
                cur.execute(command_insert, (current_user, score, level))
            connection.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Show the user's highest level
def show_highest_level():
    command = "SELECT MAX(level) FROM user_scores WHERE user_name = %s"
    try:
        with connection.cursor() as cur:
            cur.execute(command, (current_user,))
            result = cur.fetchall()
            return result
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Run these when script starts
if __name__ == '__main__':
    # Create tables if they don't exist yet
    execute_query(query_create_table_users)
    execute_query(query_create_table_user_scores)

    input_user()
    add_or_update_score(10,2)

    connection.close()
