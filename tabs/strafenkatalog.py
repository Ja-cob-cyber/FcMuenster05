"""
Strafenkatalog Tab - Übersicht aller Strafen und Regeln
"""

import streamlit as st


def render():
    """Rendert den Strafenkatalog mit allen Regeln und Strafen"""
    
    st.header("⚠️ Strafenkatalog")
    
    st.markdown(
        """
        <ul>
            <li>1. Offene Kiste: 5€ Strafe</li>
            <li>2. Offene Kisten: 10€ Strafe</li>
            <li>3. Offene Kisten: 20€ Strafe</li>
            <li>4 oder mehr Offene Kisten: 50€ Strafe und Meldung an den Vorstand</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("---")
    
    st.markdown(
        '<p style="text-align: center; color: #6b7280; font-size: 14px;">💡 Bitte denkt daran, eure offenen Kisten zeitnah zu begleichen!</p>',
        unsafe_allow_html=True,
    )
