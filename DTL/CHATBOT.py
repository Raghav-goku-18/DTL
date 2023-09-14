from bardapi import Bard
import os
import streamlit as st

os.environ['_BARD_API_KEY'] = "awiyiyMC9DINTYb9TSMyUfgw7wRPmfJGQNETKyhH-uYQ__RjGCfhUlu9h3WbsfXoA0wUhw."

st.title("Academic Sage")

# Initialize session_state
if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'paste' not in st.session_state:
    st.session_state['paste'] = []

def response_api(prompt):
    message = Bard().get_answer(prompt)['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Doubt:")
    return input_text

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state['generate'].append(output)
    st.session_state['paste'].append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        st.write(st.session_state['paste'][i], is_user=True, key=str(i) + '_user')
        st.write(st.session_state['generate'][i], key=str(i))