import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Sai Teja Chary')
    intro = """
        Hi, I am Sai Teja! I am a Python programmer. I graduated in 2020 with a Bachelor of Technology 
        in Electrical and Electronics Engineering. Currently working as Senior Software Engineer at Capgemini, 
        providing services as an Automation Tester for Morgan Stanley.
        """
    st.info(intro)

content = """
Below You can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)