from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def export_report_pdf(report: dict) -> bytes:

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(report["title"], styles["Heading1"])
    )

    elements.append(
        Paragraph(
            f"<b>Type:</b> {report['report_type']}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    for line in report["content"].splitlines():

        if line.strip():

            elements.append(
                Paragraph(
                    line,
                    styles["BodyText"],
                )
            )

    document.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf