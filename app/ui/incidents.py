import streamlit as st

from app.services.incident_service import (
    get_all_incidents,
)


def show():

    st.title("🚨 Incident History")

    st.write(
        "View all cybersecurity incidents recorded by CyberGuard AI."
    )

    st.divider()

    incidents = get_all_incidents()

    st.subheader(
        f"📋 Recorded Incidents ({len(incidents)})"
    )

    if not incidents:

        st.info(
            "No incidents have been recorded."
        )

        return

    for incident in incidents:

        (
            incident_id,
            title,
            description,
            severity,
            status,
            created_at,
        ) = incident

        with st.expander(
            f"🚨 Incident #{incident_id} • {title}"
        ):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Severity",
                    severity,
                )

            with col2:
                st.metric(
                    "Status",
                    status,
                )

            with col3:
                st.metric(
                    "Incident ID",
                    incident_id,
                )

            st.caption(
                f"Created: {created_at}"
            )

            st.markdown("---")

            st.markdown("### Description")

            st.write(description)