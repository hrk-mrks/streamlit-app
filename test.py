import streamlit as st
import numpy as np
import pandas as pd
import time
import hidden_menu


st.sidebar.title('Streamlit 入門')

# プレぐれスバ
st.write('プログレスバー')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  latest_iteration.text(f'{i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

# チェックボックス
if st.sidebar.checkbox('show imgage') :
  st.write('チェック！')


# セレクトボックス
option = st.sidebar.selectbox(
  'あなたが好きな数字を教えてください',
  list(range(1,11))
)
st.write(f'あなたの好きな数字は{option}です')

# テキスト
text = st.text_input('あなたの趣味を教えてください')
st.write(f'あなたの趣味は{text}です')

# スライダ
condition = st.slider('あなたの今の調子は？', 0,100,50)
st.write(f'あなたの調子は{condition}です')

# 列
left_column, right_column = st.columns(2)
button = left_column.button('右からむに文字を表示')
if button:
  right_column.write('もじだよ')

expander = st.expander('問い合わせ')
expander.write('ないようだよ')


# 文字を書く
st.write('Dataframe')


df = pd.DataFrame(
  {
    '1列目': [1,2,3,4],
    '2列目': [2,3,4,5]
  }
)

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=400)

st.table(df.style.highlight_max(axis=0))

"""
# 見出し1
aaaa

- a
- a


"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']             
)

st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon'] 
)

st.map(df3)

