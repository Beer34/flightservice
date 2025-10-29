import os

def get_db_config():
    return {
        'host': os.getenv('DB_HOST', 'mysql_db'),
        'user': os.getenv('DB_USER', 'user'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'database': os.getenv('DB_NAME', 'flightdb')
    }
