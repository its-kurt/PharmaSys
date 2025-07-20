USE pharmacy;

TRUNCATE TABLE pharmacy.drugs;
TRUNCATE TABLE pharmacy.users;

LOAD DATA INFILE 'C:\Users\Gumgum\Desktop\SoftD\ProjectFiles\[SQL]Sheets/DrugDatabase.csv'
INTO TABLE pharmacy.drugs
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:\Users\Gumgum\Desktop\SoftD\ProjectFiles\[SQL]Sheets/LoginData.csv'
INTO TABLE pharmacy.users
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;