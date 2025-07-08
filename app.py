import streamlit as st
import pandas as pd
from data_cleaner import clean_data
from graph_generator import generate_plot

st.set_page_config(layout="wide")
st.title("📊 CSV Graph Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Data")
    st.dataframe(df)

    cleaned_df = clean_data(df)
    st.subheader("🧹 Cleaned Data")
    st.dataframe(cleaned_df)

    st.sidebar.header("📌Plot Your Graph")

    all_columns = cleaned_df.columns.tolist()
    x_axis = st.sidebar.selectbox("X-axis", all_columns)
    y_axis = st.sidebar.selectbox("Y-axis", all_columns)
    chart_type = st.sidebar.selectbox("Chart Type", ['Line', 'Bar', 'Scatter', 'Pie'])
    chart_title = st.sidebar.text_input("Graph Title", "Graph Title")

    if st.sidebar.button("Generate Graph"):
        fig = generate_plot(cleaned_df, x_axis, y_axis, chart_type, chart_title)
        st.plotly_chart(fig, use_container_width=True)

    if st.sidebar.button("Download Cleaned CSV"):
        st.download_button(
            label="Download Cleaned CSV",
            data=cleaned_df.to_csv(index=False).encode('utf-8'),
            file_name='cleaned_data.csv',
            mime='text/csv',
        )
