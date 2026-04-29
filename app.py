import pandas as pd
import streamlit as st

df = pd.read_csv("data.csv")

st.title("📊 Survey Data Dashboard")

st.write("### Dataset Preview")
st.dataframe(df)

st.write("### Average Satisfaction")
st.write(df["Satisfaction"].mean())

st.write("### Recommendations")
st.bar_chart(df["Recommend"].value_counts())

st.write("### Filter by Gender")

gender = st.selectbox("Select Gender", df["Gender"].unique())

filtered_df = df[df["Gender"] == gender]

st.dataframe(filtered_df)

st.write("### Key Insights")

st.write("- Most users are satisfied with the service.")
st.write("- Mobile services show higher satisfaction.")
st.write("- Majority of users would recommend the service.")