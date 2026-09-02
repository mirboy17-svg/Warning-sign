import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Streamlit 페이지 설정 (전체화면, 사이드바 숨김)
st.set_page_config(
    page_title="MSDS Auto-Generator Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 기본 UI(헤더, 푸터, 패딩) 숨기기 및 iframe 높이 강제 설정
# (기존 HTML 프로그램이 화면에 꽉 차게 나오도록 CSS 강제 조작)
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 기본 여백 제거 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* iframe 100% 채우기 */
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. index.html 파일 절대 경로로 안전하게 찾아서 렌더링하기
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 컴포넌트를 사용하여 렌더링
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error(f"⚠️ '{html_file_path}' 경로에서 index.html 파일을 찾을 수 없습니다. 깃허브에 파일이름이 정확한지 확인해주세요.")
