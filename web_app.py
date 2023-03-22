import streamlit as sl
import functions

todos = functions.get_todos()

#Function to add new task
def add_todo():
    todo = sl.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)

#this will create a title in the webapp.
sl.title("My To-Do app")
sl.write("This app will help you increase your productivity")

# this loop will delete the selected tasks.

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

#adds text where we can add new task
sl.text_input(label="", placeholder="Enter new todo..",
              on_change=add_todo, key="new_todo")

