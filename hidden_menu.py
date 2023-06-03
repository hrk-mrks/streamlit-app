import streamlit as st
def hidden_menu_and_footer():
  hidden_menu_and_footer = """
  <style>
    footer{
      visibility: hidden;
      }
    #MainMenu{
    visibility: hidden;
    }
  </style>
  """
  st.markdown(hidden_menu_and_footer, unsafe_allow_html=True)