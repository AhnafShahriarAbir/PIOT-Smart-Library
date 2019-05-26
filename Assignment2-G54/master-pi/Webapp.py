"""
    This part is developing the console-menu for the Master pi after successfully log in and redirect.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

import json
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from adminUtils import DatabaseUtils
import os

app = Flask(__name__)


# Endpoint to log in as admin.
@app.route('/', methods=['GET', 'POST'])
def login():
    """Endpoint to log in as admin, verify the username and password in the local JSON file 
    error message will prompt if username or password are failed to identify 
    """
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        with open("login.json") as read:
            data = json.load(read)
        if request.form['password'] == data['password'] and request.form['username'] == data['username']:
            return redirect(url_for('dashboard'))
        else:
            return('<h2> Wrong Password! </h2>')

# Endpoint to show dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """A dash borad in Web Heml is presented for admin, option and form are created from the HTML element 
    button.  

    Different button will direct admin to the different page to execute the next command.
    """
    if request.method == 'GET':
        return render_template('dashboard.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))
        elif request.form['button'] == 'Day Report':
            return redirect(url_for('dayReport'))
        elif request.form['button'] == 'Week Report':
            return redirect(url_for('weekReport'))
        elif request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))

# Endpoint to insert book
@app.route('/insert', methods=['GET', 'POST'])
def insertBook():
    """direct admin to the insert page and calling the DatabaseUtils function to ADD value to table
    """
    create = DatabaseUtils()
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        if request.form['button'] == 'insert':
            if len(request.form['title']) != 0 and len(request.form['author']) != 0:
                create.insertBook(
                    request.form['title'], request.form['author'])
                return redirect(url_for('insertBook'))
            else:
                return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Dashboard':
            #: redirect to the dashboard
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))


# Endpoint to delete book
@app.route('/delete', methods=['GET', 'POST'])
def deleteBook():
    """direct admin to the insert page and calling the DatabaseUtils function to DELETE value from table
    """
    create = DatabaseUtils()
    if request.method == 'GET':
        result = create.showBooks()
        return render_template('delete.html', result=result)
    elif request.method == 'POST':
        if request.form['button'] == 'delete':
            if len(request.form['id']) != 0:
                create.deleteBook(request.form['id'])
                return redirect(url_for('deleteBook'))
            else:
                return redirect(url_for('deleteBook'))
        elif request.form['button'] == 'Dashboard':
            #: redirect to the dashboard
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))


# Endpoint to show data visualization daily
@app.route('/reportDay', methods=['GET', 'POST'])
def dayReport():
    """calling google graph studio API to generate graph form the table data with selected dates
    """
    if request.method == 'GET':
        return render_template('reportDay.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Dashboard':
            #: redirect to the dashboard
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))

# Endpoint to show data visualization weekly
@app.route('/reportWeek', methods=['GET', 'POST'])
def weekReport():
    """calling google graph studio API to generate graph form the table data with selected period
    """
    if request.method == 'GET':
        return render_template('reportWeek.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))


# execute the main function
if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=2000, debug=False)
