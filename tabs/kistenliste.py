"""
Kistenliste Tab - Detaillierte Statistiken und Diagramme
"""

import streamlit as st
from utils.data_loader import load_data, create_open_boxes_table, create_ranking_table
from utils.charts import create_person_chart, create_payment_chart, create_reasons_chart


def render():
    """Rendert die Kistenliste mit allen Statistiken und Diagrammen"""
    
    # Daten laden
    df = load_data()

    if df is None:
        st.stop()

    # Statistiken berechnen
    bezahlt_count = len(df[df["Bezahlt_Status"] == "Bezahlt"])
    offen_count = len(df[df["Bezahlt_Status"] == "Offen"])
    personen_count = df["Name"].nunique()

    # Metriken anzeigen
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Gesamt Einträge", len(df))
    with col2:
        st.metric("Bezahlt", bezahlt_count, delta=None, delta_color="normal")
    with col3:
        st.metric("Offen", offen_count, delta=None, delta_color="inverse")
    with col4:
        st.metric("Personen", personen_count)

    st.markdown("---")

    # Offene Kisten Tabelle
    st.subheader("⚠️ Offene Kisten")
    open_boxes = create_open_boxes_table(df)
    st.dataframe(
        open_boxes,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Name": st.column_config.TextColumn("Name", width="large"),
            "Offene Kisten": st.column_config.NumberColumn(
                "Offene Kisten", width="small"
            ),
        },
    )

    st.markdown("---")

    # Diagramme
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("🏆 Kisten pro Person")
        fig1 = create_person_chart(df)
        st.pyplot(fig1)

    with col_right:
        st.subheader("💰 Bezahlstatus")
        fig2 = create_payment_chart(df)
        st.pyplot(fig2)

    st.markdown("---")

    # Gründe
    st.subheader("📋 Top 10 Häufigste Gründe")
    fig3 = create_reasons_chart(df)
    st.pyplot(fig3)

    st.markdown("---")

    # Rangliste
    st.subheader("🏆 Rangliste")
    ranking = create_ranking_table(df)

    # Styling für Tabelle
    st.dataframe(
        ranking,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Rang": st.column_config.NumberColumn("Rang", width="small"),
            "Medaille": st.column_config.TextColumn("", width="small"),
            "Name": st.column_config.TextColumn("Name", width="medium"),
            "Anzahl Kisten": st.column_config.NumberColumn(
                "Anzahl Kisten", width="small"
            ),
        },
    )

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #6b7280; font-size: 14px;">💡 Die Seite aktualisiert sich automatisch bei Änderungen der Excel-Datei</p>',
        unsafe_allow_html=True,
    )
