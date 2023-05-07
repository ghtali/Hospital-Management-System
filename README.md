# Hospital Management System

## Python demo web application with Flask and MySQL using SOLID principles

- This is a demo web application that uses Python, Flask, MySQL and Bootstrap. It is a simple hospital management system that allows you to add, edit and delete patients and doctors.

# Table of Contents

- [Diagrams](#diagrams)
  - [Database Schema](#db-schema)
- [Application Structure](#application-structure)
  - [Structure](#structure)
  - [SOLID Principles](#solid-principles)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Setup](#setup)
- [Usage](#usage)
  - [Run](#run)
  - [Test](#test)
- [License](#license)

# Diagrams

## Database Schema

![Database Schema](https://raw.githubusercontent.com/ghtali/hospital-management-system/master/docs/images/db-schema.jpg)

[Link to the Database Schema on DrawSQL](https://drawsql.app/teams/team-a-27/diagrams/hospital/embed)

- The Patients table has a one-to-many relationship with the Appointments table. This means that one patient can have multiple appointments, but each appointment is associated with only one patient. The relationship is established by the PatientID column in the Appointments table, which serves as a foreign key that references the PatientID column in the Patients table.

- The Doctors table also has a one-to-many relationship with the Appointments table. This means that one doctor can have multiple appointments, but each appointment is associated with only one doctor. The relationship is established by the DoctorID column in the Appointments table, which serves as a foreign key that references the DoctorID column in the Doctors table.

- The Appointments table has a one-to-one relationship with the Prescriptions table. This means that each appointment can have only one prescription, and each prescription is associated with only one appointment. The relationship is established by the AppointmentID column in the Prescriptions table, which serves as a foreign key that references the AppointmentID column in the Appointments table.

- The Appointments table also has a one-to-many relationship with the Lab Tests table. This means that one appointment can have multiple lab tests, but each lab test is associated with only one appointment. The relationship is established by the AppointmentID column in the Lab Tests table, which serves as a foreign key that references the AppointmentID column in the Appointments table.

# Application Structure

## Structure

```
app/
├── api/
│   ├── __init__.py
│   ├── appointments.py
│   ├── doctors.py
│   ├── lab_tests.py
│   ├── patients.py
│   └── prescriptions.py
├── db/
│   ├── __init__.py
│   ├── models.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── appointments_repository.py
│   │   ├── doctors_repository.py
│   │   ├── lab_tests_repository.py
│   │   ├── patients_repository.py
│   │   └── prescriptions_repository.py
│   ├── database.py
│   └── interfaces/
│       ├── __init__.py
│       ├── appointment_repository_interface.py
│       ├── doctor_repository_interface.py
│       ├── lab_test_repository_interface.py
│       ├── patient_repository_interface.py
│       └── prescription_repository_interface.py
├── services/
│   ├── __init__.py
│   ├── appointments_service.py
│   ├── doctors_service.py
│   ├── lab_tests_service.py
│   ├── patients_service.py
│   └── prescriptions_service.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── appointments.py
│   ├── doctors.py
│   ├── lab_tests.py
│   ├── patients.py
│   └── prescriptions.py
├── static/
│   ├── script.js
│   ├── style.css
├── templates/
│   ├── base.html
│   ├── appointments.html
│   ├── home.html
│   ├── patients.html
│   ├── lab_tests.html
│   ├── login.html
│   └── doctors.html
├── utils/
│   ├── __init__.py
│   ├── auth.py
│   └── validators.py
└── app.py

```

## This application follows the SOLID principles:

- Single Responsibility Principle (SRP): Each class should have only one responsibility.

  We separate classes for handling patients, doctors, appointments, prescriptions, and lab tests. Each class should handle only one type of entity and the operations related to it.

- Open/Closed Principle (OCP): Classes should be open for extension but closed for modification.

  We create an interface for each class and define the required methods. Then, we could create concrete implementations of the interface for each class. This way, we can easily add new functionality without modifying existing code.

- Liskov Substitution Principle (LSP): Subclasses should be substitutable for their parent classes.

  Each concrete implementation should adhere to the interface defined by the parent class. This allows us to easily swap out one implementation for another without breaking the code.

- Interface Segregation Principle (ISP): Clients should not be forced to depend on methods they do not use.

  Each interface should define only the methods required by the client. This reduces the coupling between the client and the implementation and makes the code more maintainable.

- Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions.

  We create a repository layer that handles the communication with the database. The classes in the application layer should depend on the repository layer abstraction rather than the implementation.

# Installation

## Requirements

- Python 3.6 or higher
- MySQL 5.7 or higher

## Setup

- Clone the repository

```
git clone
```

- Create a virtual environment

```
python3 -m venv venv
```

- Activate the virtual environment

```
.\.venv\Scripts\activate
```

- Install the dependencies

```
pip install -r requirements.txt
```

- Create a database

```
mysql -u root -p
```

```
CREATE DATABASE hospital;
```

- Create a .env file and add the following environment variables

- Run the migrations

```
flask db upgrade
```

# Usage

## Run

```
flask run
```

## Test

```
pytest
```

# License

MIT

MIT License

Copyright (c) [2023] [github.com/ghtali]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
