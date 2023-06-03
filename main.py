import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import hidden_menu

hidden_menu.hidden_menu_and_footer()

st.title("米国株価可視化アプリ")

st.sidebar.write(
    """
# GAFA株価
可視化ツールです。
"""
)

st.sidebar.write(
    """
## 表示日数選択
"""
)

days = st.sidebar.slider("日数", 1, 50, 20)

st.write(f"""### 過去{days}日間のGAFA株価""")


@st.cache_data
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{days}d")
        hist.index = hist.index.strftime("%Y-%m-%d")
        hist = hist[["Close"]]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    return df


try:
    tickers = {
        "apple": "AAPL",
        "facebook": "META",
        "google": "GOOGL",
        "microsoft": "MSFT",
        "netflix": "NFLX",
        "amazon": "AMZN",
    }

    df = get_data(days, tickers)

    companies = st.multiselect(
        "会社名を選択してください", list(df.index), ["google", "amazon", "facebook", "apple"]
    )

    if not companies:
        st.error("少なくとも一社は選んでください")
    else:
        data = df.loc[companies]
        ymin, ymax = data.min().min(), data.max().max()
        st.write("### 株価(USD)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["Date"]).rename(
            columns={"value": "Stock Prices(USD)"}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y(
                    "Stock Prices(USD):Q",
                    stack=None,
                    scale=alt.Scale(domain=[ymin, ymax]),
                ),
                color="Name:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error("エラーが発生しました")
