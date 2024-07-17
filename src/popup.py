# Function to show the modal
def show_modal(st):
    st.session_state['show_modal'] = True

# Function to hide the modal
def hide_modal(st):
    st.session_state['show_modal'] = False

# Function to render the modal with content
def render_modal(st, content):
    if 'show_modal' not in st.session_state:
        st.session_state['show_modal'] = False

    if st.session_state['show_modal']:
        with st.container():
            st.markdown(
                f"""
                <div style="background-color: rgba(0, 0, 0, 0.8); padding: 20px; border-radius: 10px; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1000;">
                    {content}
                    <button onclick="document.getElementById('close-btn').click()">Close</button>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Hidden Streamlit button to close the modal
        st.sidebar.button("Close Popup", key='close-btn', on_click=hide_modal)

        # Add a semi-transparent overlay when the modal is shown
        st.markdown(
            """
            <style>
            .overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5);
                z-index: 999;
            }
            </style>
            <div class="overlay"></div>
            """,
            unsafe_allow_html=True
        )