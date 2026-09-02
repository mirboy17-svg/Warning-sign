import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 전체 모드 설정 (Wide mode)
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 2. Streamlit 기본 여백 및 흰색 배경 제거 CSS 주입
st.markdown("""
    <style>
        /* 상단 헤더, 햄버거 메뉴 숨기기 */
        header {visibility: hidden;}
        
        /* 메인 컨테이너 상하좌우 여백 0으로 설정 */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        
        /* 외부 기본 스크롤바 숨기기 및 배경색을 좌측 사이드바 색상과 일치 */
        body, .stApp {
            overflow: hidden !important;
            background-color: #0f172a !important; 
        }
        
        /* iframe 크기를 화면 높이에 강제 고정하여 흰 여백 차단 */
        iframe[title="streamlit_components.v1.components.html"] {
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. index.html 파일 읽어서 화면에 렌더링
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=1000)
