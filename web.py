import streamlit as st
import functions


feladatok = functions.get_todos()


def add_todo():
    feladat = st.session_state["uj_feladat"] + "\n"
    feladatok.append(feladat)
    functions.write_todos(feladatok)


st.title("Az Én feladat listám")
st.subheader("Ez az én feladatlistám")
st.write("Ez az alkalmazás megnöveli a produktivitásod.")

for index, feladat in enumerate(feladatok):
    checkbox = st.checkbox(feladat, key=feladat)
    if checkbox:
        feladatok.pop(index)
        functions.write_todos(feladatok)
        del st.session_state[feladat]
        st.experimental_rerun()

st.text_input(label="Új feladat hozzáadása:", placeholder="Írj be egy új feladatot...",
              on_change=add_todo, key="uj_feladat")
