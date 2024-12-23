# Import libraries
import streamlit as st

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Explanation of the purpose of this app
st.markdown(
    """
    <h1>House price prediction </h1>
    <h2> The big picture </h2>
    Welcome to the Machine Learning Housing Corporation! <br><br>
    Our task is to build a model using California census data to predict housing prices.<br><br>
    The data includes details like population, median income, and housing prices for small areas called block groups (or "districts"), which usually have 600–3,000 people.<br><br>
    Our model will use this data to <b>predict the median housing price</b> in a district based on other metrics.<br><br>

    <h2> Framing the problem </h2>
    <h3> What is the business objective is?</h3>
    The goal isn’t just to build a model but to understand how the company plans to use it and benefit from it.<br><br>
    Knowing the objective helps <b>define the problem</b>, <b>choose algorithms</b> <b>select a performance measure</b>, and <b>decide how much effort to spend improving the model</b>.<br><br>
    In our current project, our model’s predictions (median housing prices) will be used by another system, alongside other data, to decide if investing in an area is worthwhile.<br><br>
    <b>This decision is crucial as it impacts revenue</b>.<br><br>

    <h3> What is the current solution (if it exists) ?</h3>
    Understanding it can provide a <b>performance baseline</b> and <b>ideas for solving the problem</b>br><br>
    In our corporation, housing prices are <b>currently estimated manually</b> by experts who gather district data and use complex rules when the median price isn’t available. <br>
    This process is <b>expensive</b>, <b>slow</b>, and <b>often inaccurate—estimates are frequently off by over 30%</b>.<br><br>
    The company wants to train a model to predict median housing prices using district data.<br><br>
    Census data, which includes prices and other district information for thousands of areas, is ideal for this task.<br><br>

    <h3> What is the type of learning ?</h3>
    With the gathered information, we are ready to design our system.<br><br>
    This is a <b>supervised learning task</b> because the model can train on labeled examples (districts with their median housing prices).<br><br>
    It’s a <b>regression task</b> since the goal is to predict a value. Specifically, it’s a <b>multiple regression</b> problem because the prediction uses several features (like population and median income).<br><br>
    It’s <b>univariate regression</b> because only one value (median price) is predicted for each district. If multiple values were predicted, it would be multivariate regression.<br><br>
    Since the data is not continuously flowing, doesn’t require rapid updates, and fits in memory, <b>batch learning</b> is sufficient.<br><br>

    <h2> Selecting a performance measure </h2>
    The next step is to choose a performance measure.<br><br>
    For regression problems, a common choice is the <b>root mean square error (RMSE)</b>.<br><br>
    It shows how much error the model typically makes, giving more weight to larger errors.<br><br>

    <h1>Let's go ! </h1>
    """,
    unsafe_allow_html=True
)
