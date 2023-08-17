import sqlite3

connect = sqlite3.connect('name1.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       col_1 INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       col_1 TEXT)''')

list_1 = ["white", 5, "yellow", 10, "green", 7, "pink", 3, "blue", 9]


for i in list_1:
    if isinstance(i, str):
        cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))

        cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', (len(i),))

    elif isinstance(i, int):
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (i,))

        else:
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', ("нечетное",))


    cursor.execute('''SELECT COUNT(*) FROM tab_1 ''')
    text_count = cursor.fetchone()[0]

    if text_count > 5:
        cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')

    connect.commit()


cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')

connect.close()
