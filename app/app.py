from flask import Flask, jsonify
import mysql.connector
from config import get_db_config

app = Flask(__name__)

@app.route('/')
def home():
    return "Flight Service is Running!"

@app.route('/flights')
def get_flights():
    db_config = get_db_config()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flights;")
    flights = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(flights)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

