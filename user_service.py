from flask import Flask
from db import db_connection

def get_userdata(email):
    connection=db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT Name, email FROM Users WHERE email=%s",(email,))

    Userdata=cursor.fetchone()
    if Userdata:
        cursor.close()
        connection.close()
        return Userdata
    cursor.close()
    connection.close()
    return False
    
def update_name(new_name,email):
    connection=db_connection()
    cursor=connection.cursor()

    cursor.execute("UPDATE Users SET Name= %s WHERE email=%s",(new_name,email))
    connection.commit()
    cursor.close()
    connection.close()
    return True




def update_email(new_email,old_email):
    connection=db_connection()
    cursor=connection.cursor()

    cursor.execute("UPDATE Users SET email= %s WHERE email=%s",(new_email,old_email))
    connection.commit()
    cursor.close()
    connection.close()
    return True

def delete_account(email):
    connection=db_connection()
    cursor=connection.cursor()

    cursor.execute("DELETE  FROM Users WHERE email=%s",(email,))
    connection.commit()
    cursor.close()
    connection.close()
    return True