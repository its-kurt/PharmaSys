# I screwed up with the last backend file so I'm remaking it all over again
#The line below allows the script to skim through the operating system directory. of course, we can change that to just detect the web files and the sql, but for prototype reasons, yeah
import os
#csv for prototype for now
import csv
#This is what we will use for the whole code. flask, exclusively. 
from flask import Flask, render_template, request, redirect, url_for, flash
#MySQL connector for backend integration
import mysql.connector

#This line is needed to initialize flask
app = Flask(__name__)
app.secret_key = 'a_very_secret_key_for_session_management' # Required for flash messages

# MySQL database config block
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'pharmacy'
}


##LOG IN SECTION-----------------------------------------------------------------------------------------------
##the back slash is an appending prefix with the GET method implying a request from the html
##note: GET is used to jump from HTML to HTML if action is detected
@app.route('/', methods=['GET'])
##no idea why its called index but hey
def index():
    #Renders the initial form page, which in this case, is Login.html
    return render_template('Login.html')

##depending on what the action states, this is returned and simulated.
##note: POST is used to simulate actions depending on what is requested on the HTML. e.g. if a button on the form says submit form, then grab that form and init
@app.route('/login', methods=['POST'])
def submit_form():
    #Handles form submission and performs validation.
    if request.method == 'POST':
        employeeId = request.form.get('employeeId')
        username = request.form.get('username')
        password = request.form.get('password')

        errors = []

        # Server-side validation logic
        if not employeeId:
            errors.append("employeeId is required.")
        elif len(employeeId) > 8:
            errors.append("Invalid employeeId.")
        
        if not username:
            errors.append("Username is required.")
        elif len(username) < 3:
            errors.append("Username must be at least 3 characters long.")

        if not password:
            errors.append("Password is required.")
        elif len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if errors:
            # If validation fails, re-render the form with error messages
            for error in errors:
                flash(error, 'error') # 'error' is a category for styling
            return render_template('Login.html',
                                   username=username,
                                   employeeId=employeeId) # Pass back submitted data to pre-fill form
        else:
            # If validation succeeds, process the data (e.g., validate against DB)
            try:
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()
                ##PATCH THIS ERROR! IT'S SUPPOSED TO BE GET AND COMPARE, NOT INSERT
                print("Trying to insert user into database...")
                cursor.execute(
                    "INSERT INTO users (ID, Username, Password, status) "
                    "VALUES (%s, %s, %s)",
                    (employeeId, username, password)
                )
                connection.commit()
                print("User logged in successfully.")

                user = cursor.fetchone()
                if user:
                    flash('Login successful!', 'LoginSucess')
                    return redirect(url_for('LoginSuccess_page'))
                else:
                    flash('Invalid credentials.', 'error')
                    return render_template('Login.html')
            except mysql.connector.Error as err:
                flash(f'Database error: {err}', 'error')
                return render_template('Login.html')
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
    return redirect(url_for('index')) # Redirect if accessed via GET

@app.route('/LoginSucess')
def LoginSuccess_page():
    #Renders a success page after successful Login form submission.
    return render_template('LoginSuccess.html')

@app.route('/success')
def success_page():
    #Renders a success page after successful Signup form submission.
    return render_template('success.html')


@app.route('/signup', methods=['GET'])
def signup_page():
    #Renders the signup form page, which in this case, is SignUp.html
    return render_template('SignUp.html')

# This is where the signup will check
@app.route('/signup', methods=['POST'])
def submit_signup():
    if request.method == 'POST':
        # These are variables to be retrieved from the signup page
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        employeeId = request.form.get('employeeId')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        errors = []

        # We want to check if any values are empty
        if not firstName:
            errors.append("First name is required.")
        if not lastName:
            errors.append("Last name is required.")
        if not employeeId:
            errors.append("Employee ID is required.")
        elif len(employeeId) > 8:
            errors.append("Invalid Employee ID.")
        if not username:
            errors.append("Username is required.")
        elif len(username) < 3:
            errors.append("Username must be at least 3 characters long.")
        if not password:
            errors.append("Password is required.")
        elif len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not confirmPassword:
            errors.append("Please confirm your password.")
        elif password != confirmPassword:
            errors.append("Passwords do not match.")

        # Check if any errors exist and flash them
        if errors:
            for error in errors:
                flash(error, 'error')
            print("Validation errors (signup):", errors)
            return render_template('SignUp.html',
                                   firstName=firstName,
                                   lastName=lastName,
                                   username=username,
                                   employeeId=employeeId)
        else:
            connection = None
            cursor = None
            try:
                print("Inserting new user:", employeeId, username)
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()
                # Insert the account into the users database
                cursor.execute(
                    "INSERT INTO users (ID, role, Username, Password, status, FirstName, LastName) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (employeeId, 'user', username, password, 'active', firstName, lastName)
                )
                connection.commit()
                flash('Account created successfully!', 'success')
                print("Signup successful. Redirecting to success page.")
                return redirect(url_for('success_page'))
            except mysql.connector.Error as err:
                flash(f'Database error: {err}', 'error')
                print("MySQL error (signup):", err)
                return render_template('SignUp.html')
            finally:
                if connection and connection.is_connected():
                    cursor.close()
                    connection.close()
    return redirect(url_for('signup_page'))



##This is what starts flask. 
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloads and detailed error messages
