import streamlit as st

st.set_page_config("MailBlast - Privacy Policy", "static/logo.png")

#title
st.title("Privacy Policy")

# Privacy policy and terms of service
privacy_policy = '''

<p style='font-size:1.2rem;'><strong>MailBlast</strong> values your privacy and ensures that your data is handled securely. Here's how we manage your information:</p>

### **Data Collection**: 
1. We only access your email content, contact lists, and attachments temporarily during the email-sending process. 
2. None of this data is stored on our servers or shared with third parties.

### **Google OAuth 2.0**: 
1. We use Google’s OAuth 2.0 protocol to securely authenticate and access your Gmail account. 
2. Your credentials remain secure, and we do not store or have direct access to your login information.

### **Data Security**: 
1. All data transferred between MailBlast and Google’s servers is encrypted to ensure your information remains private and secure.

### **Data Deletion**: 
1. Since we do not store your data, there is no need for data deletion on our part. 
2. All emails, drafts, and attachments remain in your Google account, where you have full control.

### **Revocation of Access**: 
1. You can revoke MailBlast’s access to your Google account at any time through your Google account settings, immediately stopping the app from accessing your data.

### **Compliance**: 
1. MailBlast complies with Google’s API Services User Data Policy, ensuring that all data handling meets the highest privacy and security standards.
'''

st.write(privacy_policy, unsafe_allow_html=True)

# popup.show_modal(st)
# popup.render_modal(st, privacy_policy)