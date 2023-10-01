
# Hospital Management System

An open-source hospital management system designed to assist small hospitals around the world.

## Features

- Patient registration and management
- Doctor and appointment scheduling
- Lab test and prescription management
- User authentication and registration

## Setup and Running

### 1. Setup a Virtual Environment

It's recommended to use a virtual environment. This avoids potential package conflicts.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
```

### 2. Install Required Libraries

Navigate to the project directory and install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

If you want to use a different database than the SQLite default, set the DATABASE_URI environment variable:

```bash
export DATABASE_URI="mysql+pymysql://<username>:<password>@<host>:<port>/<database>"
```

### 4. Initialize the Database

Before running the app for the first time, initialize the database:

```python
from utils.database import Base, engine
Base.metadata.create_all(bind=engine)
```

### 5. Run the App

Navigate to the project directory and run:

```bash
python app.py
```

### 6. Access the App

Once the app is running, access it in your web browser at `http://localhost:5000/`.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or raise issues. (just pull request to the 'develop') branch is allowed!

## License

This project is open-source and available under the [MIT License](LICENSE).
