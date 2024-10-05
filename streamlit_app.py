import streamlit as st
import plotly.express as px

# Sample data for the pie chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
values = [450, 300, 200, 150]

# Create a pie chart using Plotly
fig = px.pie(names=labels, values=values, title='Programming Language Popularity')

# Display the pie chart in Streamlit
st.title("Pie Chart Example in Streamlit")
st.plotly_chart(fig)