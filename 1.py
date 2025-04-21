import psycopg2
import csv
import json

try:
    conn = psycopg2.connect(
        dbname = "phonebook2",
        user = "postgres",
        password = "erketaika11",
        host = "localhost"
    )
except psycopg2.Error as e:
    print("Error in connecting:", e)
    exit()

#Adding or updating new contacts
def insert_or_update_user():
    name = input("Enter first name:")
    surname = input("Enter last name:")
    phone = input("Enter phone number:")
    email = input("Enter email:")
    