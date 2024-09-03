import streamlit as st
import requests, os
from dotenv import load_dotenv
from src import utils


st.set_page_config("MailBlast - Privacy Policy", "static/logo.png")

st.info("We'd love your feedback! Please take a moment to complete the survey.")

st.title("MailBlast User Survey")


with st.expander("MailBlast User Survey", expanded=True):

    utils.hide_labels(st)

    # load env
    load_dotenv()
    survey_script_url = os.getenv("survey_sheet_url")

    # Another select slider question
    st.write("How easy was it to navigate and use the MailBlast app?")
    simplicity = st.select_slider(
        "",
        options=["Very Easy", "Easy", "Neutral", "Difficult", "Very Difficult"],
    )

    # Another select slider question
    st.write("How satisfied are you with the email customization and sending features?")
    satisfaction = st.select_slider(
        "",
        options=[
            "Very Satisfied",
            "Satisfied",
            "Neutral",
            "Unsatisfied",
            "Very Unsatisfied",
        ],
    )

    # Text input question
    st.write(
        "What additional features would you like to see in future updates of MailBlast?"
    )
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
