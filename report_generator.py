from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf_report(summary, events):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    path = "video_report.pdf"
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph("Video Summary", styles["Title"]))
    flowables.append(Paragraph(summary, styles["BodyText"]))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph("Detected Events", styles["Title"]))
    for event in events:
        flowables.append(Paragraph(str(event), styles["BodyText"]))
        flowables.append(Spacer(1, 6))

    doc.build(flowables)
    return path
