import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="erketaika11",
    host="localhost"
)

cur = conn.cursor()

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
    print("\n1. Add contact\n2. Show all\n3. Update\n4. Delete\n5. Exit")
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
        break
    else:
        print("Invalid choice!")

cur.close()
conn.close()
