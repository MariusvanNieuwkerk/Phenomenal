import streamlit as st


def render_automatic_flight():
    st.markdown("## Automatic Flight (AFCS)")
    st.caption("ATA 22 | Source: Phenom 300 POH (Section 6-03, Rev 12)")

    with st.expander("**1. Scope**", expanded=True):
        st.markdown(
            """
This section covers the Automatic Flight Control System (AFCS), including:
- AFCS control unit functions (mode selection)
- Lateral and vertical guidance modes
- Flight director and autopilot interaction
- Go-around and disconnect logic (conceptual)

This is treated as an aircraft system (Section 6-03). It is distinct from general avionics/communications.
"""
        )

    with st.expander("**2. Mode awareness (study approach)**", expanded=False):
        st.markdown(
            """
High-yield study method:
- Always know the **active lateral mode** and **active vertical mode** (FMA).
- Know what conditions cause **mode changes** (captures, limits, disconnect).
- Tie each mode to what the airplane will do next (turn/roll/track and climb/descent behavior).
"""
        )

    with st.expander("**3. Disconnects and protections (conceptual)**", expanded=False):
        st.markdown(
            """
Key concepts to understand:
- What triggers an autopilot **disconnect**
- How quick disconnect and CWS (control wheel steering) interact with AFCS logic
- How go-around mode changes lateral/vertical guidance

Use the POH/QRH for exact procedures and limitations.
"""
        )

