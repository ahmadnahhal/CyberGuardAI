import streamlit as st

from app.services.report_service import (
    generate_report,
    get_reports,
)


def show():

    st.title("📄 Reports")

    st.write(
        "Generate, view and manage cybersecurity reports."
    )

    st.divider()

    st.subheader("Generate Report")

    report_input = st.text_area(
        "Describe the cybersecurity event",
        height=180,
        placeholder="Example: User received a phishing email requesting Microsoft credentials..."
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

            report = generate_report(report_input)

            st.success("Report generated successfully.")

            st.markdown(f"### {report['title']}")

            st.markdown(report["content"])

    st.divider()

    st.subheader("Saved Reports")

    reports = get_reports()

    if not reports:

        st.info("No reports have been generated yet.")

        return

    for report in reports:

        report_id, title, report_type, content, created_at = report

        with st.expander(
            f"{title} ({created_at})"
        ):

            st.write(f"**Type:** {report_type}")

            st.write(content)