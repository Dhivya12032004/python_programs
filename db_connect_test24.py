import mysql.connector

# Database connection config
config = {
    "host": "localhost",
    "user": "root",
    "password": "D@2004",  # change this to your actual password
    "database": "construction_site"
}

try:
    # Step 1: Connect to MySQL
    conn = mysql.connector.connect(**config)
    print("✅ Connected to MySQL successfully!")
    cursor = conn.cursor()

    # Step 2: Create employee table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        role VARCHAR(100),
        salary DECIMAL(10, 2),
        hire_date DATE
    )
    """
    cursor.execute(create_table_query)
    print("✅ Employee table is ready.")

    # Step 3: Insert a sample record
    insert_query = """
    INSERT INTO employee (name, role, salary, hire_date)
    VALUES (%s, %s, %s, %s)
    """
    sample_data = ("John Doe", "Site Engineer", 55000.00, "2024-06-01")
    cursor.execute(insert_query, sample_data)
    conn.commit()
    print("✅ Sample employee inserted.")

    # Step 4: Fetch and display records
    cursor.execute("SELECT * FROM employee")
    results = cursor.fetchall()
    print("\n📋 Employee Records:")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"❌ Error connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔒 MySQL connection closed.")
