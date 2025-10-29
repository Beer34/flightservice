CREATE TABLE IF NOT EXISTS flights (
  id INT AUTO_INCREMENT PRIMARY KEY,
  flight_number VARCHAR(50),
  origin VARCHAR(100),
  destination VARCHAR(100)
);

INSERT INTO flights (flight_number, origin, destination)
VALUES ('AI101', 'Delhi', 'London'),
       ('BA202', 'London', 'New York');
