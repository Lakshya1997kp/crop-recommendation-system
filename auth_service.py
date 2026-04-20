from flask import Flask
import mysql.connector
from werkzeug.security import generate_password_hash
from db import db_connection
from werkzeug.security import check_password_hash


def authentication_for_signup(name, email , password):
    
    
    connection= db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT Id FROM Users WHERE email= %s",(email,))

    if ( cursor.fetchone()):
        connection.close()
        cursor.close()
        return("Email already exists!!")
    
    hashed_password=generate_password_hash(password)

    cursor.execute(
    "INSERT INTO Users (name, email, password) VALUES (%s, %s, %s)",
    (name, email, hashed_password))    
    connection.commit()
    cursor.close()
    connection.close()
    return None


# -------------------------------------------------------------



def authentication_for_login(email, entered_password):
    connection= db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT password FROM Users WHERE email=%s",(email,))
    stored_password = cursor.fetchone()
    if stored_password:
        stored_password=stored_password[0]

        result = check_password_hash(stored_password, entered_password)
        cursor.close()
        connection.close()
        return result 
    cursor.close()
    connection.close()
    return False

