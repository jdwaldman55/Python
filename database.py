import sqlite3

fileList = ['information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')

with conn:
    for file in fileList:
        if file.endswith('.txt'):
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (file,))
            conn.commit()
conn.close()



for file in fileList:
    if file.endswith('.txt'):
        print(file)
