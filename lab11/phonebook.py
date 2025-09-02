import psycopg2
import csv
import json

# Подключение к базе данных PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="phonebook2",
        user="postgres",
        password="11447700",
        host="localhost"
    )
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    exit()

# 1. Добавление/обновление одного пользователя
def insert_or_update_user():
    name = input("Enter first name: ")
    surname = input("Enter last name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    cur.execute("CALL insert_or_update_user(%s, %s, %s, %s)", (name, surname, phone, email))
    conn.commit()
    print("User inserted or updated.")

# 2. Загрузка из CSV и массовая вставка через JSON
def load_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            users = [
                {
                    "name": row.get('first_name'),
                    "surname": row.get('last_name'),
                    "phone": str(row.get('phone')).strip(),
                    "email": row.get('email')
                }
                for row in reader
                if row.get('first_name') and row.get('last_name') and row.get('phone')
            ]

        cur.execute("CALL insert_many_users(%s::json)", [json.dumps(users)])
        conn.commit()
        print("Users loaded from CSV and inserted.")

    except psycopg2.Error as e:
        print("PostgreSQL error:", e.pgerror)
        conn.rollback()

    except Exception as e:
        print("Error loading from CSV:", e)




# 3. Поиск по паттерну
def search_by_pattern(pattern):
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)

# 4. Пагинация
def show_paginated(limit_count, offset_count):
    cur.execute("SELECT * FROM get_contacts_by_page(%s, %s)", (limit_count, offset_count))
    for row in cur.fetchall():
        print(row)

# 5. Удаление по имени или телефону
def delete_user_by_name_or_phone():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL delete_user(%s, %s)", (name, phone))
    conn.commit()
    print("User deleted.")

# Главное меню
while True:
    print("\n--- PhoneBook Menu ---")
    print("1. Add or update user")
    print("2. Load from CSV")
    print("3. Search by pattern")
    print("4. Show paginated")
    print("5. Delete user by name/phone")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        insert_or_update_user()
    elif choice == '2':
        file_path = input("Enter CSV file path: ")
        load_from_csv(file_path)
    elif choice == '3':
        pattern = input("Enter search pattern: ")
        search_by_pattern(pattern)
    elif choice == '4':
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        show_paginated(limit, offset)
    elif choice == '5':
        delete_user_by_name_or_phone()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")

cur.close()
conn.close()
