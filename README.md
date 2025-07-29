# This project is for Academic Purposes only!
___________________________________________________________________________________________________________________________

This web application is designed for the sole purpose of modernizing transactions within small scale pharmacies in hopes
of lightening the burden of manual documentation and digitizing database storage for convenient use.

___________________________________________________________________________________________________________________________
Needed applications:
MySQL Workbench
XAMPP
VScode
python (install flask, cursor and mysql python)

Instructions on how to start application:
1. Install XAMPP and run the APACHE server on ports 8080. This can be modified in the first config file (httpd.conf), and search for "Listen 80" and "Servername localhost:80"
2. Modify "C:\xampp\phpMyAdmin\config.inc.php" and add "$cfg['Servers'][$i]['port'] = '3307';" to register the new port
3. import the databases to PHPMYADMIN in "http://localhost:8080/phpmyadmin"
4. Make sure that Python is installed, and mysql.connector and flask is installed with pip install in the terminal
5. On VScode, open the project folder and run the python script
6. done!
___________________________________________________________________________________________________________________________
notes:
The application features a universal css file and a single python file for backend for portable use.
CDN imports are avoided in the implementation to harden the local usability, eliminating the need for a network connection
___________________________________________________________________________________________________________________________
# Features:
 - Login
 This page enables users to enter their ID, username and Password for credential checking
 Once filled, the forms are sent to the backend and processed to verify if the account exists and if the entered password is right or wrong
 - Sign up
 This page enables users to register for an account.
 Data entered into the form is submitted to the backend, read with GET and uploaded into the database
 - User Dashboard
 Depending on the registered role of the user which is set by the admin, the user can modify the databases through CRUD
 The only allowed Database to be modified by the User role is the Inventory database and the Transactions database
 - Admin Dashboard
 The admin dashboard allows the user [Admin] to modify all in the User Dashboard, plus the account database.
 It's basically the same thing, but with greater hiearchy rights