import streamlit as st
import pandas as pd

# 페이지 제목
st.title("주식 투자 포트폴리오 관리 데모")
st.write("이 데모 페이지에서는 기본적인 포트폴리오 정보를 확인할 수 있습니다.")

# 샘플 포트폴리오 데이터 생성
data = {
    "종목": ["AAPL", "GOOGL", "TSLA"],
    "보유 수량": [10, 5, 2],
    "평균 매입가": [150, 2700, 800]
}
portfolio = pd.DataFrame(data)

# 포트폴리오 테이블 출력
st.subheader("포트폴리오 현황")
st.dataframe(portfolio)

# 사이드바를 활용한 항목 추가 (기능 데모)
st.sidebar.header("새 포트폴리오 항목 추가")
symbol = st.sidebar.text_input("종목 코드", placeholder="예: AAPL")
quantity = st.sidebar.number_input("보유 수량", min_value=0, value=0)
purchase_price = st.sidebar.number_input("평균 매입가", min_value=0.0, value=0.0)
if st.sidebar.button("추가"):
    st.sidebar.info("새 항목 추가 기능은 데모 버전에서 지원되지 않습니다.")
