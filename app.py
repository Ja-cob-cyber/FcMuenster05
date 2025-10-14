"""
Kistenliste Dashboard - Streamlit App
Hauptdatei für FC Münster 05 Dashboard
"""

import streamlit as st
from datetime import datetime

# Import der Tab-Module
from tabs import startseite, kistenliste, strafen
from utils.data_loader import load_data

# Seitenkonfiguration
st.set_page_config(
    page_title="FC Münster 05",
    page_icon="icon.png",
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
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        width: 100%;
    }
    .stTabs [data-baseweb="tab"] {
        flex-grow: 1;
        text-align: center;
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
    # Header mit Logo - zentriert
    col1, col_center, col3 = st.columns([1, 2, 1])
    with col_center:
        # Innere Spalten für Logo und Titel
        inner_col1, inner_col2 = st.columns([1, 3])
        with inner_col1:
            st.image("icon.png", width=80)
        with inner_col2:
            st.markdown(
                """
                <div style='padding-top: 15px;'>
                    <h2 style='margin: 0;'>FC Münster 05 1. Mannschaft</h2>
                </div>
            """,
                unsafe_allow_html=True,
            )
    # Link zur offiziellen Seite
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button(
            "Zur offiziellen Fussball.de Seite",
            "https://www.fussball.de/mannschaft/fc-muenster-05-fc-muenster-05-westfalen/-/saison/2526/team-id/011MI9N9Q4000000VTVG0001VTR8C1K7#!/",
            use_container_width=True,
        )

    st.markdown("---")

    # Tabs erstellen
    tab1, tab2, tab3 = st.tabs(["🏠 Startseite", "📦 Kistenliste", "⚠️ Strafenkatalog"])

    with tab1:
        startseite.render()

    with tab2:
        kistenliste.render()

    with tab3:
        strafen.render()


if __name__ == "__main__":
    main()
