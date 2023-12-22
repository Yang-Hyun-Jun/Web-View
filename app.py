import streamlit as st
import pandas as pd
import numpy as np


# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="Generative Alpha Search Model (BETA)",
    layout="wide",
)

# 로딩바 구현하기
# with st.spinner(text="페이지 로딩중..."):
#     sleep(2)

image_path = '/home/hyunjun/workspace/beta_GAS/Silentist.png'

st.image(image_path, width=300)

# 페이지 헤더, 서브헤더 제목 설정
st.header("Generative Alpha Search Model (BETA)")

cols = st.columns((1, 1))

# Meta 정보 지정 섹션
############################################################################################
# Ticker 선택
ticker = cols[0].selectbox(
    'Select the ticker that is the target of your strategy',
    ('BTCUSDT', 'ETHUSDT', 'DOGEUSDT'))

# Start Quarter 선택
start_quarter = cols[0].selectbox(
    'Select a period to start searching your strategy',
    ('2019Q3', '2019Q4', '2020Q1'))

# Trading Mode 선택
trade_mode = cols[1].selectbox(
    'Select the trading mode of your strategy',
    ('Long-Only', 'Short-Only', 'Long-Short Swithcing'))

# End Quarter 선택
end_quarter = cols[1].selectbox(
    'Select a period to end searching your strategy',
    ('2022Q2', '2022Q3', '2022Q4'))


st.markdown("---")

# Alpha Performance 지정 섹션
############################################################################################
default_text = 'Generate a trading rule with a Sharpe ratio of 1.0 or higher.'
prompt = st.text_input("Describe the desired investment performance", value=default_text)

cols = st.columns((1, 1, 1))


expected_return = cols[0].slider('Expected Return', 0.0, 1.0, 0.5)
share_ratio = cols[0].slider('Sharpe Ratio', 0.0, 1.0, 0.5)
volatility = cols[0].slider('Volatility', 0.0, 1.0, 0.5)
sortino = cols[1].slider('Sortino Ratio', 0.0, 1.0, 0.5)
pnl_ratio = cols[1].slider('PNL Ratio', 0.0, 1.0, 0.5)
win_ratio = cols[1].slider('WIN Ratio', 0.0, 1.0, 0.5)
tpi_ratio = cols[2].slider('TPI', 0.0, 1.0, 0.5)
calmar = cols[2].slider('Calmar Ratio', 0.0, 1.0, 0.5)
############################################################################################

st.markdown("---")


# 생성 알파 결과 뷰 섹션
############################################################################################
st.subheader("Generated Alphas")


alpha1 = 'AND()\n├── NOT()\n│   └── NewHigh(3)\n│       └── DATA[Close]\n└── SmallerThan(3)\n    └── MIN(3)\n        └── DATA[Low]'
alpha2 = 'Comparison()\n├── MIN(3)\n│   └── DATA[Volume]\n└── DIV()\n    ├── DATA[Close]\n    └── DATA[Close]'

df = pd.DataFrame([{'trading_col': 9339,
 'max_return': 6.18654,
 'min_return': -0.0163,
 'max_drawdown': -0.5663,
 'trading_count (yearly)': 201.6488,
 'expected_return (yearly)': 0.52148,
 'volatility (yearly)': 0.66343,
 'sortino_ratio (yearly)': -2.56711,
 'sharpe_ratio (yearly)': 0.7860,
 'calmar_ratio': 0.92079,
 'pnl_ratio': 1.20522,
 'win_ratio': 0.5069,
 'tpi': 1.11799}])


on = st.toggle('Generate Alpha 1')

if on:
    
    metrics = df
    np.random.seed(42)

    plot = pd.DataFrame(
        np.random.random((20, 2)),
        columns=['a', 'b']
    )

    cols = st.columns((1, 5))
    cols[0].subheader('Long Strategy')
    cols[0].text(alpha1)
    cols[0].subheader('Short Strategy')
    cols[0].text(alpha2)
    # cols[2].line_chart(chart_data)
    cols[1].caption('Back-Testing Results')
    cols[1].dataframe(metrics, hide_index=True)
    cols[1].line_chart(plot)


on2 = st.toggle('Generate Alpha 2')

if on2:
    
    metrics = df

    plot = pd.DataFrame(
        np.random.random((20, 2)),
        columns=['a', 'b']
    )

    cols = st.columns((1, 5))
    cols[0].subheader('Long Strategy')
    cols[0].text(alpha1)
    cols[0].subheader('Short Strategy')
    cols[0].text(alpha2)
    cols[1].caption('Back-Testing Results')
    cols[1].dataframe(metrics, hide_index=True)
    cols[1].line_chart(plot)

############################################################################################

