import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL, 
    email VARCHAR(20) NOT NULL UNIQUE
);

''')
conn.commit()

# cur.execute('''
# CREATE TABLE IF NOT EXISTS posts(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title VARCHAR(20) NOT NULL,
#     body VARCHAR(140) NOT NULL,
#     user_id INTEGER  NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
#
#
#
# );
# ''')

conn.commit()

#
# cur.execute('''
# INSERT INTO users(name, email) VALUES(?, ?);
# ''', ('petya', 'petya@info.com'))

conn.commit()

# cur.execute('''
# UPDATE users SET name=? WHERE id=?;
# ''', ('masha', 2))
# conn.commit()

# cur.execute('''
# DELETE FROM users WHERE name=?;
# ''',('masha',))
#
# conn.commit()

# cur.execute('''
# SELECT * FROM users LEFT JOIN posts ON users.id = posts.user_id;
#
# ''')
# # for user in cur.fetchall():
# #    print(user)
# print(cur.fetchall())
lst=[]
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:

        lst.append(line.replace("\n","").split("~"))
print(lst)
cur.execute('''
CREATE TABLE IF NOT EXISTS posts(
    title VARCHAR(20) NOT NULL,
    body VARCHAR(140) NOT NULL, 
    is_publish INTEGER NOT NULL,
    user_id INTEGER  NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE



);
''')

conn.commit()

cur.executemany('''
INSERT INTO posts(title, body, is_publish, user_id ) VALUES(?, ?, ?, ?);
''', (lst, ))

conn.commit()