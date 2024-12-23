# Import libraries
import streamlit as st

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <h1>House price prediction </h1>
    <h2> Features </h2>

    We have the folowing features : <br>
    - **Longitude**: Geographical longitude of the block group's centroid.
    - **Latitude**: Geographical latitude of the block group's centroid.
    - **Housing median age**: Median age of houses in the block group.
    - **Total rooms**:
    - **Total bedrooms**:
    - **Population**:Total population of the block group.
    - **Households**:
    - **Median income**: Median income of households in the block group (in tens of thousands of dollars).
    - **Ocean proximity**:
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h2> Data inputs </h2>
    """,
    unsafe_allow_html=True
)

# Coordinates input
col1, col2 = st.columns(2)
with col1:
    longitude = st.number_input(label = "Longitude")
with col2:
    latitude = st.number_input(label = "Latitude")

# House median age
housing_median_age = st.number_input(label = "Housing median age", min_value=0, step=1)

# Census info
col1, col2 = st.columns(2)
with col1:
    total_rooms = st.number_input(label = "Total rooms", min_value=0, step=1)
with col2:
    total_bedrooms = st.number_input(label="Total bedrooms",min_value=0, step=1)

# Population info
col1, col2 = st.columns(2)
with col1:
    population = st.number_input(label = "Population", min_value=0, step=1)
with col2:
    households = st.number_input(label="Households",min_value=0, step=1)

# Median income
median_income = st.number_input(label = "Median income", min_value=0, step=1)

# Ocean proximity
ocean_proximity = st.number_input(label = "Ocean proximity", min_value=0, step=1)
