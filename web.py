import streamlit as st
import Functions
st.set_page_config(layout="wide")
filepath = 'tasks.txt'
lst = Functions.get_lst(filepath)


def add_task():
    task = st.session_state["new_task"]
    Functions.add_task(filepath, task)
    st.session_state["new_task"] = ""

st.title("My To-Do App")
st.subheader("this is my to-do app")
st.write("This app is to increase your <b>productivity!</b>",unsafe_allow_html=True)
st.text_input(label="", placeholder="Add new task...", on_change=add_task, key="new_task")

for item in lst:
    checkbox = st.checkbox(item,key=item)
    if checkbox:
        Functions.complete(filepath,item)
        del st.session_state[item]
        st.experimental_rerun()


