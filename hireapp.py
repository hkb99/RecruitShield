import streamlit as st
from hireagent import analyze

st.set_page_config(
    page_title = "RecruitShield",
    layout = "centered"
)

st.title = "Recruit Shield"
st.subheader("AI Recruitment Scam Detection Assistant")

st.divider()

with st.form("analysis"):

    message = st.text_area("Recruiter Message", placeholder = "Submit recruiter message:", height = 200, max_chars = 10000)

    email = st.text_input("Sender email address", placeholder = "recruiter@example.com", max_chars = 254)

    submitted_text = st.form_submit_button("Analyze Message", use_container_width = True)

if submitted_text:
    if not message.strip():
        st.warning("Enter a recruiter message.")

    else:
        try:
            with st.spinner("Investigating."):

                result = analyze(message, email.strip() or None)

            st.success("Analysis Complete")
            st.subheader("Security Analysis")
            st.markdown(result)

        except ValueError as err:
            st.error(str(err))
        except Exception:
            st.error("Analysis failed, try again later.")


st.divider()




