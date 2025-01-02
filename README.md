# Expert Skills Matching Program

## Overview
A Python-based program that ranks experts based on how well their skills match a given candidate description by comparing it with stored skills in a MySQL database.

## Setup Instructions

### 1. Backend Database (XAMPP)

- Install XAMPP and start MySQL.
- Create a database and table using the following SQL:

```sql
CREATE DATABASE test001;
USE test001;

CREATE TABLE experts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    skills TEXT,
    experience INT,
    location VARCHAR(255)
);
```

### 2. Insert random data
- Run write_sql.py for insert random data into database.
```
python write_sql.py
```
### 3. Run the Program
-Run the cal.py file:
```
python cal.py
```
Enter a candidate description when prompted: We are looking for someone with strong Python skills, experience in Machine Learning, and knowledge in NLP.
The program will output a ranked list of experts based on skill similarity.

## Reminder
If you have your own database, you just need to change your database information in the function that connects to the database.
```
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",        
        user="root",    
        password="",  # Your MySQL password
        database="test001",  # Your database name
        port="3307"   # MySQL port if different
    )
```
