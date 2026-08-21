import sqlite3

connection = sqlite3.connect("patient_database.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        date_of_birth TEXT NOT NULL
    )
""")

def save_patient(patient):
    cursor.execute("""
        INSERT INTO patients (
        first_name,
        last_name,
        gender,
        date_of_birth
        )
        VALUES (?, ?, ?, ?)
    """, (
        patient.first_name,
        patient.last_name,
        patient.gender,
        patient.date_of_birth
    ))

    connection.commit()