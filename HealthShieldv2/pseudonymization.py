from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from cryptography.fernet import Fernet

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'arnold7800'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '7800'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'PatientsDetails'  # Replace with your MySQL database name

mysql = MySQL(app)

# Generate a key for encryption and decryption
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

def encrypt(text):
    return cipher.encrypt(text.encode('utf-8')).decode('utf-8')

def decrypt(text):
    try:
        return cipher.decrypt(text.encode('utf-8')).decode('utf-8')
    except InvalidToken as e:
        # Handle decryption errors (e.g., log the error)
        return f"Decryption Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_name = request.form['username']
        age = request.form['Age']
        height = request.form['Height']
        weight = request.form['Weight']
        pulse_rate = request.form['Pulse Rate']

        # Data encryption
        enc_full_name = encrypt(full_name)
        enc_age = encrypt(age)
        enc_height = encrypt(height)
        enc_weight = encrypt(weight)
        enc_pulse_rate = encrypt(pulse_rate)

        # Create a cursor
        cursor = mysql.connection.cursor()
        
        # Insert encrypted data into MySQL
        cursor.execute("INSERT INTO patients_details (full_name, age, height, weight, pulse_rate) VALUES (%s, %s, %s, %s, %s)",
                       (enc_full_name, enc_age, enc_height, enc_weight, enc_pulse_rate))
        
        # Commit transaction
        mysql.connection.commit()

        # Close cursor
        cursor.close()

        return 'Form submitted successfully and data inserted into MySQL!'
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Create a cursor
    cursor = mysql.connection.cursor()
    
    # Fetch encrypted data from MySQL
    cursor.execute("SELECT full_name, age, height, weight, pulse_rate FROM patients_details")
    encrypted_data = cursor.fetchall()
    
    # Decrypt data
    decrypted_records = []
    for row in encrypted_data:
        dec_full_name = decrypt(row[0])
        dec_age = decrypt(row[1])
        dec_height = decrypt(row[2])
        dec_weight = decrypt(row[3])
        dec_pulse_rate = decrypt(row[4])
        decrypted_records.append((dec_full_name, dec_age, dec_height, dec_weight, dec_pulse_rate))
    
    # Close cursor
    cursor.close()

    return render_template('dashboard.html', data=decrypted_records)

if __name__ == '__main__':
    app.run(debug=True)
