import streamlit as st

import pandas

st.set_page_config(layout='wide')

col1 , col2=st.columns(2)

with col1:
    st.image('Faizan Ali.png')
    
with col2:
    st.title('Faizan Ali')
    content="""My name is Faizan Ali. I am a Highschool student i am studying in 12th class .I live in Pakistan."""
    st.info(content)
    
st.write("Below you can find my projects. Feel free to contact me.")

col3, empty, col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"Source code]({row['url']})")
    
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"Source code]({row['url']})")





