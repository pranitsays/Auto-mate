import sqlite3

con=sqlite3.connect('automate.db')
cursor=con.cursor()
# rows=cursor.execute('UPDATE users SET email_id = "shreyashtalwekar649@gmail.com" WHERE username="shreyash"')
# rows=cursor.execute('SELECT sql FROM sqlite_master WHERE name="users"')
# cursor.execute(
#     'CREATE TABLE current_user('
#     'username TEXT PRIMARY KEY,'
#     'password TEXT NOT NULL DEFAULT "",'
#     'theme BOOLEAN DEFAULT 0,'
#     'voice BOOLEAN DEFAULT 0,'
#     'music TEXT DEFAULT "G:/Music",'
#     'video TEXT DEFAULT "G:/VDOS/Music",'
#     'movie TEXT DEFAULT "G:/Movies", '
#     'email_id TEXT DEFAULT "abc@gmail.com",'
#     'location TEXT DEFAULT "Pune"'
#     ')'
# )
# cursor.execute(
#     'INSERT INTO current_user VALUES('
#     '"abhinav",'
#     '"abhi1829",'
#     '0,'
#     '0,'
#     '"G:/Music",'
#     '"G:/VDOS/Music",'
#     '"G:/Movies",'
#     '"abhinow63@gmail.com",'
#     '"Nagpur"'
#     ')'
# )
# cursor.execute(
#     'INSERT INTO users VALUES('
#     '"shreyash",'
#     '"shreyash",'
#     '0,'
#     '0,'
#     '"G:/Music",'
#     '"G:/VDOS/Music",'
#     '"G:/Movies",'
#     '"shreyashtalwekar649@gmail.com",'
#     '"Wardha"'
#     ')'
# )
# cursor.execute('DROP TABLE current_user')
# for row in rows:
#     print(row)
con.commit()
con.close()