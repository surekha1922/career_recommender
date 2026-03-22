from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(file, email, score, role, matched, missing):

    doc = SimpleDocTemplate(file)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("AI Resume Report", styles["Title"]),
        Paragraph(f"User: {email}", styles["Normal"]),
        Paragraph(f"Role: {role}", styles["Normal"]),
        Paragraph(f"Score: {score}", styles["Normal"]),
        Paragraph(f"Matched: {matched}", styles["Normal"]),
        Paragraph(f"Missing: {missing}", styles["Normal"])
    ]

    doc.build(content)