from flask import Flask, render_template, request, redirect, session, url_for, make_response
from gevent import pywsgi
import sqlite3
import hashlib
import base64
import os

app = Flask(__name__)
key = os.urandom(16)


conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS users')
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, admin BIT DEFAULT 0)''')
adminPw = hashlib.sha256(os.urandom(16).hex().encode()).hexdigest()
c.execute("INSERT INTO users (username, password, admin) VALUES ('admin', '" + adminPw +"', 1)")
conn.commit()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            return '<script>alert("Username and password cannot be empty!");window.location.href = "/register";</script>'
        if len(username) > 20 or len(password) > 20:
            return '<script>alert("Username and password cannot be longer than 20 characters!");window.location.href = "/register";</script>'
        if len(username) < 6 or len(password) < 6:
            return '<script>alert("Username and password cannot be shorter than 6 characters!");window.location.href = "/register";</script>'
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = c.fetchone()
        if existing_user:
            return '<script>alert("Username already exists!");window.location.href = "/register";</script>'

        c.execute("INSERT INTO users (username, password, admin) VALUES (?, ?, 0)", (username, hashed_password))
        conn.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = c.fetchone()
        if user:
            admin = user[3]
            if admin == 1:
                admin = "True"
            else:
                admin = "False"
            response = make_response(redirect(url_for('profile')))
            content = 'username=' + username + '&admin=' + admin
            response.set_cookie('identity', encrypt(content))
            return response
        else:
            return '<script>alert("Invalid username or password!");window.location.href = "/login";</script>'

    return render_template('login.html')


@app.route('/profile')
def profile():
    if request.cookies.get('identity'):
        try:
            cookie = decrypt(request.cookies.get('identity'))
            username = cookie.split('&')[0].split('=')[1]
            admin = cookie.split('&')[1].split('=')[1]
            if admin == 'True':
                flag = open('flag.txt', 'r').read()
                return 'Welcome, ' + username + '! Here is your flag: ' + flag + ' <br/>(This is a secret for admin only)'
            else:
                return 'Welcome, ' + username + '! <br/> <a href="/logout">Logout</a>'
        except:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('identity', '', expires=0)
    return response

def encrypt(content):
    buf = content.encode()
    i = 0
    output = []
    for b in buf:
        output.append( b ^ key[i % len(key)] )
        i = i + 1
    output = base64.b64encode(bytes(output)).decode()
    return output

def decrypt(cipher):
    buf = bytes.fromhex(base64.b64decode(cipher).hex())
    i = 0
    output = []
    for b in buf:
        output.append( b ^ key[i % len(key)] )
        i = i + 1
    output = bytes(output).decode()
    return output

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
