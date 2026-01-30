CREATE TABLE Patients (
    id SERIAL PRIMARY KEY,
    age INT,
    insurance_type VARCHAR(50)
);

CREATE TABLE Departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Admissions (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES Patients(id),
    dept_id INT REFERENCES Departments(id),
    admission_date TIMESTAMP,
    discharge_date TIMESTAMP,
    outcome VARCHAR(50)
);
