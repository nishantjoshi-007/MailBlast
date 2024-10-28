import streamlit as st
import requests, os
from dotenv import load_dotenv
from src import utils
from streamlit_star_rating import st_star_rating


st.set_page_config("MailBlast - Privacy Policy", "static/logo.png")

st.title("MailBlast User Survey")

st.info("We'd love your feedback! Please take a moment to complete the survey.")

# Custom CSS to style the select slider
st.markdown(
    """
    <style>
    .StyledThumbValue[data-testid="stThumbValue"] {
        color: rgb(124, 252, 0) !important;
    }
    .st-emotion-cache-1vzeuhh.ew7r33m3{
        background-color: rgb(124, 252, 0) !important;
    }
    .st-av.st-aw.st-ax.st-ay.st-cy.st-cu.st-b9.st-cv.st-cw{
        background: linear-gradient(to right, rgb(124, 252, 0) 0%, 
        rgb(124, 252, 0) 50%, rgba(172, 177, 195, 0.25) 50%, 
        rgba(172, 177, 195, 0.25) 100%) !important;
    }
    .st-av.st-aw.st-ax.st-ay.st-cz.st-cu.st-b9.st-cv.st-cw{
        background: linear-gradient(to right, rgb(124, 252, 0) 0%, 
        rgb(124, 252, 0) 100%, rgba(172, 177, 195, 0.25) 100%, 
        rgba(172, 177, 195, 0.25) 100%) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.expander("MailBlast User Survey", expanded=True):

    utils.hide_labels(st)

    # load env
    load_dotenv()
    survey_script_url = os.getenv("survey_sheet_url")

    # Another select slider question
    st.write("How easy was it to navigate and use the MailBlast app?")
    simplicity = st_star_rating("", maxValue=5, defaultValue=3, key="simplicity")

    # Another select slider question
    st.write("How satisfied are you with the email customization and sending features?")
    satisfaction = st_star_rating("", maxValue=5, defaultValue=3, key="satisfaction", emoticons=True)

    # Text input question
    st.write("What additional features would you like to see in future updates of MailBlast?")
    new_features = st.text_area("")

    # another select slider question
    st.write("How likely are you to recommend MailBlast to a friend or colleague?")
    recommend = st.select_slider(
        "",
        options=["Very Likely", "Neutral", "Not Likely"],
    )

    # submit
    if st.button("Submit Survey", type="primary"):
        data = {
            "simplicity": simplicity,
            "satisfaction": satisfaction,
            "new_feature": new_features,
            "recommend": recommend,
        }

        if survey_script_url is not None:
            response = requests.post(survey_script_url, json=data)

            if response.status_code == 200:
                st.success("Thank you for your feedback!")
            else:
                st.error("An error occurred. Please try again.")
