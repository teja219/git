import sqlite3

# Function to create a new SQLite database and table
def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create a table named 'codes' with columns 'hashcode' and 'code'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS codes (
            hashcode TEXT PRIMARY KEY,
            code TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Function to insert a new row into the 'codes' table
def insert_code(db_file, hashcode, code):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO codes (hashcode, code) VALUES (?, ?)', (hashcode, code))
        conn.commit()
        print("Inserted successfully!")
    except sqlite3.IntegrityError:
        print(f"Hashcode '{hashcode}' already exists. Use update_code() to update the code.")
    
    conn.close()

# Function to update an existing row in the 'codes' table
def update_code(db_file, hashcode, new_code):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('UPDATE codes SET code = ? WHERE hashcode = ?', (new_code, hashcode))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Code updated successfully for hashcode '{hashcode}'!")
    else:
        print(f"Hashcode '{hashcode}' not found. Use insert_code() to add a new code.")
    
    conn.close()

# Example usage
if __name__ == '__main__':
    db_file = 'codes.db'
    create_database(db_file)
    
    # Insert new code
    insert_code(db_file, 'abc123', 'SampleCode123')
    
    # Update existing code
    update_code(db_file, 'abc123', 'UpdatedCode456')
