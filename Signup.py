"""
Author: Jared Park
This is the signup page for the streamlit blog app
"""

import streamlit as st
import db
import time
import streamlit_authenticator as stauth
from to_yaml import make_yaml_file

def make_account(email:str, username:str, password:str, re_pass:str, hashed_password:str, name:str) -> None:
    """
    This function takes in all the info from the sign up form
    and makes a profile in the deta database and the ymal file
    """

    if password != re_pass:
        st.error("Retyped password does not match entered pass word")

    else:
        db.insert_user(username, hashed_password, email, name)
        make_yaml_file()
        st.success("Account has been created")

def check_auth() -> bool:
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None
    return st.session_state['authentication_status']


def signup() -> None:
    """
    This function will make the sign up form for the blog app
    """
    auth = check_auth()

    if auth == False or auth == None:
        with st.form(key = 'Signup'):
            st.subheader("Sign Up")
            email = st.text_input(
                label = "Email:"
            )
            username = st.text_input(
                label = "Username:",
                max_chars = 30
            )
            name = st.text_input(
                label = "First Name:",
                max_chars = 30
            )
            password = st.text_input(
                label = "Password:",
                type = "password",
                max_chars = 30
            )
            re_pass = st.text_input(
                label = "Retype Password:",
                type = "password"
            )

            submit = st.form_submit_button(label = "Sign Up")

            if submit:
                with st.spinner("Making Profile..."):
                    hashed_password = stauth.Hasher([password,]).generate()
                    make_account(email, username, password, re_pass, hashed_password, name)
                    time.sleep(2)
    if auth:
        st.write("Cannot Make An Account While Signed In.")

