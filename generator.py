
import requests
from docx import Document
import requests
def generate_proposal(title, agency):
    return {
        "title": title,
        "agency": agency,
        "status": "Draft",
        "sections": {
            "Executive Summary": (
                f"We propose to support {agency} by delivering services "
                f"aligned with the solicitation titled '{title}'."
            ),
            "Scope of Work": (
                "Provide planning, execution, and reporting services "
                "in accordance with government requirements."
            ),
            "Technical Approach": (
                "Use a structured, compliant, and scalable approach "
                "to meet all contract objectives."
            ),
            "Compliance Statement": (
                "All applicable federal requirements and standards will be met."
            )
        }
    }

def export_proposal_to_docx(proposal, filename):
    doc = Document()
    doc.add_heading(proposal["title"], level=1)
    doc.add_paragraph(f"Agency: {proposal['agency']}")
    doc.add_paragraph(f"Status: {proposal['status']}")

    for section, content in proposal["sections"].items():
        doc.add_heading(section, level=2)
        doc.add_paragraph(content)

    doc.save(filename)

def select_template(agency):
    templates = {
        "Department of Defense": "dod_template.docx",
        "Department of Education": "education_template.docx"
    }
    return templates.get(agency, "default_template.docx")

def push_to_crm(proposal):
    payload = {
        "title": proposal["title"],
        "agency": proposal["agency"],
        "status": proposal["status"]
    }
    print("CRM payload ready:", payload)

def evaluate_bid(proposal):
    keywords = ["Defense", "Training", "Media"]
    score = sum(
        1 for word in keywords
        if word.lower() in proposal["title"].lower()
    )
    return "BID" if score >= 2 else "SKIP"

if __name__ == "__main__":
    proposal = generate_proposal(
        "Sports Media Training Services",
        "Department of Defense"
    )

    export_proposal_to_docx(proposal, "sports_media_proposal.docx")

    decision = evaluate_bid(proposal)
    push_to_crm(proposal)

    print("Bid decision:", decision)
    print("Proposal generated successfully.")
