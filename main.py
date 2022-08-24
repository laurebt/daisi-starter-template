import streamlit as st

def hello(name="Daisi"):
    return f"Hello {name}!"

def app():
    name = st.text_input('Type your name', value = "Daisi user")
    greeting = hello(name)
    st.header(greeting)

if __name__ == '__main__':
    app()
