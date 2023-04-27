import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', width=400)

with col2:
    st.title('Sai Teja Chary')
    intro = """
        Hi, I am Sai Teja! I am a Python programmer. I graduated in 2020 with a Bachelor of Technology 
        in Electrical and Electronics Engineering from Jawaharlal Nehru Technological University. 
        Currently working as Senior Software Engineer at Capgemini providing services as a GUI Automation Tester.
        """
    st.info(intro)

content = """
Below You can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(f"<h4 style='text-align: center;'>{content}</h4>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        source_url, app_url = st.columns(2)
        with source_url:
            st.write(f"[Source Code]({row['sourceurl']})")
        with app_url:
            st.write(f"[Try App]({row['appurl']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        source_url, app_url = st.columns(2)
        with source_url:
            st.write(f"[Source Code]({row['sourceurl']})")
        with app_url:
            st.write(f"[Try App]({row['appurl']})")