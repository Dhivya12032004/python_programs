import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="D@2004",  
)


cursor = conn.cursor()
print("MySQL connection successful!")


cursor.execute("CREATE DATABASE IF NOT EXISTS construction_site")
cursor.execute("USE construction_site")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        project_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        location VARCHAR(100),
        budget INT
    )
""")
print("Table 'projects' created or already exists.")

cursor.execute("INSERT INTO projects (name, location, budget) VALUES (%s, %s, %s)", 
               ("Skyline Towers", "Chennai", 5000000))
cursor.execute("INSERT INTO projects (name, location, budget) VALUES (%s, %s, %s)", 
               ("Green Homes", "Coimbatore", 3000000))

conn.commit()
print("Sample records inserted.")


cursor.execute("SELECT * FROM projects")
rows = cursor.fetchall()

print("\nProject Details:")
for row in rows:
    print(row)

cursor.close()
conn.close()
print("\nMySQL connection closed.")

