import time, os

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
    time.sleep(delay)
    # st.write(f'<meta http-equiv="refresh" content="{time}">', unsafe_allow_html=True)
    keys_to_clear = ['file_uploaded', 'resume_data', 'resume_name', 'email_sent']
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

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
        
# Function to check session timeout
def check_session_timeout(st, SESSION_TIMEOUT):
    if time.time() - st.session_state['last_activity'] > SESSION_TIMEOUT:
        st.session_state.clear()
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
        st.experimental_rerun()