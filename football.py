import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db_name = 'events_football.db'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/events')
def events():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM event")
    rows = cur.fetchall()
    conn.close()
    return render_template('events.html', rows=rows)

@app.route('/event_details/<id>')
def event_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM event WHERE id_event=?", (id,))
    event = cur.fetchone()
    conn.close()
    return render_template('events_details.html', event=event)

@app.route('/games')
def ginfs():
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM ginf")
    rows = cur.fetchall()
    conn.close()
    return render_template('ginf.html', rows=rows)

@app.route('/game_details/<id>')
def ginf_details(id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM ginf WHERE id_odsp=?", (id,))
    game = cur.fetchone()
    conn.close()
    return render_template('ginf_detail.html', ginf=ginf)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(sqlite3.Error)
def handle_database_error(error):
    return render_template('error.html', message='Database error: {}'.format(str(error))), 500


