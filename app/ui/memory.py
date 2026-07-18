import streamlit as st
from app.services.memory_service import (
    get_all_preferences,
    delete_preference,
    clear_preferences,
)

def show():

    st.title("🧠 Long-Term Memory")
    
    st.write(
    "CyberGuard AI stores long-term user preferences between conversations."
    )

    st.divider()

    if st.button(
     "🗑️ Clear All Memory",
     type="secondary",
    ):
     clear_preferences()
     st.success("Memory cleared.")
     st.rerun()

    memory = get_all_preferences()

    if not memory:

        st.info("No memories stored yet.")

        return

    for key, value in memory:

        col1, col2 = st.columns([5, 1])

        with col1:
         st.markdown(f"### {key.replace('_', ' ').title()}")
         st.write(value)

        with col2:

         if st.button(
          "🗑️",
          key=f"delete_{key}",
          help="Delete memory",
          ):
           delete_preference(key)
           st.rerun()

        st.divider()