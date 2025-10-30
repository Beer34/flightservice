from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# --------------------------------------------
# Database Configuration (from environment vars)
# --------------------------------------------
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_USER = os.getenv('DB_USER', 'flightuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'StrongUserPass123')
DB_NAME = os.getenv('DB_NAME', 'flightdb')


# --------------------------------------------
# Database Connection Helper
# --------------------------------------------
def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection


# --------------------------------------------
# API Routes
# --------------------------------------------

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to FlightService API ✈️",
        "endpoints": {
            "GET /flights": "List all flights",
            "POST /flights": "Add a new flight"
        }
    })


@app.route('/flights', methods=['GET'])
def get_flights():
    """Retrieve all flights from database"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flights;")
    flights = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(flights)


@app.route('/flights', methods=['POST'])
def add_flight():
    """Add a new flight"""
    data = request.get_json()
    flight_number = data.get('flight_number')
    origin = data.get('origin')
    destination = data.get('destination')
    departure_time = data.get('departure_time')
    arrival_time = data.get('arrival_time')

    if not (flight_number and origin and destination):
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (flight_number, origin, destination, departure_time, arrival_time)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Flight added successfully"}), 201


# --------------------------------------------
# Health Check Endpoint
# --------------------------------------------
@app.route('/health')
def health_check():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.close()
        conn.close()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


# --------------------------------------------
# Main Entry Point
# --------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

