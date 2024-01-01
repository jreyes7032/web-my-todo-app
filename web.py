import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)

# ctr + r = refresh
# streamlit run C:\Users\reyes\Documents\UDEMY\python\DropBox\web.py
# pip install streamlit / streamlit hello to test if working
#  streamlit run web.py [ARGUMENTS]
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.6:8501
# pip freeze > requirements.txt (packages that are needed for this program)

st.title("My Todo App")
st.subheader("This is my todo app.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        print(todos, index)
        st.experimental_rerun()
        # print(todos, index)
        # del st.session_state[todos[index]]
        # todos.pop(index)
        # functions.write_todos(todos)
        # st.experimental_rerun()

textbox = st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

print("hello")
# st.session_state -- use to see the variables for reviewing


