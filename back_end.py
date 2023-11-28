import sqlite3

def connecting():
    con = sqlite3.connect("FORM.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS FORM(ID integer PRIMARY KEY, Name text , phone integer , gender text, payment_mode text)")
    con.commit()
    con.close()

def inserting(name,phone,gender,payment):
    con = sqlite3.connect("FORM.db")
    cur = con.cursor()
    cur.execute(" INSERT INTO FORM VALUES(name,?,?,?)",(name,phone,gender,payment))
    con.commit()
    con.close()

def printing():
    con = sqlite3.connect("FORM.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM FORM")
    content = cur.fetchall()
    con.close()
    return content


def deleting(id):
    con = sqlite3.connect("FORM.db")
    cur = con.cursor()
    cur.execute("DELETE FROM FORM WHERE ID=? " ,(id,))
    con.commit()
    con.close()
# connecting()
# inserting("cormen","DAA ",2022 ,9876)
# # print(searching(year=2021))
# # deleting(3)
print(printing())
