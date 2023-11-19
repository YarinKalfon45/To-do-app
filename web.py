

import streamlit as st
import Functions
st.set_page_config(layout="wide")
filepath = 'tasks.txt'  # Default filepath
lst = Functions.get_lst(filepath)


def add_task():
    """
    This is a function for the web app that adds new task
    :return:
    """
    task = st.session_state["new_task"]  # Saving the task the user inputted
    Functions.add_task(filepath, task)  # Using our function to add a new task for the list
    st.session_state["new_task"] = ""  # Clearing the input box

st.title("My To-Do App")
st.subheader("this is my to-do app")
st.write("This app is to increase your <b>productivity!</b>",unsafe_allow_html=True)
st.text_input(label="", placeholder="Add new task...", on_change=add_task, key="new_task")

"""
This next loop job is to remove checked tasks from the to do list
"""
for item in lst:  # Iterating over every element in the list
    checkbox = st.checkbox(item,key=item)
    if checkbox:  # If checkbox in checked
        Functions.complete(filepath,item)  # Using our complete function
        del st.session_state[item]
        st.experimental_rerun()


