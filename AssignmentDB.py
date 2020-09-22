import sqlite3
import os

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_folder( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )")
    conn.commit()
conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    for temp in fileList:
        if temp.endswith('.txt'):
            cur.execute('insert INTO tbl_folder(col_files) Values (?)', \
                        (temp,))
    conn.commit()
conn.close()

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM tbl_folder')
    results = cur.fetchall()
    print(results)
conn.close()
