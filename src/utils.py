import base64
import hashlib
import os
from datetime import datetime, timedelta

# Function to hide the warning
def hide_warning(st):
    # Inject custom CSS to hide the specific warning
    hide_warning_css = """
        <style>
        .stAlert[data-testid="stAlert"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_warning_css, unsafe_allow_html=True)

# Function to refresh the app
def refresh_app(st, delay):
    st.write(f'<meta http-equiv="refresh" content="{delay}">', unsafe_allow_html=True)

# Function to download sample CSV
def download_sample_csv(st):
    
    #dict to path of sample csv
    sample_csv_dict = {
    "Event Invite": "./static/sample/event_invite_sample.csv",
    "Job Application": "./static/sample/job_application_sample.csv",
    "Product Launch": "./static/sample/product_launch_sample.csv",
    "Referral Request": "./static/sample/referral_request_sample.csv"
    }

    #radio button to select the template
    radio_select = st.sidebar.radio("Select a Template for which you want to Download Sample", 
                     ["Event Invite", "Job Application", "Product Launch", "Referral Request"], index=None)
    
    if radio_select:
        #open the file and read the content
        with open(sample_csv_dict[radio_select], 'r') as file:
            sample_csv = file.read()
        
        #download button to download the sample csv
        st.sidebar.download_button(
            label="Download CSV",
            data=sample_csv,
            file_name=f'{radio_select.replace(" ","_").lower()}sample.csv',
            mime='text/csv'
        )
        
# Function to set a cookie
def set_cookie(st, key, value, expires_at):
    cookie_value = f"{value}|{expires_at.isoformat()}"
    encoded_value = base64.b64encode(cookie_value.encode()).decode()
    st.experimental_set_query_params(**{key: encoded_value})

# Function to get a cookie
def get_cookie(st, key):
    params = st.experimental_get_query_params()
    if key in params:
        encoded_value = params[key][0]
        decoded_value = base64.b64decode(encoded_value).decode()
        value, expires_at = decoded_value.split('|')
        expires_at = datetime.fromisoformat(expires_at)
        if expires_at > datetime.now():
            return value
    return None

# Function to delete a cookie
def delete_cookie(st, key):
    st.experimental_set_query_params(**{key: ""})
    
# Function to check session timeout
def check_session_timeout(st, SESSION_TIMEOUT):
    if datetime.now() - datetime.fromisoformat(st.session_state['last_activity']) > timedelta(seconds=SESSION_TIMEOUT):
        st.session_state.clear()
        delete_cookie(st, "creds")
        st.experimental_rerun()