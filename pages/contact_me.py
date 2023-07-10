import streamlit as st
import send_email

myEmail = "eng.davoudpur@gmail.com"
myPhone = "+98-9360912936"
myTel_ID = "https://t.me/Davoudpur"

st.title('contact me'.title())

st.header('send e_mail:')
with st.form(key='send email'):
    user_email = st.text_input('your email:'.title())
    user_message = st.text_area('your message:'.title())
    button = st.form_submit_button('submit')

    message_body = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""

if button:
    send_email.send_email(message_body)
    st.write('your mail was sent successfully')
