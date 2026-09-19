import sqlite3
from flask import g, current_app


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE_URL'])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                ilgi_alani TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
    app.teardown_appcontext(close_db)


def lead_ekle(isim, telefon, mesaj=None, ilgi_alani=None):
    db = get_db()
    cursor = db.execute(
        'INSERT INTO leads (isim, telefon, mesaj, ilgi_alani) VALUES (?, ?, ?, ?)',
        (isim, telefon, mesaj, ilgi_alani)
    )
    db.commit()
    return cursor.lastrowid


def tum_leadler():
    db = get_db()
    rows = db.execute('SELECT * FROM leads ORDER BY tarih DESC').fetchall()
    return [dict(row) for row in rows]


