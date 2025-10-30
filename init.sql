CREATE DATABASE IF NOT EXISTS flightdb;

USE flightdb;

CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(50) NOT NULL,
    origin VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL
);

INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time)
VALUES
('AB123', 'DUB', 'LHR', '2025-11-01 09:00:00', '2025-11-01 10:30:00'),
('CD456', 'LHR', 'JFK', '2025-11-02 12:00:00', '2025-11-02 16:00:00');
