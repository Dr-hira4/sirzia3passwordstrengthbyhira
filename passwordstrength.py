#project 02: password strength meter sir zia project.

import re
import streamlit as st

#page styling
st.set_page_config(page_title="password strength checker by Hira", page_icon="@", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto }
    .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: #45a049;}
<style>
""", unsafe_allow_html=True)

#page title and description
st.title("password strength generator")
st.write("enter your password below to check its security level. ")

#function to check password strength
def check_password_strength(password) :
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append(" password should be **atleast 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("password should include **at least one number (0-9)**.")

    #special characters
    if re.search(r"[1@#%^&*]", password):
        score +=1
    else:
        feedback.append("include **at least one special character (!@#$^&*)**.")

    #display password strength results
    if score == 4:
        st.success(" **strong password** - your password is secure.")
    elif score == 3:
        st.info("**moderate password** - consider improving security by adding more feature.")
    else:
        st.error("**weak password** - follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander(" **improve your password**."):
            for item in feedback:
                st.write(item)
password = st.text_input("enter your password:", type="password", help="ensure your password is strong")

#button working
if st.button("check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("please enter a password first!") #show warning if password empty