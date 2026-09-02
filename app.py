import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="MSDS Auto-Generator Platform", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100vw !important; height: 100vh !important; border: none !important; }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error("⚠️ index.html 파일을 찾을 수 없습니다. GitHub 최상위 폴더에 파일이름이 정확한지 확인해주세요.")
