# Custom CTF Platform

## Overview
The Custom CTF Platform is a web-based cybersecurity training platform built using Flask.  
It allows users to register, log in, solve security challenges, submit flags, and track scores through a leaderboard system.

This project demonstrates real-world backend development, authentication systems, database handling, and security challenge architecture.

---

## Features

### Authentication
- User Registration
- Secure Password Hashing
- User Login / Logout
- Session Management

### Challenge System
- View Security Challenges
- Submit Flags
- Automatic Flag Validation
- Points Award System

### Leaderboard
- Global User Ranking
- Score Based Sorting

### Challenge Management
- Create New Challenges
- Store Challenges in Database
- Dynamic Challenge Loading

---

## Tech Stack

| Layer | Technology |
|---|---|
Backend | Python, Flask |
Database | SQLite |
Authentication | Flask-Login |
ORM | Flask-SQLAlchemy |
Security | Werkzeug Password Hashing |
Frontend | HTML, CSS, Bootstrap (if used) |

---

## Project Structure

```
Custom_CTF_Platform/
│
├ app.py
├ config.py
├ models.py
├ database.db
│
├ templates/
│ ├ index.html
│ ├ login.html
│ ├ register.html
│ ├ dashboard.html
│ ├ challenge.html
│ ├ create.html
│ └ leaderboard.html
│
├ screenshots/
├ requirements.txt
└ README.md
```
---

## Screenshots

Screenshots of the platform UI are available in the `screenshots` folder:

- Home Page
- Login Page
- Register Page
- Dashboard
- Challenge Page
- Create Challenge Page
- Leaderboard Page

---

## Installation & Setup

### Clone Repository
git clone <your-repo-link>
cd ctf-platform


---

### Create Virtual Environment
python -m venv venv


Activate:

Windows:
venv\Scripts\activate


Mac/Linux:
source venv/bin/activate


---

### Install Dependencies
pip install -r requirements.txt


---

### Run Application
python app.py


---

### Open Browser
http://127.0.0.1:5000


---

## 🧪 Sample Challenges Included

### Crypto Challenge
Decode Base64 string to obtain flag.

### Web Challenge
Analyze webpage source to locate hidden flag.

---

## Learning Outcomes

- Flask Web Application Development
- Secure Authentication Implementation
- Database Design & ORM Usage
- Cybersecurity Challenge Design
- Secure Coding Practices
- Session Handling
- Security Tool Architecture

---

## Limitations

- Uses Flask Development Server (Not Production Ready)
- SQLite Database (Not Scalable for Large Users)
- Basic Role System (Admin controls can be extended)

---

## Future Improvements

- Admin Panel
- Challenge Categories
- File Upload Challenges
- Docker Deployment
- Cloud Hosting
- Competition Timer Mode
- Team Based Challenges
- API Integration

---

## Disclaimer

This project is developed for educational and cybersecurity training purposes only.

---

## Author

Anirudha G Kulkarni \
Cybersecurity | Application Security | Backend Development

---