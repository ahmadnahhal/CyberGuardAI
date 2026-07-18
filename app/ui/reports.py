import streamlit as st
from app.services.pdf_service import export_report_pdf
from app.services.report_service import get_report
from app.services.report_service import (
    generate_report,
    get_reports,
)


def show():

    st.title("📄 Reports")

    st.write(
        "Generate, review and manage cybersecurity reports."
    )

    st.divider()

    st.subheader("📝 Generate New Report")

    report_input = st.text_area(
        "Describe the cybersecurity event",
        height=180,
        placeholder=(
            "Example:\n"
            "A user received a phishing email requesting Microsoft credentials..."
        ),
    )

    if st.button(
        "Generate Report",
        use_container_width=True,
    ):

        if not report_input.strip():

            st.warning(
                "Please enter some information."
            )

        else:

            report = generate_report(
                report_input
            )

            st.success(
                "✅ Report generated successfully."
            )

            st.markdown(
                f"### {report['title']}"
            )

            st.markdown(
                report["content"]
            )

    st.divider()

    reports = get_reports()

    st.subheader(
        f"📚 Saved Reports ({len(reports)})"
    )

    if not reports:

        st.info(
            "No reports have been generated yet."
        )

        return

    for report in reports:

        report_id, title, report_type, content, created_at = report

        with st.expander(
            f"📄 Report #{report_id} • {title}"
        ):

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Report ID",
                    report_id,
                )

            with col2:
                st.metric(
                    "Type",
                    report_type,
                )

            st.caption(
                f"Created: {created_at}"
            )

            st.markdown("---")

            st.markdown(content)
            
            full_report = get_report(report_id)

            pdf = export_report_pdf(full_report)

            st.download_button(
                label="⬇ Export PDF",
                data=pdf,
                file_name=f"CyberGuard_Report_{report_id}.pdf",
                mime="application/pdf",
                use_container_width=True,
                key=f"pdf_{report_id}",
                )