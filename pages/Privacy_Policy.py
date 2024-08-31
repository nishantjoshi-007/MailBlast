import streamlit as st

st.set_page_config("MailBlast - Privacy Policy", "static/logo.png")

#title
st.title("Privacy Policy")

# Privacy policy and terms of service
privacy_policy = '''

<p style='font-size:1.2rem;'><strong>MailBlast</strong> values your privacy and is committed to ensuring that your data is handled securely and transparently. Below, we outline how we manage, use, and protect your information when you use our application.</p>

### **Data Collection and Usage**:
1. **User-Uploaded Data**: MailBlast allows users to upload CSV files containing email addresses and other relevant information necessary for the email-sending process. We only access this data temporarily to facilitate the email delivery.
2. **File Attachments**: Users can upload attachments directly through the app to be included in their emails. We do not access or store files from your Google Drive or any other storage service.
3. **No Data Storage**: All data from uploaded CSV files and attachments is processed in real-time and not stored on our servers. We use this data solely for the email-sending process.

### **Use of Google OAuth 2.0**:
1. **Secure Authentication**: We use Google’s OAuth 2.0 protocol to securely authenticate users and access their Gmail accounts for sending emails. Users control which permissions to grant, and MailBlast does not store or have direct access to user credentials.
2. **Purpose of Access**: The access provided is used strictly to send emails on the user’s behalf, and no other data from Google services is accessed or stored.

### **Data Security Measures**:
1. **Encryption**: All data transferred between MailBlast and Google servers is encrypted to ensure data privacy and security during transmission.
2. **Secure Session Handling**: Session data is managed securely, and temporary data is purged immediately after completing the email-sending process.

### **Data Retention and Deletion**:
1. **No Retention of Personal Data**: As MailBlast does not store any user data, there is no need for data deletion from our side. All emails, drafts, and attachments remain within your Google account, fully under your control.
2. **Control Over Data**: Users maintain full control over the data they upload and manage it through their Google account or directly within the app.

### **Revocation of Access**:
1. **User-Controlled Access**: Users can revoke MailBlast’s access to their Google account at any time through their Google account settings, immediately stopping any data flow between MailBlast and the user’s account.

### **Compliance and User Rights**:
1. **Compliance with Google’s Policies**: MailBlast fully complies with Google’s API Services User Data Policy. We adhere to all requirements for data privacy and security, ensuring the highest standards of user data protection.
2. **User Rights and Transparency**: We are committed to transparency in how we handle user data and are available to address any concerns or questions about our data practices.

By using MailBlast, you consent to this Privacy Policy and agree to the outlined practices for data handling, access, and security.
'''

st.write(privacy_policy, unsafe_allow_html=True)