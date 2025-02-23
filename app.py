import streamlit as st
from utils import extract_text_from_pdf, preprocess_text, extract_keywords

st.title("📄 Resume Keyword Extractor")
st.write("Upload your resume and paste a job description to extract matching keywords.")

# Resume Upload
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

# Job Description Input
job_desc = st.text_area("Paste the Job Description", height=200)

if uploaded_file and job_desc:
    with st.spinner("Processing..."):
        # Extract and preprocess text
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_text = preprocess_text(resume_text)
        job_desc = preprocess_text(job_desc)

        # Extract keywords
        keywords = extract_keywords(resume_text, job_desc)

        st.success("Top Matching Keywords Found:")
        st.write(", ".join(keywords))

st.markdown("🔍 *Tip: Include these keywords in your resume to improve job match!*")
