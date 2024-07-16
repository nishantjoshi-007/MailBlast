import os
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
import pickle, base64

# Allow OAuth over HTTP for local development
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Configuration
REDIRECT_URI = os.getenv('redirect_uris')
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/gmail.send', 'openid']

def save_credentials(creds):
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    st.session_state['creds'] = creds

def load_credentials():
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            return creds
    return None

def get_user_info(creds):
    try:
        service = build('oauth2', 'v2', credentials=creds)
        user_info = service.userinfo().get().execute()
        return user_info
    except HttpError as error:
        st.error(f'An error occurred: {error}')
        return None

def refresh_token_if_expired(creds):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        save_credentials(creds)
    return creds

def create_message(sender, to, subject, message_text, resume_data=None, resume_name=None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    if resume_data and resume_name:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(resume_data)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={resume_name}')
        message.attach(part)
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        return sent_message
    except HttpError as error:
        st.error(f'An error occurred: {error}')
        return None

def get_flow():
    return Flow.from_client_config(
        {
            "web": {
                "client_id": os.getenv('client_id'),
                "project_id": os.getenv('project_id'),
                "auth_uri": os.getenv('auth_uri'),
                "token_uri": os.getenv('token_uri'),
                "auth_provider_x509_cert_url": os.getenv('auth_provider_x509_cert_url'),
                "client_secret": os.getenv('client_secret'),
                "redirect_uris": [os.getenv('redirect_uris')],
                "javascript_origins": [os.getenv('javascript_origins')]
            }
        },
        scopes=SCOPES,
    )