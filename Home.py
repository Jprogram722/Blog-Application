"""
Author: Jared Park
This program will allow users you create blog posts
"""

import streamlit as st
import post_db
from Login import login
from Signup import signup
from Profile import profile
from streamlit_option_menu import option_menu

def local_css(file):
    """
    Opens and applys changes to how the web app looks using a local css file
    """
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def check_auth() -> bool:
    """
    This function will check to see if the user is authenticated or not
    """
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None
    return st.session_state['authentication_status']

def menu():
    """
    This function displays the streamlit options menu and returns the options set by the menu
    """
    auth = check_auth()

    if auth == False or auth == None:
        main_menu = option_menu(
            None, 
            options = ['Home', 'Profile', "Log In", "Sign Up"], 
            icons = ['house', 'card-text', 'person', 'door-open'],
            orientation = 'horizontal'
        )

    if auth:
        main_menu = option_menu(
            None, 
            options = ['Home', 'Profile', "Log out", "Sign Up"], 
            icons = ['house', 'card-text', 'person', 'door-open'],
            orientation = 'horizontal'
        )

    return main_menu

main_menu = menu()

def main() -> None:
    """
    This function displays the introduction page and all the posts made
    """

    html = """
    <h1><center>Blog Application</center></h1>
    <h3><center>Streamlit Application By: Jared Park</center></h3>
    """

    st.markdown(html, unsafe_allow_html=True)

    posts = post_db.fetch_all_posts()

    for post in posts:
        text = f"""
            <div class="container">
                <h3 class="title">{post['title']}</h3<br>
                <p class="author">Author: {post['author']}</p><br>
                <p class="post">{post['post']}
            </div>
            """
        st.markdown(text, unsafe_allow_html=True)
        local_css("style/style.css")


if main_menu == 'Log In' or main_menu == 'Log out':
    login()
if main_menu == 'Sign Up':
    signup()
if main_menu == 'Home':
    main()
if main_menu == 'Profile':
    profile()