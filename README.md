# Flight Service Microservice

This microservice provides flight information and connects to a MySQL database. It is containerized using Docker and orchestrated using Docker Compose.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Directory Structure](#directory-structure)
3. [Environment Variables](#environment-variables)
4. [Building and Running the Services](#building-and-running-the-services)
5. [Testing the Application](#testing-the-application)
6. [Database Connectivity](#database-connectivity)
7. [Stopping and Removing Services](#stopping-and-removing-services)

---

## Prerequisites

* AWS EC2 instance (or any Linux server)
* Docker installed
* Docker Compose installed
* Git installed

---

## Directory Structure

```
flightservice/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Environment Variables

Set in `docker-compose.yml`:

```yaml
environment:
  DB_HOST: mysql_db
  DB_PORT: 3306
  DB_USER: flightuser
  DB_PASSWORD: StrongUserPass123
  DB_NAME: flightdb
```

These are used by the Flask application to connect to the MySQL database.

---

## Building and Running the Services

1. **Clone the repository**:

```bash
git clone https://github.com/Beer34/flightservice
cd flightservice
```

2. **Build Docker images**:

```bash
docker compose build
```

3. **Start the multi-container application**:

```bash
docker compose up -d
```

4. **Check running containers**:

```bash
docker compose ps
```

You should see both `flightservice` and `mysql_db` running.

---

## Testing the Application

1. Open your browser and go to:

```
http://<EC2-Public-IP>:5000
```

You should see:

```json
{"message":"Welcome to Flight Service"}
```

2. Access the flights endpoint:

```
http://<EC2-Public-IP>:5000/flights
```

You should see a list of flights from the database:

```json
[
  {"id": 1, "flight_number": "AI101", "origin": "Delhi", "destination": "London"},
  {"id": 2, "flight_number": "BA202", "origin": "London", "destination": "New York"}
]
```

---

## Database Connectivity

The MySQL database is running in a separate container (`mysql_db`).

* Connect to the database:

```bash
docker exec -it mysql_db mysql -u flightuser -p
# Enter password: StrongUserPass123
```

* Use the `flightdb` database:

```sql
USE flightdb;
SHOW TABLES;
```

* Sample table creation (already preloaded):

```sql
CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10),
    origin VARCHAR(50),
    destination VARCHAR(50)
);

INSERT INTO flights (flight_number, origin, destination)
VALUES ('AI101', 'Delhi', 'London'), ('BA202', 'London', 'New York');
```

---

## Stopping and Removing Services

1. Stop running containers:

```bash
docker compose down
```

2. To also remove volumes (including database data):

```bash
docker compose down -v
```

3. Clean up unused images and containers:

```bash
docker system prune -a
```

> ⚠️ Be careful: `docker system prune -a` will remove all unused images and stopped containers.

---

## Notes

* The `flightservice` container depends on `mysql_db`, so it will wait until the database is healthy.
* Flask is running in development mode. For production, use a WSGI server like Gunicorn.
* Data persists even if the containers are restarted because the MySQL container uses a named volume `mysql_data`.
