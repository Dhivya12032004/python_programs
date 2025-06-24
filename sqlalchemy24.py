from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Use %40 instead of @ in the password
engine = create_engine("mysql+pymysql://root:D%402004@localhost/construction_site")

metadata = MetaData()

salary_table = Table(
    'salary', metadata,
    Column('emp_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(100), nullable=False),
    Column('salary', Integer, nullable=False)
)

# Create the table
try:
    metadata.create_all(engine)
    print("✅ Table 'salary' created successfully.")
except Exception as e:
    print(f"❌ Failed to create table: {e}")

# Insert sample data
try:
    with engine.connect() as conn:
        conn.execute(salary_table.insert(), {"name": "Bob", "salary": 60000})
        print("✅ Inserted sample record into 'salary'.")
except Exception as e:
    print(f"❌ Insert failed: {e}")
