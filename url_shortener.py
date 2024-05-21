import streamlit as st 
import pyperclip
import pyshorteners as pyst

def display_url():
    global url
    shortened_url = shortener.tinyurl.short(url)
    st.title("Shortened URL")
    st.markdown(f"{shortened_url}")
    def copy():
        global shortened_url
        pyperclip.copy(shortened_url)
    cp_btn = st.button("Copy",on_click=copy)
    
    

shortener = pyst.Shortener()
st.write("URL Shortener")
st.markdown("---")
form = st.form("name")
url = form.text_input("Enter URL here....")
btn  = form.form_submit_button("Shorten")
if btn:
    display_url()