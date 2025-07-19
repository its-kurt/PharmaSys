# I screwed up with the last backend file so I'm remaking it all over again
#The line below allows the script to skim through the operating system directory. of course, we can change that to just detect the web files and the sql, but for prototype reasons, yeah
import os
#csv for prototype for now
import csv
#This is what we will use for the whole code. flask, exclusively. 
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'a_very_secret_key_for_session_management' # Required for flash messages


##login back end script-----------------------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def index():
    #Renders the initial form page.
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/submit', methods=['POST'])
def submit_form():
    #Handles form submission and performs validation.
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        errors = []

        # Server-side validation logic
        if not username:
            errors.append("Username is required.")
        elif len(username) < 3:
            errors.append("Username must be at least 3 characters long.")

        if not email:
            errors.append("Email is required.")
        elif "@" not in email or "." not in email:
            errors.append("Invalid email format.")

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
                                   email=email) # Pass back submitted data to pre-fill form
        else:
            # If validation succeeds, process the data (e.g., save to a database)
            # For this example, we'll just redirect to a success page
            flash('Form submitted successfully!', 'success')
            return redirect(url_for('success.html'))
    return redirect(url_for('index')) # Redirect if accessed via GET

@app.route('/success')
def success_page():
    """Renders a success page after successful form submission."""
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for automatic reloads and detailed error messages