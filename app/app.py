from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.getenv('DB_HOST', 'mysql_db'),
    'user': os.getenv('DB_USER', 'user'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'flightdb')
}

@app.route('/')
def home():
    return "Flight Service is Running!"

@app.route('/flights')
def get_flights():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flights")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
