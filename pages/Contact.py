import streamlit as st

st.header('Contact')

with st.form(key='email_form'):
    user_email = st.text_input('Enter your email')
    message = st.text_area('Message')
    button = st.form_submit_button('Submit')
    if button:
        st.info('Email sent successfully')


