"""
Kistenliste Dashboard - Streamlit App
Hauptdatei für FC Münster 05 Dashboard
"""

import streamlit as st
from datetime import datetime

# Import der Tab-Module
from tabs import startseite, kistenliste, strafenkatalog
from utils.data_loader import load_data

# Seitenkonfiguration
st.set_page_config(
    page_title="FC Münster 05",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS für besseres Design
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
    }
    .stMetric {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f2937;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    """Hauptfunktion der App"""
    # Header
    st.title("⚽ FC Münster 05 1. Mannschaft")
    st.markdown(
        '<p style="text-align: center; color: #6b7280; font-size: 18px;">Aktuelle Liste von offenen Bierkisten</p>',
        unsafe_allow_html=True,
    )

    # Timestamp
    st.markdown(
        f'<p style="text-align: center; color: #9ca3af; font-size: 12px;">Letzte Aktualisierung: {datetime.now().strftime("%d.%m.%Y %H:%M")}</p>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Tabs erstellen
    tab1, tab2, tab3 = st.tabs(["🏠 Startseite", "📦 Kistenliste", "⚠️ Strafenkatalog"])

    with tab1:
        startseite.render()

    with tab2:
        kistenliste.render()

    with tab3:
        strafenkatalog.render()


if __name__ == "__main__":
    main()
