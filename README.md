Reimbursement App

It is a full-stack project consisting of Angular frontend and a .Net Core backend. The application allows employees to submit receipts for reimbursement, with file upload functionality and a simple form submission.

Before running the project, have these requirements installed:
Node.js 
Angular CLI
.NET SDK
SQLite

Cloning the repository:
git clone https://github.com/Suyeshbatman/ReimbursementApp.git

After cloning navigate to ReimbursementApp
cd ReimbursementApp

Running the Backend
cd ReimbursementAPI
dotnet restore
dotnet run

The Backend API should be running on http://localhost:5100

Running the Frontend
cd ClientApp
npm Install
ng serve

The Angular app should now be running on http://localhost:4200

Once it is running you should see the "Employee Reimbursement Form" and can now interact with the form and submit the form.

Once submitted, the receipt file will be generated under Uploads folder. 
