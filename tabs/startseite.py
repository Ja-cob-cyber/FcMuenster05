"""
Startseite Tab - Übersicht und Mannschaftskader
"""

import streamlit as st
from datetime import datetime
from utils.data_loader import load_data, load_kader, check_kader_consistency


def render():
    """Rendert die Startseite mit Hintergrundbild, Kader und Infos"""

    # Versuche Hintergrundbild zu laden
    try:
        st.image("team_foto.jpg", use_column_width=True)
        st.markdown(
            """
            <div style="text-align: center; margin-top: -80px; position: relative; z-index: 10; background: rgba(0,0,0,0.6); padding: 40px; border-radius: 15px;">
                <h1 style="color: white; font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin: 0;">⚽ FC MÜNSTER 05</h1>
                <p style="color: white; font-size: 24px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin: 10px 0;">1. Mannschaft • Saison 2024/25</p>
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
                <h1 style="font-size: 48px; margin: 0;">⚽ FC MÜNSTER 05</h1>
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
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="🍺 Gesamt Kisten", value=total_kisten, delta=None)

    with col2:
        st.metric(
            label="✅ Bezahlte Kisten",
            value=bezahlt_kisten,
            delta=None,
            delta_color="normal",
        )

    with col3:
        st.metric(
            label="⚠️ Offene Kisten",
            value=offene_kisten,
            delta=None,
            delta_color="inverse",
        )

    with col4:
        st.metric(label="👥 Spieler", value=personen, delta=None)

    st.markdown("---")

    # Kader anzeigen
    st.markdown("### 👥 Mannschaftskader")

    if df_kisten is not None:
        # Kader aus JSON laden
        kader_data = load_kader()

        # Konsistenz-Check
        if df_kisten is not None:
            check_kader_consistency(kader_data, df_kisten)

        st.info(f"📋 **{len(kader_data)} Personen** im Kader (inkl. Trainer)")

        cols = st.columns(4)
        for idx, spieler in enumerate(kader_data):
            with cols[idx % 4]:
                name = spieler["vollname"]
                nummer = spieler["nummer"]
                position = spieler.get("position", "")

                # Offene Kisten für diesen Spieler
                if df_kisten is not None:
                    offene = len(
                        df_kisten[
                            (df_kisten["Name"] == name)
                            & (df_kisten["Bezahlt_Status"] == "Offen")
                        ]
                    )
                else:
                    offene = 0

                # Anzeige
                if offene > 0:
                    st.markdown(f"⚠️ **#{nummer} {name}**")
                    st.caption(
                        f"{position} • {offene} Kiste{'n' if offene != 1 else ''} offen"
                    )
                else:
                    st.markdown(f"✅ **#{nummer} {name}**")
                    st.caption(f"{position}")

    st.markdown("---")

    # Strafenkatalog Regeln
    st.markdown("### ⚖️ Strafenkatalog & Regeln")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            """
        #### 🍺 Kisten-Strafen
        - **1 offene Kiste:** 5€
        - **2 offene Kisten:** 10€
        - **3 offene Kisten:** 20€
        - **4+ offene Kisten:** 50€ + Meldung an Vorstand
        """
        )

        st.markdown(
            """
        #### 📝 Weitere Regeln
        - Training schwänzen: **10€**
        - Zu spät zum Spiel: **15€**
        - Fehlende Ausrüstung: **5€**
        """
        )

    with col_right:
        st.markdown(
            """
        #### ⚽ Spiel-Strafen
        - **Gelbe Karte:** 10€
        - **Gelb-Rote Karte:** 20€
        - **Rote Karte:** 25€
        - **Platzverweis:** 50€
        """
        )

        st.markdown(
            """
        #### 🎯 Sonstiges
        - Nicht bei Mannschaftsfeier: **20€**
        - Handy im Training: **5€**
        - Vergessene Trikots waschen: **10€**
        """
        )

    st.markdown("---")

    # Top 3 Preview aus Kistenliste
    if df_kisten is not None and len(df_kisten) > 0:
        st.markdown("### 🏆 Hall of Fame (Top 3)")

        top_3 = df_kisten["Name"].value_counts().head(3)
        medals = ["🥇", "🥈", "🥉"]

        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]

        for idx, (name, count) in enumerate(top_3.items()):
            with cols[idx]:
                st.markdown(
                    f"""
                    <div style="background: white; padding: 20px; border-radius: 10px; 
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
                        <div style="font-size: 48px;">{medals[idx]}</div>
                        <div style="font-size: 20px; font-weight: bold; margin: 10px 0;">{name}</div>
                        <div style="font-size: 24px; color: #2563eb; font-weight: bold;">{count} Kisten</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

    st.markdown("---")

    # Call-to-Action Buttons
    st.markdown("### 🎯 Navigation")

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        st.info("📦 **Zur Kistenliste** → Wechsle oben zum Tab 'Kistenliste'")

    with col_btn2:
        st.info("⚠️ **Zum Strafenkatalog** → Wechsle oben zum Tab 'Strafenkatalog'")

    st.markdown("---")

    # Footer
    st.markdown(
        f'<p style="text-align: center; color: #6b7280; font-size: 14px;">💡 Diese Seite wird automatisch aktualisiert • Letzte Aktualisierung: {datetime.now().strftime("%d.%m.%Y %H:%M")}</p>',
        unsafe_allow_html=True,
    )
