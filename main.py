import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo2.png",width=600)

with col2:
    st.title("sajjad sokhanvari")
    content = """
    Hi , I am Sajjad! I am a Python programmer,teacher,and founder of PythonHow.
    
    
    """
    st.info(content)
content2="""
Below you can find some of the app,  I have built in Python .
"""
st.write(content2)