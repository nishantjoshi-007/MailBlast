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
                <div style="background-color: rgba(0, 0, 0, 0.8); padding: 20px; border-radius: 10px; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1000; max-height: 70vh; overflow-y: auto;">
                <style>
                    h3 {
                        "color: green;"
                    }
                    p, span, div, ul, li {
                        "color: floralwhite;"
                    }
                </style>
                </div>
                    {content}
                """,
                unsafe_allow_html=True
            )