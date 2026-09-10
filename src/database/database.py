import sqlite3

connection = sqlite3.connect("patient_database.db", check_same_thread=False)
cursor = connection.cursor()

# primary tables

cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        sex TEXT NOT NULL,
        date_of_birth TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical_conditions (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS allergies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

# relationship tables

cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_medical_conditions (
        patient_id INTEGER NOT NULL,
        condition_id INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (condition_id) REFERENCES medical_conditions(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_medications (
        patient_id INTEGER NOT NULL,
        medication_id INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (medication_id) REFERENCES medications(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_allergies (
        patient_id INTEGER NOT NULL,
        allergy_id INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (allergy_id) REFERENCES allergies(id)
    )
""")
#### main functions

#save a patient and return the id of the patient
def save_patient(patient):
    cursor.execute("""
        INSERT INTO patients (
        first_name,
        last_name,
        sex,
        date_of_birth
        )
        VALUES (?, ?, ?, ?)
    """, (
        patient.first_name,
        patient.last_name,
        patient.sex,
        patient.date_of_birth
    ))

    connection.commit()

    return cursor.lastrowid


#save a medical condition and return the id of the medical condition
def save_medical_condition(medical_condition):
    cursor.execute("""
        SELECT id
        FROM medical_conditions
        WHERE name = ?
    """, (medical_condition,))

    result = cursor.fetchone()

    if result:
        return result[0]
    
    cursor.execute("""
        INSERT INTO medical_conditions (name)
        VALUES (?)
    """, (medical_condition,))

    connection.commit()

    return cursor.lastrowid

#save a medication and return the id of the medication
def save_medication(medication):
    cursor.execute("""
        SELECT id
        FROM medications
        WHERE name = ?
    """, (medication,))

    result = cursor.fetchone()

    if result:
        return result[0]
        
    cursor.execute("""
        INSERT INTO medications (name)
        VALUES (?)
    """, (medication,))

    connection.commit()
    
    return cursor.lastrowid

#save an allergy and return the id of the allergy
def save_allergy(allergy):
    cursor.execute("""
        SELECT id
        FROM allergies
        WHERE name = ?
    """, (allergy,))

    result = cursor.fetchone()

    if result:
        return result[0]
        
    cursor.execute("""
        INSERT INTO allergies (name)
        VALUES (?)
    """, (allergy,))
        
    connection.commit()

    return cursor.lastrowid


### relationship functions

#save a patient id and a medical condition id to a relationship table
def link_patient_medical_condition(patient_id, condition_id):
    cursor.execute("""
        INSERT INTO patient_medical_conditions (
            patient_id, 
            condition_id
        )
        VALUES (?, ?)
    """, (patient_id, condition_id))

    connection.commit()

#save a patient id and a medication id to a relationship table
def link_patient_medication(patient_id, medication_id):
    cursor.execute("""
        INSERT INTO patient_medications (
            patient_id,
            medication_id
        )
        VALUES (?, ?)
    """, (patient_id, medication_id))

    connection.commit()


#save a patient id and an allergy id to a relationship table
def link_patient_allergy(patient_id, allergy_id):
    cursor.execute("""
        INSERT INTO patient_allergies (
        patient_id,
        allergy_id
    )
    VALUES (?, ?)
    """, (patient_id, allergy_id))

    connection.commit()


### retrieve functions

#retrieve a patient by id
def retrieve_patient_by_id(patient_id):
    cursor.execute("""
        SELECT *
        FROM patients
        WHERE id = ?
    """, (patient_id,))
    return cursor.fetchone()

#retrieve patients medical conditions by patient id
def retrieve_patient_medical_conditions_by_id(patient_id):
    cursor.execute("""
        SELECT medical_conditions.name
        FROM medical_conditions
        JOIN patient_medical_conditions 
            ON medical_conditions.id = patient_medical_conditions.condition_id
        WHERE patient_medical_conditions.patient_id = ?
    """, (patient_id,))
    return cursor.fetchall()

#retrieve patients medications by patient id
def retrieve_patient_medications_by_id(patient_id):
    cursor.execute("""
        SELECT medications.name
        FROM medications
        JOIN patient_medications
            ON medications.id = patient_medications.medication_id
        WHERE patient_medications.patient_id = ?
    """, (patient_id,))
    return cursor.fetchall()

#retrieve patients allergies by patient id
def retrieve_patient_allergies_by_id(patient_id):
    cursor.execute("""
        SELECT allergies.name
        FROM allergies
        JOIN patient_allergies
            ON allergies.id = patient_allergies.allergy_id
        WHERE patient_allergies.patient_id = ?
    """, (patient_id,))
    return cursor.fetchall()

if __name__ == "__main__":
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print(tables)

    from src.modules.patient.patient import Patient

    # test_patient = Patient(
    #     first_name="John",
    #     last_name="Doe",
    #     sex="Male",
    #     date_of_birth="1990-01-01"
    # )

    # test_patient_id = save_patient(test_patient)
    # print(test_patient_id)

    print(cursor.execute("SELECT * FROM patients").fetchall())
