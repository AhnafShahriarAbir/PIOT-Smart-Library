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
        elif request.form['button'] == 'Day Report':
            return redirect(url_for('dayReport'))
        elif request.form['button'] == 'Week Report':
            return redirect(url_for('weekReport'))
        elif request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))


@app.route('/insert', methods=['GET', 'POST'])
def insertBook():
    create = DatabaseUtils()
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        if request.form['button'] == 'insert':
            if len(request.form['title']) != 0 and len(request.form['author']) != 0:
                create.insertBook(request.form['title'], request.form['author'])
                return redirect(url_for('insertBook'))
            else:
                return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))

        


@app.route('/delete', methods=['GET', 'POST'])
def deleteBook():
    create = DatabaseUtils()
    if request.method == 'GET':
        result = create.showBooks()
        return render_template('delete.html', result = result)
    elif request.method == 'POST':
        if request.form['button'] == 'delete':
            if len(request.form['id']) != 0:
                create.deleteBook(request.form['id'])
                return redirect(url_for('deleteBook'))
            else:
                return redirect(url_for('deleteBook'))
        elif request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))
        
        

@app.route('/reportDay', methods=['GET', 'POST'])
def dayReport():
    if request.method == 'GET':
        return render_template('reportDay.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))

@app.route('/reportWeek', methods=['GET', 'POST'])
def weekReport():
    if request.method == 'GET':
        return render_template('reportWeek.html')
    elif request.method == 'POST':
        if request.form['button'] == 'Dashboard':
            return redirect(url_for('dashboard'))
        elif request.form['button'] == 'Insert a New Book':
            return redirect(url_for('insertBook'))
        elif request.form['button'] == 'Delete a Book':
            return redirect(url_for('deleteBook'))

if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)
