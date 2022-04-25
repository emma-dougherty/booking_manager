DROP TABLE IF EXISTS waitinglist;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS members;

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR (100),
    times VARCHAR (100),
    duration VARCHAR (100),
    age_range VARCHAR (100),
    capacity INT,
    location VARCHAR (255),
    description TEXT 
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR (255),
    phone_number VARCHAR (255),
    email VARCHAR (255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE,
    course_id SERIAL REFERENCES courses(id) ON DELETE CASCADE,
    child_first_name VARCHAR (255),
    child_last_name VARCHAR (255),
    child_age INT,
    special_requirements TEXT
);

CREATE TABLE waitinglist (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE,
    course_id SERIAL REFERENCES courses(id) ON DELETE CASCADE,
    child_first_name VARCHAR (255),
    child_last_name VARCHAR (255),
    child_age INT,
    special_requirements TEXT
);
