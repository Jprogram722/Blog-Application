"""
This is the login page for the streamlit app
"""

import streamlit as st
import streamlit_authenticator as stauth
import yaml

def login() -> None:
    """
    This function will prompt the user to login in to their account by
    asking for their username and pass word it already has a streamlit interface.
    This function returns authenticator so that user can logout anytime
    """

    with open('config.yml') as file:
        config = yaml.load(file, Loader = yaml.SafeLoader)


    authenticator = stauth.Authenticate(
        config['credentials'], 
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
        )

    name, authtication_status, username = authenticator.login("Login", "main")

    if authtication_status == False:
        st.error("Incorrect Username / Password")


    if authtication_status == None:
        st.warning("Please Enter Your Login Information")

    if authtication_status:
        
        st.session_state['authtication_status'] = authtication_status
        if 'username' not in st.session_state:
            st.session_state['username'] = username
        if 'name' not in st.session_state:
            st.session_state['name'] = name

        st.success("Logged in.")
        authenticator.logout("logout", "main")