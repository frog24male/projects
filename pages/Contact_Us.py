import streamlit as st
from send_email import send_emaill

st.header("Contact Me")
with st.form(key="email_form"):
    user_email=st.text_input("Your Email")
    message=st.text_area("Your message")
    button=st.form_submit_button("Submit")
    message=f"""\
    Subject: New email for testing
    
    From: {user_email}
    {message}"""
    if button:
        send_emaill(message)
        st.info("Your emaill wa sent successfully")
        
        
        
        
