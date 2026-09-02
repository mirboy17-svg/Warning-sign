import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Streamlit 페이지 설정 (전체화면, 사이드바 닫기)
st.set_page_config(
    page_title="MSDS Auto-Generator Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 기본 UI(헤더, 푸터, 여백) 숨기기 및 HTML 강제 전체화면 설정
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 기본 여백 완전 제거 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* HTML 화면을 꽉 채우도록 설정 */
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. index.html 파일 절대 경로로 안전하게 찾아오기
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "index.html")

# 4. HTML 화면에 렌더링하기
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 높이를 충분히 주어 스크롤이 원활하게 작동하도록 설정
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error("⚠️ index.html 파일을 찾을 수 없습니다. GitHub 최상위 폴더에 파일이름이 정확한지 확인해주세요.")
