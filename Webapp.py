import json
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from adminUtils import DatabaseUtils
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        with open("login.json") as read:
            data = json.load(read)
        if request.form['password'] == data['password'] and request.form['username'] == data['username']:
            return redirect(url_for('dashboard'))
        else:
            return('<h2> Wrong Password! </h2>')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))
        elif request.form['button'] == 'Hourly Report':
            return redirect(url_for('dayReport'))
        elif request.form['button'] == 'Weekly Report':
            return redirect(url_for('weekReport'))
        elif request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))


@app.route('/insert', methods=['GET', 'POST'])
def insertBook():
    create = DatabaseUtils()
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        create.insertBook(request.form['title'], request.form['author'])
        return('<h2> Book added to the database! </h2>')


@app.route('/delete', methods=['GET', 'POST'])
def deleteBook():
    create = DatabaseUtils()
    if request.method == 'GET':
        result = create.showBooks()
        return render_template('delete.html', result = result)
    elif request.method == 'POST':
        create.deleteBook(request.form['id'], request.link['insert.html'])
        return('<h2> Book deleted from the database! </h2>')

@app.route('/reportDay', methods=['GET', 'POST'])
def dayReport():
    if request.method == 'GET':
        return render_template('reportDay.html')
    elif request.method == 'POST':
        create.dayReport(request.form['day'])
        return('<h2> Day Report added to the database! </h2>')

@app.route('/reportWeek', methods=['GET', 'POST'])
def weekReport():
    if request.method == 'GET':
        return render_template('reportWeek.html')
    elif request.method == 'POST':
        create.weekReport(request.form['week'])
        return('<h2> Week Report added to the database! </h2>')

if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)
