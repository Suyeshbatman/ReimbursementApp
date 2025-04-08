# ReimbursementApp
Application to submit reimbursement payments.

There are two branches
main &
Main

main--
This branch contains the application developed using Flask, simple HTML, CSS, Javascript and SQLite

Main--
This branch contains the application developed using .Net, Angular, SQLite

Navigate to the correct branch to clone the repository.

FlaskApp
Backend:
Flask
SQLAlchemy, Werkzeug, CORS

Frontend:
HTML, CSS, Javascript

Database:
SQLite

Cloning the repository:
git clone https://github.com/Suyeshbatman/ReimbursementApp.git

Running the application:
python -m venv venv 
.\venv\Scripts\activate 
Installing requirements
pip install Flask
pip install flask-sqlalchemy
pip install flask-cors

python app.py
AFter running the application navigate to the browser where the application is serving and copy paste : http://127.0.0.1:5000
Running on http://127.0.0.1:5000

You will be able to see the Employee Reimbursement Form and can interact with the form.

After submitting the form, the receipt will be saved under Uploads folder.


