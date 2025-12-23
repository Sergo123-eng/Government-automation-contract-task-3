import streamlit as st
from generator import generate_proposal, export_proposal_to_docx

st.title("Proposal Draft Generator")

title = st.text_input("Proposal Title")
agency = st.text_input("Agency")

if st.button("Generate Proposal"):
    proposal = generate_proposal(title, agency)
    export_proposal_to_docx(proposal, "proposal.docx")
    st.success("Proposal generated")

    with open("proposal.docx", "rb") as file:
        st.download_button(
            label="Download Proposal",
            data=file,
            file_name="proposal.docx"
        )

