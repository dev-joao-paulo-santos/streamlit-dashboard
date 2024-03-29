import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('tabela.csv', sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
# df.sort_values(df["Date"])

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, color="City", x="Date", y="Total", title="Faturamento por dia")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered, color="City", x="Date", y="Product line", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby("City")[("Total")].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

fig_rating = px.bar(df_filtered, y='Rating', x='City', title='Avaliação')
col5.plotly_chart(fig_rating, use_container_width=True)