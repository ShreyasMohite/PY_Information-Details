import sqlite3

def Personal_Information():
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("create table if not exists personal_info(id integer primary key,fullname text,address text,email text,dob text,gender text,contact text)")
    conn.commit()
    conn.close()
def add_personal_information(fullname,address,email,dob,gender,contact):
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("insert into personal_info values(null,?,?,?,?,?,?)",(fullname,address,email,dob,gender,contact))
    conn.commit()
    conn.close()
def view_personal_information():
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("select * from personal_info")
    row=cur.fetchall()
    conn.close()
    return row

def search_by_id_personal_informatio(id):
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("select * from personal_info where id=?",(id,))
    conn.commit()
    conn.close()
def delete_by_id_personal_information(id):
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("delete from personal_info where id=?",(id,))
    conn.commit()
    conn.close()

def update_by_id_personal_information(id,fullname=" ",address=" ",email=" ",dob=" ",gender=" ",contact=" "):
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("select * from personal_info where fullname=? or address=?  or email=? or dob=? or gender=? or contact=?",(fullname,address,email,dob,gender,contact,id))
    conn.commit()
    conn.close()

def search_all_data(fullname=" ",address=" ",email=" ",dob=" ",gender=" ",contact=" "):
    conn=sqlite3.connect("personal_information")
    cur=conn.cursor()
    cur.execute("select * from personal_info where fullname=? or address=?  or email=? or dob=? or gender=? or contact=? ",(fullname,address,email,dob,gender,contact))
    row=cur.fetchall()
    conn.close()
    return row


Personal_Information()

