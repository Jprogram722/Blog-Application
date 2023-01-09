"""
This python file contains the commmands to store info in a database
"""

import os
from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# initialize Deta
deta = Deta(DETA_KEY)

# Create/Connect to database for the user
db = deta.Base("users_db")

#--------------------------THIS IS FOR THE USER DATABASE-------------------------

def insert_user(username:str, password:str, email:str, name:str) -> None:
    """
    inserts user data into a data base
    """
    return db.put({'key': username, 'password': password, 'email': email, 'name': name})

def get_user(username:str) -> dict:
    """
    Get a dictionary containing data on a user
    """
    return db.get(username)

def update_user(username:str, updates:str) -> None:
    """
    Update user data in the database
    """
    return db.update(updates, username)

def delete_user(username:str) -> None:
    """
    Delete user from the database
    """
    return db.delete(username)

def fetch_all_users() -> dict:
    """
    Returns a dictionary contianing all users
    """
    res = db.fetch()
    return res.items