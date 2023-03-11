from flask import Flask, g, jsonify, request
import sqlite3
from face_recognition import face_encodings, compare_faces, load_image_file

DATABASE = 'database.db'

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/login', methods=['POST'])
def login():
    print(request.body)
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                (request.form['username'], request.form['password']))
    user = cur.fetchone()
    if user is None:
        return jsonify({"error": "Invalid username or password"}), 401
    else:
        return jsonify({"success": "Logged in successfully", "token": user[2]}), 200


@app.route('/verify', methods=['POST'])
def verify():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE token = '|n/>JOGt]5,:P4Bd?RO2Ep%'") # , (request.form['token']))
    user = cur.fetchone()
    print(user[0])
    if user is None:
        return jsonify({"error": "Invalid token"}), 401

    print(request.files['file'])
    img = user[3]
    user_img = request.files['file'].read()
    open(f'user_img_{user[0]}.jpg', 'wb').write(user_img)
    open(f'img_{user[0]}.jpg', 'wb').write(img)
    
    user_img_encoding = face_encodings(load_image_file(f'user_img_{user[0]}.jpg'))[0]
    img_encoding = face_encodings(load_image_file(f'img_{user[0]}.jpg'))[0]

    print('wtf')
    if compare_faces([img_encoding], user_img_encoding)[0]:
        return jsonify({"success": "Verified successfully"}), 200
    else:
        return jsonify({"error": "Verification failed"}), 401


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
