import streamlit as st

st.set_page_config(layout='wide')

col1 , col2=st.columns(2)

with col1:
    st.image('images/photo.png')
with col2:
    st.title('Faizan Ali')
    content="""my name is Faizan Ali. I am a highschool student i am studyinng in 12th class .i live in Pakistan."""
    st.info(content)