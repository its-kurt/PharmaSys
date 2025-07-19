import os
import csv
from flask import Flask, request, redirect, send_from_directory

# ─── Path configuration ───────────────────────────────────
BackendDir  = os.path.dirname(__file__)
ProjectRoot = os.path.abspath(os.path.join(BackendDir, os.pardir))
CsvFolder   = os.path.join(ProjectRoot, '[SQL]Sheets')
LoginCsv    = os.path.join(CsvFolder, 'LoginData.csv')
HtmlFolder  = ProjectRoot

# ─── Flask app setup ──────────────────────────────────────
Application = Flask(
    __name__,
    static_folder=os.path.join(ProjectRoot, 'assets'),
    static_url_path='/assets'
)

# ─── Login route ──────────────────────────────────────────
@Application.route('/login', methods=['GET', 'POST'])
def LoginHandler():
    if request.method == 'POST':
        EmployeeId = request.form.get('employeeId', '')
        UserName   = request.form.get('username', '')
        Password   = request.form.get('password', '')

        # authenticate against CSV
        with open(LoginCsv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            authenticated = False
            for row in reader:
                if (row.get('EmployeeId') == EmployeeId
                        and row.get('Username') == UserName
                        and row.get('Password') == Password
                        and row.get('status') == 'Active'):
                    authenticated = True
                    break
        if authenticated:
            # Successful login → redirect to dashboard
            return redirect('/admin')
        else:
            # Invalid credentials → reload login page
            return redirect('/login')

    # GET → serve the login page
    return send_from_directory(HtmlFolder, 'Web_LogIn.html')

# ─── Sign-up route ─────────────────────────────────────────
@Application.route('/Web_SignUp.html', methods=['GET', 'POST'])
def SignupHandler():
    if request.method == 'POST':
        FullName       = request.form.get('fullName', '')
        EmployeeId     = request.form.get('EmployeeId', '')
        UserName       = request.form.get('username', '')
        Password       = request.form.get('password', '')
        ConfirmPassword= request.form.get('confirmPassword', '')

        # check passwords match
        if Password != ConfirmPassword:
            return redirect('/Web_SignUp.html')

        # append new user to CSV
        with open(LoginCsv, 'a', newline='') as csvfile:
            CsvWriter = csv.writer(csvfile)
            CsvWriter.writerow([
                EmployeeId,    # EmployeeId variable
                'User',
                UserName,
                Password,
                'Active',
                FullName,
                ''
            ])

        # redirect to login after successful sign-up
        return redirect('/Web_LogIn.html')

    # GET → serve the sign-up page
    return send_from_directory(HtmlFolder, 'Web_SignUp.html')

# ─── Dashboard route ───────────────────────────────────────
@Application.route('/admin')
def AdminDashboardHandler():
    return send_from_directory(HtmlFolder, 'Web-AdminDashboard.html')

if __name__ == '__main__':
    Application.run(debug=True)