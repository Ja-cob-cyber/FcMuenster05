"""
Strafen Tab - Aktuelle Strafen aus Excel
"""

import streamlit as st
from utils.data_loader import (
    load_strafen_excel,
    calculate_strafen_per_person,
    get_strafen_stats,
)


def render():
    """Rendert den Strafen-Tab mit allen Statistiken"""

    # Daten laden
    df_strafen = load_strafen_excel()

    if df_strafen is None or df_strafen.empty:
        st.warning("Keine Strafen-Daten verfügbar.")
        st.stop()

    # Statistiken berechnen
    stats = get_strafen_stats(df_strafen)

    # Metriken anzeigen
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Gesamt Strafen", stats["gesamt"])
    with col2:
        st.metric("✅ Bezahlt", stats["bezahlt"], delta=None, delta_color="normal")
    with col3:
        st.metric("⚠️ Offen", stats["offen"], delta=None, delta_color="inverse")
    with col4:
        st.metric(
            "💰 Offener Betrag", f"{stats['betrag_offen']:.2f} €", delta_color="inverse"
        )

    st.markdown("---")

    # Offene Strafen pro Person
    st.subheader("⚠️ Offene Strafen pro Person")
    strafen_per_person = calculate_strafen_per_person(df_strafen)

    if not strafen_per_person.empty:
        st.dataframe(
            strafen_per_person,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Name": st.column_config.TextColumn("Name", width="large"),
                "Offener Betrag (€)": st.column_config.NumberColumn(
                    "Offener Betrag (€)", format="%.2f €", width="medium"
                ),
                "Anzahl Strafen": st.column_config.NumberColumn(
                    "Anzahl Strafen", width="small"
                ),
            },
        )
    else:
        st.success("🎉 Keine offenen Strafen!")

    st.markdown("---")

    # Filter für Detailansicht
    st.subheader("📋 Alle Strafen - Detailansicht")

    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        filter_person = st.selectbox(
            "Person filtern",
            ["Alle"] + sorted(df_strafen["Wer?"].dropna().unique().tolist()),
        )

    with col_filter2:
        filter_status = st.selectbox("Status filtern", ["Alle", "Offen", "Bezahlt"])

    # Filtern
    df_filtered = df_strafen.copy()

    if filter_person != "Alle":
        df_filtered = df_filtered[df_filtered["Wer?"] == filter_person]

    if filter_status != "Alle":
        df_filtered = df_filtered[df_filtered["Bezahlt_Status"] == filter_status]

    # Spalten für Anzeige auswählen
    display_columns = ["Termin", "Was?", "Wer?", "Betrag", "Bezahlt_Status"]
    df_display = df_filtered[display_columns].copy()

    # Datum formatieren
    df_display["Termin"] = df_display["Termin"].dt.strftime("%d.%m.%Y")

    st.dataframe(
        df_display,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Termin": st.column_config.TextColumn("Datum", width="small"),
            "Was?": st.column_config.TextColumn("Vergehen", width="large"),
            "Wer?": st.column_config.TextColumn("Person", width="medium"),
            "Betrag": st.column_config.NumberColumn(
                "Betrag", format="%.2f €", width="small"
            ),
            "Bezahlt_Status": st.column_config.TextColumn("Status", width="small"),
        },
    )

    st.caption(f"Angezeigt: {len(df_display)} von {len(df_strafen)} Strafen")

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #6b7280; font-size: 14px;">💡 Die Daten werden automatisch aus der Excel-Datei geladen</p>',
        unsafe_allow_html=True,
    )
