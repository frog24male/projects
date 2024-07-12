import streamlit as st

st.set_page_config(layout='wide')

col1 , col2=st.columns(2)

with col1:
    st.image('images/photo.png')
    
with col2:
    st.title('Faizan Ali')
    content="""My name is Faizan Ali. I am a Highschool student i am studying in 12th class .I live in Pakistan."""
    st.info(content)
    
st.write("Below you can find my projects. Feel free to contact me")
