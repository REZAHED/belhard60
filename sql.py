# Написать SQL на создание/заполнение таблиц,
# а так же запросы на выборку данных из таблиц

import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL,
    email VARCHAR(24) NOT NULL UNIQUE 

);

''')

conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL UNIQUE
    

);

''')

conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(36) NOT NULL,
    description VARCHAR(36) NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE


);

''')

conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL UNIQUE


);

''')

conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE CASCADE
    


);

''')

conn.commit()

cur.execute('''
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE



);

''')

conn.commit()


# cur.execute('''
# INSERT INTO users(name, email) VALUES(?, ?);
# ''',('sasha', 'sasha@info.com'))
#
# # conn.commit()

# cur.execute('''
# INSERT INTO users(name, email) VALUES(?, ?);
# ''',('tanya', 'tanya@info.com'))

# conn.commit()

# cur.execute('''
# INSERT INTO categories(name) VALUES(?);
# ''',('shoes',))
#
# conn.commit()

# cur.execute('''
# INSERT INTO products(title, description,category_id) VALUES(?, ?, ?);
# ''',('boots','black for men',1))
#
# conn.commit()

# cur.execute('''
# INSERT INTO statuses(name) VALUES(?);
# ''',('on sale',))
#
# conn.commit()

# cur.execute('''
# INSERT INTO orders(user_id, status_id) VALUES(?, ?);
# ''',(2,1))
#
# conn.commit()

# cur.execute('''
# INSERT INTO order_items(order_id, product_id) VALUES(?, ?);
# ''',(1,1))
#
# conn.commit()


cur.execute('''
SELECT name, email, id FROM users;
''')
print(cur.fetchall())

cur.execute('''
SELECT title, id , description FROM products;
''')
print(cur.fetchall())
