from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database configuration using environment variables
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'flightuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'StrongUserPass123')
DB_NAME = os.getenv('DB_NAME', 'flightdb')

def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )
    return conn

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Flight Service"}), 200

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/flights', methods=['GET'])
def get_flights():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(flights), 200

@app.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    flight_number = data.get('flight_number')
    origin = data.get('origin')
    destination = data.get('destination')
    departure_time = data.get('departure_time')
    arrival_time = data.get('arrival_time')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time)
        VALUES (%s, %s, %s, %s, %s)
    """, (flight_number, origin, destination, departure_time, arrival_time))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Flight added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
