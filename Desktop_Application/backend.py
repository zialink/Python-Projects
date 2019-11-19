import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        row=self.cur.fetchall()
        return row

    def update(self, ID, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE ID=?", (title,author,year,isbn,ID))
        self.conn.commit()

    def search(self,title='', author='', year='', isbn=''):
        self.cur.execute("SELECT * FROM book WHERE(title=? OR author=? OR year=? OR isbn=?)",(title, author, year, isbn))
        row=self.cur.fetchall()
        return row

    def delete(self, ID):
        self.cur.execute("DELETE FROM book WHERE ID =?", (ID,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    #insert("Honest Mistake", "Angel Davies", 1950, 168393896412244321)
    #print(search(year='2000'))
    #update(7,"Fired!","Bill Zia", 1988, 21983896412244321)
    #print(view())
