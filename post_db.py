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
db = deta.Base("post_db")

#-------------------------------THIS IS FOR THE POST DATABASE--------------------------

def insert_post(id:str, username:str, title:str, post:str):
    """
    Inserts post into database
    """
    return db.put({'key':id,'author': username, 'title': title, 'post': post})

def get_post(id:str) -> dict:
    """
    Get a dictionary containing data on a post
    """
    return db.get(id)

def update_post(id:str, updates:str) -> None:
    """
    Update post data in the database
    """
    return db.update(updates, id)

def delete_post(id:str) -> None:
    """
    Delete post from the database
    """
    return db.delete(id)

def fetch_all_posts() -> dict:
    """
    Returns a dictionary contianing all posts
    """
    res = db.fetch()
    return res.items