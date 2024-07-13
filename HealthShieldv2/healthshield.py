from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import gocept.pseudonymize
import secrets

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  # Replace with your MySQL host
app.config['MYSQL_USER'] = 'arnold7800'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '7800'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'PatientsDetails'  # Replace with your MySQL database name

mysql = MySQL(app)

def reverse_name(pseudonymized_name, secret):
    return gocept.pseudonymize.name(pseudonymized_name, secret)

def reverse_integer(pseudonymized_integer, secret):
    return gocept.pseudonymize.integer(pseudonymized_integer, secret)


secret = secrets.token_hex(32)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_name = request.form['username']
        age = request.form['Age']
        height = request.form['Height']
        weight = request.form['Weight']
        pulse_rate = request.form['Pulse Rate']

        # Data psuedonymizaton

        ps_full_name = gocept.pseudonymize.name(full_name, 'secret')
        ps_age = gocept.pseudonymize.integer(age, 'secret')
        ps_height = gocept.pseudonymize.integer(height, 'secret')
        ps_weight = gocept.pseudonymize.integer(weight, 'secret')
        ps_pulse_rate = gocept.pseudonymize.integer(pulse_rate, 'secret')

        # Create a cursor
        cur = mysql.connection.cursor()
        
        # Insert data into MySQL
        cur.execute("INSERT INTO patients_details (full_name, age, height, weight, pulse_rate) VALUES (%s, %s, %s, %s, %s)",
                    (ps_full_name, ps_age, ps_height, ps_weight, ps_pulse_rate))
        
        # Commit transaction
        mysql.connection.commit()

         # Close cursor
        cur.close()

        return 'Form submitted successfully and data inserted into MySQL!'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
