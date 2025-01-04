# Import libraries
import streamlit as st
import pandas as pd

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
"""
    <h1>House price prediction </h1>
    <h2> Specific issues and objectives </h2>

    <h3> Nature of the problem </h3>
    This is a <b>regression task</b> where the objective is to predict housing prices.<br>

    <h3> Priority criterion  </h3>
    For regression problems, a common choice is the <b>root mean square error (RMSE)</b>.<br>
    It shows how much error the model typically makes, giving more weight to larger errors.<br>
    We'll also look at some other metrics ! <br><br>

    <h2> Data analysis </h2>

    <h3> Features </h3>
    - Categorical features (e.g., proximity to ocean).<br><br>

    """,
    unsafe_allow_html=True
)
st.image("data/count_plots_Categorical.png", caption="Proximity to ocean")

st.markdown(
"""
    - Numerical features (e.g., income, average credit card spending).<br><br>
    """,
    unsafe_allow_html=True
)
st.image("data/hist_plots_Numerical.png", caption="Examples of numerical features")

st.markdown(
"""
    <h3> Correlation between features </h3>
    """,
    unsafe_allow_html=True
)
st.image("data/correlation_numerical.png", caption="Correlation between numerical features")

st.markdown(
"""
    <h2> Model comparison </h2>
    <h3> Cross validation </h3>
    Let's compute different metrics for each regression model we want to train <b>AFTER CROSS VALIDATION</b> (cv = 5) : <br><br>
    """,
    unsafe_allow_html=True
)

compare_metrics = pd.read_csv("data/compare_metrics.csv")
st.dataframe(data = compare_metrics, hide_index=True)

st.markdown(
"""
    <h3> Residuals </h3>
    Let's plot the boxplots, Q-Q plots and KDE plots for each regression model we want to train : <br><br>
    """,
    unsafe_allow_html=True
)
st.image("data/residuals_summary.png", caption="Residuals plots")


st.markdown(
"""
    The **Random Forest Regressor** has : <br>
    - the highest mean **R2**<br>
    - the lowest mean **MAE**<br>
    - the lowest mean **RMSE**<br>
    - the lowest mean **residuals**<br>
    - the lowest **error magnitudes of residuals**<br><br>

    We select the **Random Forest Regressor** !
    """,
    unsafe_allow_html=True
)

st.markdown(
"""
    <h2> Explainability of the model</h2>
    After fine-tuning our <b>Random Forest Regressor</b> through <b>Random Grid Search</b>, we perform <b>feature permutation importance</b> technique to evaluate the importance of individual features (or predictors) in a predictive model. It provides a measure of how much
    a model's performance is affected when the values of a particular feature are randomly shuffled, effectively breaking any
    relationship between that feature and the target variable.<br><br>
    """,
    unsafe_allow_html=True
)
st.image("data/feature_permutation_importance.png", caption="Feature permutation importance based on F1 score")

st.markdown(
"""
    The median income of households in the block group is the most important feature on the prediction.
    """,
    unsafe_allow_html=True
)

# st.markdown(
# """
#     <h2> Final validation </h2>
#     Let's check the model performance on a test set not used during training.<br><br>
#     """,
#     unsafe_allow_html=True
# )
# st.image("data/confusion_matrix_final_model.png", caption="Final validation with test set")

# st.markdown(
# """
#     With this model, we can achieve (<b>on class 1</b>):
#     - <b>96%</b> recall
#     - <b>80%</b> precision .
#     - <b>87%</b> for F1 score. <br><br>
#     """,
#     unsafe_allow_html=True
# )
