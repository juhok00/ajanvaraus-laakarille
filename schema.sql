DROP TABLE IF EXISTS cities CASCADE;
DROP TABLE IF EXISTS specialization CASCADE;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS doctor_specialization CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS appointment CASCADE;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name TEXT);

CREATE TABLE specialization (
    id SERIAL PRIMARY KEY,
    specialization_name TEXT);

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    doctor_name TEXT,
    city_id INTEGER REFERENCES cities(id));

CREATE TABLE doctor_specialization (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER REFERENCES doctors(id),
    specialization_id INTEGER REFERENCES specialization(id));

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT);

CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER,
    appointment_date DATE,
    appointment_time TIME WITHOUT TIME ZONE);


INSERT INTO cities (city_name) VALUES
    ('Helsinki'),
    ('Tampere'),
    ('Oulu'),
    ('Somero');


INSERT INTO specialization (specialization_name) VALUES
    ('Yleislääkäri'),
    ('Ortopedi'),
    ('Ihotautilääkäri'),
    ('Mielen hyvinvointi'),
    ('Näytteenotto'),
    ('Rokotteet');

INSERT INTO doctors (doctor_name, city_id) VALUES
    ('Maija Virtanen', 1),
    ('Antti Koskinen', 1),
    ('Sari Lehtonen', 1),
    ('Juha Nieminen', 1),
    ('Tiina Järvinen', 1),
    ('Matti Rantanen', 1),
    ('Johanna Mäkinen', 2),
    ('Pekka Saarinen', 2),
    ('Anna Laine', 2),
    ('Mikko Hämäläinen', 2),
    ('Katriina Koivisto', 2),
    ('Tuomas Heikkinen', 3),
    ('Laura Rautio', 3),
    ('Markus Laaksonen', 3),
    ('Henna Peltola', 3),
    ('Jari Karjalainen', 4);

INSERT INTO doctor_specialization (doctor_id, specialization_id) VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (4, 1),
    (5, 4),
    (6, 4),
    (7, 1),
    (8, 1),
    (9, 1),
    (7, 2),
    (10, 3),
    (11, 4),
    (12, 1),
    (13, 1),
    (14, 2),
    (15, 4),
    (16, 1);
