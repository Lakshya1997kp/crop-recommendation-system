import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "Admin123###"),
        database=os.environ.get("DB_NAME", "crop_recommendation_app")
    )
    return connection




