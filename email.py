import sqlite3

def register_user(email, name, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        print("Error: Email already registered.")
        return

    # Insert new user
    cursor.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)",
                   (email, name, password))
    conn.commit()
    print("Registration successful!")

    conn.close()

# Example usage
register_user('test@example.com', 'John Doe', 'securepassword')
