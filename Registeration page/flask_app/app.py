from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='templates')

# SQLite database connection
conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT, password TEXT)')
print("Table created successfully")
conn.close()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Access form data using request.form
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Save data to SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()
        
        return 'Registration Successful!'
    else:
        # Handle GET request (render the registration form)
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
