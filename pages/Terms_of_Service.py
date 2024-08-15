import streamlit as st

st.set_page_config(page_title= "MailBlast - Terms of Service", page_icon="static/logo.png")

#title
st.title("Terms of Service")

# Privacy policy and terms of service
terms_of_service = '''

<p style='font-size:1.2rem;'><strong>MailBlast</strong> is designed to provide a simple and efficient way to send personalized mass emails using your Google account. By using MailBlast, you agree to the following terms:</p>

### **User Responsibility**: 
1. You are responsible for the content of the emails you send, including ensuring that all information is accurate and complies with applicable laws. 
2. MailBlast is not liable for any issues arising from incorrect or unlawful content.

### **Service Scope**: 
1. MailBlast enables you to send emails, manage drafts, and attach files using Google’s Gmail API. 
2. The service is dependent on Google’s API, and any changes or limitations imposed by Google may affect MailBlast's functionality.

### **Account Security**: 
1. MailBlast uses Google’s OAuth 2.0 for secure authentication, but you are responsible for maintaining the security of your Google account. 
2. We are not liable for any unauthorized access due to compromised user credentials.

### **Email Sending Limits**: 
1. Gmail imposes limits on the number of emails you can send per day. 
2. If you exceed these limits, your account may be temporarily or permanently suspended by Google. 
3. **MailBlast is not responsible for any account bans or suspensions due to excessive email sending.**

### **Limitation of Liability**: 
1. MailBlast is provided "as is" without any warranties, express or implied. 
2. We do not guarantee the continuous or error-free operation of the service. 
3. MailBlast is not liable for any indirect, incidental, or consequential damages arising from your use of the service.

### **Service Modifications**: 
1. We reserve the right to modify, suspend, or discontinue the service at any time, with or without notice. 
2. We may also update these terms as necessary, and continued use of the service signifies your acceptance of any changes.

### **Compliance with Laws**:
1. You agree to use MailBlast in compliance with all applicable laws and regulations, including those related to email marketing, data protection, and privacy.

### **Termination**: 
1. We reserve the right to terminate or restrict your access to MailBlast at our discretion, particularly if you violate these terms or misuse the service.

<p style='font-size:1.2rem;'>By using MailBlast, you acknowledge and accept these terms, including your responsibility for maintaining compliance with Gmail's email sending limits and securing your Google account.</p>
'''

st.write(terms_of_service, unsafe_allow_html=True)