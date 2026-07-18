from doc_utils import create_docx
from styles import load_css
import streamlit as st

from constants import EMAIL_TYPES, TONES, EMAIL_LENGTH
from chains import email_chain

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="wide"
)
st.markdown(
    load_css(),
    unsafe_allow_html=True
)
# -------------------- Sidebar --------------------

with st.sidebar:

    st.title("📧 AI Email Generator")

    st.markdown("---")

    st.info(
        """
Generate professional emails using
LangChain + Groq LLM.
"""
    )

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- LangChain
- Groq
- Streamlit
- Prompt Engineering
- LCEL
""")

    st.markdown("---")

    st.caption("Version 1.0")

# -------------------- Title --------------------

st.title("📧 AI Email Generator")
st.markdown(
    "Generate professional emails instantly using **LangChain + Groq LLM**."
)

st.divider()

# -------------------- Layout --------------------

left_col, right_col = st.columns([1, 1])

with left_col:

    st.subheader("📝 Email Details")

    email_type = st.selectbox(
        "Email Type",
        EMAIL_TYPES
    )

    tone = st.selectbox(
        "Tone",
        TONES
    )

    email_length = st.selectbox(
        "Email Length",
        EMAIL_LENGTH
    )

    recipient_name = st.text_input(
        "Recipient Name"
    )

    recipient_designation = st.text_input(
        "Recipient Designation"
    )

    sender_name = st.text_input(
        "Your Name"
    )

    purpose = st.text_area(
        "Purpose",
        height=120
    )

    additional_details = ""

    # -------------------- Dynamic Fields --------------------

    if email_type == "Leave Request":

        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")

        reason = st.text_area("Reason for Leave")

        additional_details = f"""
Leave Duration:
{start_date} to {end_date}

Reason:
{reason}
"""

    elif email_type == "Meeting Request":

        meeting_date = st.date_input("Meeting Date")
        meeting_time = st.time_input("Meeting Time")

        agenda = st.text_area("Meeting Agenda")

        additional_details = f"""
Meeting Date:
{meeting_date}

Meeting Time:
{meeting_time}

Agenda:
{agenda}
"""

    elif email_type == "Job Application":

        company = st.text_input("Company Name")
        job_role = st.text_input("Job Role")

        additional_details = f"""
Company:
{company}

Position:
{job_role}
"""

    else:

        additional_details = st.text_area(
            "Additional Details",
            height=120
        )

    # -------------------- Generate Button --------------------

    generate_btn = st.button(
        "✨ Generate Email",
        use_container_width=True
    )

# -------------------- Right Column --------------------

with right_col:

    st.subheader("📨 Generated Email")

    if generate_btn:

        with st.spinner("Generating your email..."):

            try:

                if email_length == "Short":
                    email_length = "about 80-120 words"

                elif email_length == "Medium":
                    email_length = "about 150-220 words"

                else:
                    email_length = "about 250-350 words"

                result = email_chain.invoke({

                    "email_type": email_type,
                    "tone": tone,
                    "email_length": email_length,
                    "recipient_name": recipient_name,
                    "recipient_designation": recipient_designation,
                    "sender_name": sender_name,
                    "purpose": purpose,
                    "additional_details": additional_details

                })

                st.success("✅ Email Generated Successfully!")

                st.markdown("### 📄 Email Preview")

                st.text_area(
                    "Generated Email",
                    value=result,
                    height=400,
                    disabled=True
                )

                st.download_button(
                    label="📥 Download as TXT",
                    data=result,
                    file_name="generated_email.txt",
                    mime="text/plain",
                    use_container_width=True
                )

                docx_file = create_docx(result)

                st.download_button(
                    label="📄 Download as DOCX",
                    data=docx_file,
                    file_name="generated_email.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

            except Exception as e:

                st.error(f"Error: {e}")