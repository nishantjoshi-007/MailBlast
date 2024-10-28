import os, time
import streamlit as st
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer
from email_validator import validate_email
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from string import Template
import src.my_gmail as my_gmail, src.templates as templates
from src.instructions import instructions, home_page_instructions
from src import utils, popup

st.set_page_config("MailBlast - Home Page", "./static/logo.png")

utils.hide_warning(st)

# Initialize session state variables
if "state" not in st.session_state:
    st.session_state["state"] = None
if "creds" not in st.session_state:
    st.session_state["creds"] = my_gmail.load_credentials()
if "custom_subject" not in st.session_state:
    st.session_state["custom_subject"] = ""
if "custom_body" not in st.session_state:
    st.session_state["custom_body"] = ""
if "template_option" not in st.session_state:
    st.session_state["template_option"] = "Custom"

# Sidebar for login/logout
if "creds" in st.session_state and st.session_state["creds"]:

    st.session_state["creds"] = my_gmail.refresh_token_if_expired(st.session_state["creds"])
    user_info = my_gmail.get_user_info(st.session_state["creds"])
    if user_info:
        user_email = user_info.get("email")
        user_name = user_info.get("name")
        st.sidebar.write(f"Logged in as {user_name} ({user_email})")

    # refresh app button
    if st.sidebar.button("Restart App", help="Restarting the app will log you out!"):
        utils.refresh_app(st, 0)

    # instructions popup
    popup_col1, popup_col2 = st.columns(2)
    with popup_col1:
        if st.sidebar.button("Show Instructions"):
            popup.show_modal(st)
            popup.render_modal(st, instructions)

            with popup_col2:
                if st.sidebar.button("Hide Instructions"):
                    popup.hide_modal(st)

    # sample csv download
    utils.download_sample_csv(st)

    # logout button
    if st.sidebar.button("Logout", type="primary"):
        st.write(home_page_instructions, unsafe_allow_html=True)
        st.session_state.clear()
        if os.path.exists("token.pickle"):
            os.remove("token.pickle")
        st.rerun()

else:
    if st.sidebar.button("Login with Google", type="primary"):
        flow = my_gmail.get_flow()
        flow.redirect_uri = my_gmail.REDIRECT_URI

        authorization_url, state = flow.authorization_url(access_type="offline", include_granted_scopes="true")

        st.session_state["state"] = state
        st.write(
            f'<meta http-equiv="refresh" content="0;url={authorization_url}">',
            unsafe_allow_html=True,
        )

    query_params = st.experimental_get_query_params()
    code = query_params.get("code")
    if code:
        try:
            flow = my_gmail.get_flow()
            flow.redirect_uri = my_gmail.REDIRECT_URI

            authorization_response = f'{my_gmail.REDIRECT_URI}?code={code[0]}&state={st.session_state.get("state")}'
            flow.fetch_token(authorization_response=authorization_response)
            creds = flow.credentials
            my_gmail.save_credentials(creds)
            st.experimental_set_query_params()  # Clear query parameters
            st.rerun()
        except Exception as e:
            st.error(f"An error occurred during authentication: {e}")
            st.session_state.clear()
            if os.path.exists("token.pickle"):
                os.remove("token.pickle")

    if st.sidebar.button("Restart App", help="Restarting the app will log you out!"):
        utils.refresh_app(st, 0)

# Main app content
st.title("🚀 Welcome to MailBlast: Ultimate Mass Email Sender Tool! 🚀")

if "creds" in st.session_state and st.session_state["creds"]:

    user_info = my_gmail.get_user_info(st.session_state["creds"])
    if user_info:
        user_email = user_info.get("email")
        user_name = user_info.get("name")
        st.write(f"Welcome to MailBlast, {user_name} ({user_email})")

    # Handle file upload
    uploaded_file = st.file_uploader("Please upload the Excel/csv file.", type=["csv", "xls", "xlsx"])
    st.session_state.file_uploaded = uploaded_file

    # Display the DataFrame if a file is uploaded
    if "file_uploaded" in st.session_state:
        file_uploaded = st.session_state.file_uploaded

        if file_uploaded is not None:
            if file_uploaded.name.endswith("csv"):
                try:
                    df = pd.read_csv(file_uploaded)
                except pd.errors.EmptyDataError:
                    st.warning("The uploaded file is empty. Please upload a valid CSV/Excel file.")
                    df = pd.DataFrame()
            else:
                try:
                    df = pd.read_excel(file_uploaded)
                except ValueError:
                    st.warning("The uploaded file is empty or not a valid Excel file. Please upload a valid file.")
                    df = pd.DataFrame()

            # Check if the DataFrame is empty
            if df.empty:
                st.warning("Please attach a CSV/Excel file to proceed further.")
            else:
                # Show editable data editor
                edited_df = st.data_editor(df)

                # Update session state with the edited DataFrame
                st.session_state["edited_df"] = edited_df

                attachments = st.file_uploader(
                    "Upload the Attachment(s) (optional)", type=None, accept_multiple_files=True
                )
                if "attachments" not in st.session_state or st.session_state["attachments"] != attachments:
                    st.session_state["attachments"] = attachments

                if "show_attachments" not in st.session_state:
                    st.session_state["show_attachments"] = False

                if st.session_state["attachments"]:
                    attach_col1, attach_col2 = st.columns(2)
                    with attach_col1:
                        if st.button("Show Attachments"):
                            st.session_state["show_attachments"] = True

                    with attach_col2:
                        if st.button("Hide Attachments"):
                            st.session_state["show_attachments"] = False

                    if st.session_state["show_attachments"]:
                        for idx, attachment in enumerate(st.session_state["attachments"]):
                            st.write(f"Attachment {idx+1}: {attachment.name}")
                            utils.attachement_file_type(st, attachment, pdf_viewer, idx, pd)
                            st.divider()

                # Allow users to select a predefined template or write their own
                st.session_state["template_option"] = st.selectbox(
                    "Select an Email Template",
                    list(templates.PREDEFINED_TEMPLATES.keys()) + ["Custom"],
                    index=4,
                )

                if st.session_state["template_option"] and st.session_state["template_option"] != "Custom":
                    subject_template = templates.PREDEFINED_TEMPLATES[st.session_state["template_option"]]["subject"]
                    body_template = templates.PREDEFINED_TEMPLATES[st.session_state["template_option"]]["body"]
                    mime_type = "html"
                    st.text_input("Email Subject Template", value=subject_template, disabled=True)
                    st.text_area("Email Body Template", value=body_template, disabled=True)
                else:
                    subject_template = st.text_input(
                        "Custom Email Subject",
                        value=st.session_state["custom_subject"] or "",
                        placeholder="Email Subject Goes Here:",
                    )
                    body_template = st.text_area(
                        "Custom Email Body",
                        value=st.session_state["custom_body"] or "",
                        placeholder="Email Body Goes Here:",
                    )
                    st.session_state["custom_subject"] = subject_template
                    st.session_state["custom_body"] = body_template
                    mime_type = "plain"

                # Preview email
                if st.button("Preview Email"):
                    if len(st.session_state["edited_df"]) > 0:
                        preview_row = st.session_state["edited_df"].iloc[0].to_dict()
                        preview_row["user_name"] = user_name
                        subject = Template(subject_template).substitute(preview_row)
                        body = Template(body_template).substitute(preview_row)

                        if "attachments" in st.session_state and st.session_state["attachments"]:
                            attachment_names = "\n\nAttachments:\n" + "\n".join(
                                [attachment.name for attachment in st.session_state["attachments"]]
                            )
                            body += attachment_names

                        st.subheader("Email Preview")
                        st.write(f"Subject: {subject}")
                        st.write(f"Body:\n{body}")

                # Send emails
                if st.button("Send Emails"):
                    with st.spinner("Sending emails..."):
                        service = build("gmail", "v1", credentials=st.session_state["creds"])
                        for index, row in st.session_state["edited_df"].iterrows():
                            row_dict = row.to_dict()
                            row_dict["user_name"] = user_name
                            # Replace placeholders with actual data
                            subject = Template(subject_template).substitute(row_dict)
                            body = Template(body_template).substitute(row_dict)

                            # Validate email address
                            validate_email(row["recipient_email"])

                            # Collect attachments
                            attachments_email = [
                                {"data": attachment.getvalue(), "name": attachment.name}
                                for attachment in st.session_state["attachments"]
                            ]

                            message = my_gmail.create_message(
                                user_email,
                                row["recipient_email"],
                                subject,
                                body,
                                attachments_email,
                                mime_type=mime_type,
                            )

                            # Send message
                            my_gmail.send_message(service, "me", message)

                        # success message
                        time.sleep(3)
                        utils.success_box(st, "Hooray, Emails are sent successfully!")

                        time.sleep(3)

                        # Clear session state for file and DataFrame before switching
                        if "file_uploaded" in st.session_state:
                            del st.session_state["file_uploaded"]
                        if "attachments" in st.session_state:
                            del st.session_state["attachments"]

                        st.switch_page("pages/User_Survey.py")

else:
    st.write(home_page_instructions, unsafe_allow_html=True)
    utils.download_sample_csv(st)
