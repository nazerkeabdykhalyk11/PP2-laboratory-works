import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="erketaika11",
    host="localhost"
)

cur = conn.cursor()

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

def filter_contacts():
    keyword = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matching contacts found.")


def add_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact saved!")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def update_user():
    name = input("Whose phone to update: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()

def delete_user():
    name = input("Who to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()

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
        insert_from_csv()
    elif choice == '6':
        filter_contacts()
    elif choice == '7':
        break
    else:
        print("Invalid choice!")


cur.close()
conn.close()
