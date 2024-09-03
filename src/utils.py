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


def hide_labels(st):
    # Inject custom CSS to hide labels
    hide_labels_css = """
        <style>
        [data-testid="stWidgetLabel"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_labels_css, unsafe_allow_html=True)


# Function to add privacy-policy link to satisfy google console req
def policy_url_show(st):
    st.markdown(
        '<a href="https://mailblast.nishantjoshi.me/Privacy_Policy" style="display:none;">Privacy Policy</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://mailblast.nishantjoshi.me/Terms_of_Service" style="display:none;">Terms of Service</a>',
        unsafe_allow_html=True,
    )


# Function to refresh the app
def refresh_app(st, delay):
    st.write(f'<meta http-equiv="refresh" content="{delay}">', unsafe_allow_html=True)


# Function to download sample CSV
def download_sample_csv(st):

    # dict to path of sample csv
    sample_csv_dict = {
        "Event Invite": "./static/sample/event_invite_sample.csv",
        "Job Application": "./static/sample/job_application_sample.csv",
        "Product Launch": "./static/sample/product_launch_sample.csv",
        "Referral Request": "./static/sample/referral_request_sample.csv",
    }

    # radio button to select the template
    radio_select = st.sidebar.radio(
        "Select a Template for which you want to Download Sample",
        ["Event Invite", "Job Application", "Product Launch", "Referral Request"],
        index=None,
    )

    if radio_select:
        # open the file and read the content
        with open(sample_csv_dict[radio_select], "r") as file:
            sample_csv = file.read()

        # download button to download the sample csv
        st.sidebar.download_button(
            label="Download CSV",
            data=sample_csv,
            file_name=f'{radio_select.replace(" ","_").lower()}sample.csv',
            mime="text/csv",
        )


def success_box(st, success_message, survey_url=None):
    if survey_url:
        survey_link = f' <a href="{survey_url}" style="color: #155724; text-decoration: underline;" target="_self">Click here</a>'
    else:
        survey_link = ""

    st.markdown(
        f"""
        <div style="background-color: #d4edda; color: #155724; padding: 10px 20px; margin: 10px 0; border-color: #c3e6cb; border: 1px solid transparent; border-radius: 4px;">
            {success_message}{survey_link}
        </div>
        """,
        unsafe_allow_html=True,
    )


def attachement_file_type(st, attachment, pdf_viewer, index, pd):
    if attachment.name.lower().endswith(".pdf"):
        pdf_viewer(
            input=attachment.getvalue(),
            width=1920,
            height=1080,
            key=f"pdf_viewer_{index}",
        )
    elif attachment.name.lower().endswith((".csv", ".xls", ".xlsx")):
        if attachment.name.lower().endswith(".csv"):
            df_attachment = pd.read_csv(attachment)
        else:
            df_attachment = pd.read_excel(attachment)
        st.dataframe(df_attachment)
    elif attachment.name.lower().endswith((".png", ".jpg", ".jpeg")):
        st.image(attachment.getvalue())
    else:
        st.write(attachment.getvalue())
