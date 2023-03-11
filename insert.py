import sqlite3
import random
import string

from sys import argv

DATABASE = 'database.db'

db = sqlite3.connect(DATABASE)
cur = db.cursor()

username = argv[1]
password = argv[2]
token = ''.join(random.choice(string.punctuation +
                string.ascii_letters + string.digits) for x in range(23))

file = open(argv[3], 'rb')
blobData = file.read()
file.close()

cur.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (username, password, token, blobData))
db.commit()
db.close()

