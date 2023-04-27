import streamlit as st
from send_email import send_email

st.header('Contact')

with st.form(key='email_form'):
    user_email = st.text_input('Email Id')
    raw_message = st.text_area('Message')
    message = f"""\
Subject: New mail from {user_email}

From {user_email}
{raw_message}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Email sent successfully')



