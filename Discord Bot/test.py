import sqlite3
db = sqlite3.connect('main.sqlite')
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS main(
row TEXT, 
guild_id TEXT, 
msg TEXT, 
channel_id TEXT)
''')
cursor.close()
db.close()
