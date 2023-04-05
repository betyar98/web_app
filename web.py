import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo.local = st.session_state["uj_feladat"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Az Én feladat listám")
st.subheader("Ez az én feladatlistám")
st.write("Ez az alkalmazás megnöveli a produktivitásod.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Új feladat hozzáadása:", placeholder="Írj be egy új feladatot...",
              on_change=add_todo, key="uj_feladat")
