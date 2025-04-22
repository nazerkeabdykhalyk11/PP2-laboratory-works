import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="erketaika11",
    host="localhost"
)

cur = conn.cursor()

# Вставка из CSV-файла
def insert_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовки
            for row in reader:
                if len(row) == 4:  # Проверка, что строка содержит ровно 4 элемента
                    cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING
                    """, (row[0], row[1], row[2], row[3]))
            conn.commit()
        print("Data loaded from CSV!")
    except Exception as e:
        print(f"Error loading data from CSV: {e}")

# Фильтрация контактов
def filter_contacts():
    keyword = input("Enter name or phone to search: ")
    cur.execute("""
        SELECT * FROM phonebook 
        WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone ILIKE %s
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matching contacts found.")

# Добавление контакта
def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    cur.execute("""
        INSERT INTO phonebook (first_name, last_name, phone, email)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, phone, email))
    conn.commit()
    print("Contact saved!")

# Показать все контакты
def show_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

# Обновление номера телефона
def update_user():
    name = input("Whose phone to update (first name): ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    print("Phone updated!")

# Удаление пользователя
def delete_user():
    name = input("Who to delete (first name): ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    conn.commit()
    print("Contact deleted!")

# Главное меню
while True:
    print("\n1. Add contact\n2. Show all\n3. Update\n4. Delete\n5. Insert from CSV\n6. Filter\n7. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        show_all()
    elif choice == '3':
        update_user()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        path = input("Enter path to CSV file: ")
        insert_from_csv(path)
    elif choice == '6':
        filter_contacts()
    elif choice == '7':
        break
    else:
        print("Invalid choice!")

# Закрытие соединения
cur.close()
conn.close()
