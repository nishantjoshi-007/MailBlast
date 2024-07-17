import os, time
import streamlit as st
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer
from email_validator import validate_email, EmailNotValidError
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from string import Template 
import src.my_gmail as my_gmail, src.templates as templates
from src.instructions import instructions, home_page_instructions
from src import utils
from src import popup

st.set_page_config("MailBlast", "./static/logo.png")

utils.hide_warning(st)

# Initialize session state variables
if 'state' not in st.session_state:
    st.session_state['state'] = None
if 'email_sent' not in st.session_state:
    st.session_state['email_sent'] = False
if 'creds' not in st.session_state:
    st.session_state['creds'] = my_gmail.load_credentials()
if 'last_activity' not in st.session_state:
    st.session_state['last_activity'] = time.time()

# Define session timeout in seconds (e.g., 30 minutes)
SESSION_TIMEOUT = 30 * 60

# Update last activity timestamp
st.session_state['last_activity'] = time.time()

# Check for session timeout
utils.check_session_timeout(st, SESSION_TIMEOUT)

# Sidebar for login/logout
if 'creds' in st.session_state and st.session_state['creds']:
    st.session_state['creds'] = my_gmail.refresh_token_if_expired(st.session_state['creds'])
    user_info = my_gmail.get_user_info(st.session_state['creds'])
    if user_info:
        user_email = user_info.get('email')
        user_name = user_info.get('name')
        st.sidebar.write(f"Logged in as {user_name} ({user_email})")
    if st.sidebar.button("Logout", type='primary'):
        st.write(home_page_instructions, unsafe_allow_html=True)
        st.session_state.clear()
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
        st.experimental_rerun()

    popup_col1, popup_col2 = st.columns(2)
    with popup_col1:
        if st.sidebar.button("Show Instructions"):
            popup.show_modal(st)
            popup.render_modal(st, instructions)
            
            with popup_col2:       
                if st.sidebar.button("Hide Instructions"):
                    popup.hide_modal(st)

else:
    if st.sidebar.button("Refresh App"):
        utils.refresh_app(st, 0)
    if st.sidebar.button("Login with Google", type='primary'):
        flow = my_gmail.get_flow()
        flow.redirect_uri = my_gmail.REDIRECT_URI

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )

        st.session_state['state'] = state
        st.write(f'<meta http-equiv="refresh" content="0;url={authorization_url}">', unsafe_allow_html=True)
        
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
            st.experimental_rerun()
        except Exception as e:
            st.error(f"An error occurred during authentication: {e}")
            st.session_state.clear()
            if os.path.exists('token.pickle'):
                os.remove('token.pickle')

# Main app content
st.title("🚀 Welcome to MailBlast: Ultimate Mass Email Sender Tool! 🚀")

if 'creds' in st.session_state and st.session_state['creds']:

    user_info = my_gmail.get_user_info(st.session_state['creds'])
    if user_info:
        user_email = user_info.get('email')
        user_name = user_info.get('name')
        st.write(f"Welcome to MailBlast, {user_name} ({user_email})")
    
        utils.download_sample_csv(st) 
    
    # Handle file upload
    uploaded_file = st.file_uploader('Please upload the Excel/csv file.', type=['csv', 'xls', 'xlsx'])
    if uploaded_file is not None:
        st.session_state.file_uploaded = uploaded_file

    # Display the dataframe if a file is uploaded
    if 'file_uploaded' in st.session_state:
        file_uploaded = st.session_state.file_uploaded
        if file_uploaded.name.endswith('csv'):
            df = pd.read_csv(file_uploaded)
        else:
            df = pd.read_excel(file_uploaded)

        st.dataframe(df)

        # attachement
        attachment = st.file_uploader("Upload the Attachment (optional)", type=("pdf"))
        if attachment:
            attach_col1, attach_col2 = st.columns(2)
            with attach_col1:
                if st.button("Show Attachment"):
                    st.session_state['show_attachment'] = True
                    st.session_state['attachment_data'] = attachment.getvalue()
                    st.session_state['attachment_name'] = attachment.name
                    
                    if st.session_state['show_attachment'] == True:
                        pdf_viewer(input=st.session_state['attachment_data'], width=1920, height=1080)
                    
                    with attach_col2:       
                        if st.button("Hide Attachment"):
                            st.session_state['show_attachment'] = False

        # Allow users to select a predefined template or write their own
        template_option = st.selectbox("Select an Email Template", list(templates.PREDEFINED_TEMPLATES.keys()) + ["Custom"])

        if template_option and template_option != "Custom":
            subject_template = templates.PREDEFINED_TEMPLATES[template_option]["subject"]
            body_template = templates.PREDEFINED_TEMPLATES[template_option]["body"]
            st.text_input("Email Subject Template", value=subject_template, disabled=True)
            st.text_area("Email Body Template", value=body_template, disabled=True)
        else:
            subject_template = st.text_input("Custom Email Subject", placeholder="Email Subject Goes Here:")
            body_template = st.text_area("Custom Email Body", placeholder="Email Body Goes Here:")

        # Preview email
        if st.button('Preview Email'):
            if len(df) > 0:
                preview_row = df.iloc[0].to_dict()
                preview_row['user_name'] = user_name
                subject = Template(subject_template).substitute(preview_row)
                body = Template(body_template).substitute(preview_row)
                
                st.subheader('Email Preview')
                st.html(f'Subject: {subject}')
                st.html(f'Body:\n{body}')

        # Send emails
        if st.button('Send Emails'):
            st.session_state['email_sent'] = True
            with st.spinner('Sending emails...'):
                service = build('gmail', 'v1', credentials=st.session_state['creds'])
                for index, row in df.iterrows():
                    try:
                        row_dict = row.to_dict()
                        row_dict['user_name'] = user_name
                        # Replace placeholders with actual data
                        subject = Template(subject_template).substitute(row_dict)
                        body = Template(body_template).substitute(row_dict)

                        # Validate email address
                        try:
                            validate_email(row['recipient_email'])
                        except EmailNotValidError as e:
                            st.error(f"Invalid email address: {row['recipient_email']} - {e}")
                            email_sent_successfully = False
                            continue

                        # Create message
                        attachment_data = st.session_state.get('attachment_data', None)
                        attachment_name = st.session_state.get('attachment_name', None)
                        message = my_gmail.create_message(user_email, row['recipient_email'], subject, body, attachment_data, attachment_name if attachment else None)

                        # Send message
                        my_gmail.send_message(service, 'me', message)
                        
                        st.success(f"Email sent to {row['recipient_email']}")
                        email_sent_successfully = True
                    except Exception as e:
                        st.error(f"Failed to send email to {row['recipient_email']}. Error: {e}")
                        email_sent_successfully = False                    
                
                if email_sent_successfully == True:
                    st.success('All emails have been sent.')

                # Auto-refresh the app after a short delay without logging out
                utils.refresh_app(st, 3)
else:
    st.write(home_page_instructions, unsafe_allow_html=True)
    utils.download_sample_csv(st)