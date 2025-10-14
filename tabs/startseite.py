"""
Startseite Tab - Übersicht und Mannschaftskader
"""

import streamlit as st
from datetime import datetime
from utils.data_loader import (
    load_data,
    load_kader,
    load_strafenkatalog,
    load_strafen_excel,
    get_strafen_stats,
)


def render():
    """Rendert die Startseite mit Hintergrundbild, Kader und Infos"""

    # Versuche Hintergrundbild zu laden
    try:
        st.image("team_foto.jpg", use_container_width=True)
        st.markdown(
            """
            <div style="text-align: center; margin-top: -80px; position: relative; z-index: 10; background: rgba(0,0,0,0.6); padding: 40px; border-radius: 15px;">
                <h1 style="color: white; font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin: 0;">FC MÜNSTER 05</h1>
                <p style="color: white; font-size: 24px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin: 10px 0;">1. Mannschaft • Saison 2025/26</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    except:
        # Fallback ohne Bild
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); 
                        padding: 80px 20px; border-radius: 15px; text-align: center; color: white; margin-bottom: 30px;">
                <h1 style="font-size: 48px; margin: 0;">FC MÜNSTER 05</h1>
                <p style="font-size: 24px; opacity: 0.9; margin: 10px 0;">1. Mannschaft • Saison 2024/25</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick Stats laden
    df_kisten = load_data()

    if df_kisten is not None:
        total_kisten = len(df_kisten)
        offene_kisten = len(df_kisten[df_kisten["Bezahlt_Status"] == "Offen"])
        personen = df_kisten["Name"].nunique()
        bezahlt_kisten = len(df_kisten[df_kisten["Bezahlt_Status"] == "Bezahlt"])
    else:
        total_kisten = 0
        offene_kisten = 0
        personen = 0
        bezahlt_kisten = 0

    # Stats Kacheln

    st.markdown("### 📊 Schnellübersicht")

    # Strafen laden für Betrag
    df_strafen = load_strafen_excel()
    strafen_stats = get_strafen_stats(df_strafen)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="⚠️ Offene Kisten",
            value=offene_kisten,
            delta=None,
            delta_color="inverse",
        )

    with col2:
        st.metric(
            label="💰 Offene Strafen",
            value=f"{strafen_stats['betrag_offen']:.2f} €",
            delta=None,
            delta_color="inverse",
        )

    st.markdown("---")

    # Kader anzeigen
    st.markdown("### 👥 Mannschaftskader")

    df_kader = load_kader()

    if not df_kader.empty:
        st.dataframe(
            df_kader,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Name": st.column_config.TextColumn("Name", width="large"),
                "Position": st.column_config.TextColumn("Position", width="small"),
                "Trikotnummer": st.column_config.NumberColumn(
                    "Trikotnummer", width="small"
                ),
            },
        )
    else:
        st.warning("Mannschaftskader konnte nicht geladen werden.")

    st.markdown("---")

    # Strafenkatalog
    st.markdown("### ⚖️ Strafenkatalog")

    df_strafen = load_strafenkatalog()

    if not df_strafen.empty:
        st.dataframe(
            df_strafen,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Vergehen": st.column_config.TextColumn("Vergehen", width="large"),
                "Strafe": st.column_config.TextColumn("Strafe", width="small"),
            },
        )
    else:
        st.warning("Strafenkatalog konnte nicht geladen werden.")

    st.markdown("---")

    # Footer
    st.markdown(
        f'<p style="text-align: center; color: #6b7280; font-size: 14px;">💡 Diese Seite wird automatisch aktualisiert • Letzte Aktualisierung: {datetime.now().strftime("%d.%m.%Y %H:%M")}</p>',
        unsafe_allow_html=True,
    )
