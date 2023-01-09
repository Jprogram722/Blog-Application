"""
Veiw your profile information
"""

import streamlit as st
import post_db
import time
import random

def generate_id():
    return str(random.randint(1,100000))

def local_css(file):
    """
    Opens and applys changes to how the web app looks using a local css file
    """
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def find_posts(username: str) -> list:
    """
    This function gets all the posts that the logged in user has made.
    """
    user_posts = []
    all_posts = post_db.fetch_all_posts()
    ids = [key['key'] for key in all_posts]
    usernames = [user['author'] for user in all_posts]
    
    for i in range(len(usernames)):
        if usernames[i] == username:
            user_posts.append(post_db.get_post(ids[i]))

    print(user_posts)

    return user_posts

def profile() -> None:
    """
    This function displays the profile page for the blog app
    """

    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None
    else:
        pass

    if 'button' not in st.session_state:
        st.session_state['button'] = False
    else:
        pass

    if st.session_state['authentication_status'] == None:
        st.subheader("You need to be logged in to use to option")


    if st.session_state['authentication_status']:
        st.header(st.session_state.username)

        user_posts = find_posts(username = st.session_state.username)

        st.subheader("Your Posts:")
        for i in range(len(user_posts)):
            html = f"""
            <div class="container">
                <h3 class="title">{user_posts[i]['title']}</h3<br>
                <p class="author">Author: {user_posts[i]['author']}</p><br>
                <p class="post">{user_posts[i]['post']}
            </div>
            """

            st.markdown(html, unsafe_allow_html=True)
            local_css("style/style.css")

        add_btn = st.button("Add Post")

        if st.session_state['button'] == False:
            st.session_state['button'] = add_btn

        if st.session_state['button']:

            with st.form("Blog"):
                blog_title = st.text_input(label="Title:", placeholder="Love And Thunder")
                blog_content = st.text_area(label="Content:", placeholder="Hello World")

                submit = st.form_submit_button(label = "Post")

                if submit:
                    with st.spinner("Making Post..."):
                        post_db.insert_post(generate_id() ,st.session_state.username, blog_title, blog_content)
                        time.sleep(2)
                        st.success("Blog Post Made!!!")