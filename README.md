This project is for Academic Purposes only!
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
4. On VScode, open the project folder and run the python script
5. done!
___________________________________________________________________________________________________________________________
notes:
The application features a universal css file and a single python file for backend for portable use.
CDN imports are avoided in the implementation to harden the local usability, eliminating the need for a network connection
