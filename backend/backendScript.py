# I screwed up with the last backend file so I'm remaking it all over again
#The line below allows the script to skim through the operating system directory. of course, we can change that to just detect the web files and the sql, but for prototype reasons, yeah
import os
#csv for prototype for now
import csv
#This is what we will use for the whole code. flask, exclusively. 
from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)