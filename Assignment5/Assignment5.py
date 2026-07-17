import sqlite3

connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()

# Remove the old table so the program can be run more than once
cursor.execute("DROP TABLE IF EXISTS Temperatures")

# Creates the table.
cursor.execute("""
    CREATE TABLE Temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# Reads lines from the input file and inserts it into the table.
with open("Assignment5input.txt", "r") as input_file:
    for line in input_file:
        day, temperature = line.split()

        cursor.execute("""
            INSERT INTO Temperatures (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        """, (day, float(temperature)))

connection.commit()

#Sundays average temperature.
cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM Temperatures
    WHERE Day_Of_Week = ?
""", ("Sunday",))

sunday_average = cursor.fetchone()[0]

#Thursdays average temperature.
cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM Temperatures
    WHERE Day_Of_Week = ?
""", ("Thursday",))

thursday_average = cursor.fetchone()[0]

print(f"Average temperature for Sunday: {sunday_average:.2f}")
print(f"Average temperature for Thursday: {thursday_average:.2f}")

connection.close()
