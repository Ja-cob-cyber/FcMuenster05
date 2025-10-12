"""
Datenlade- und Verarbeitungsfunktionen
"""

import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    """
    Lädt die Excel-Datei Kistenliste.xlsx (Sheet: "Kistenliste").
    Bereinigt die Spalte "Name" und den Bezahlstatus ("Bezahlt").
    Erstellt eine neue Spalte Bezahlt_Status mit den Werten "Bezahlt" oder "Offen".
    Gibt das DataFrame zurück oder zeigt einen Fehler an.
    """
    try:
        df = pd.read_excel("Kistenliste.xlsx", sheet_name="Kistenliste")
        df["Name"] = df["Name"].str.strip()

        # Bezahlt-Status korrigieren
        df["Bezahlt"] = df["Bezahlt"].fillna("").str.strip()
        df["Bezahlt_Status"] = df["Bezahlt"].apply(
            lambda x: "Bezahlt" if x == "J" else "Offen"
        )

        return df
    except Exception as e:
        st.error(f"❌ Fehler beim Laden der Datei: {e}")
        return None


def create_open_boxes_table(df):
    """
    Erstellt Tabelle mit offenen Kisten pro Person:
    - Berücksichtigt "Geteilte Kisten" und teilt diese anteilig auf.
    - Gibt eine sortierte Tabelle mit Namen und Anzahl offener Kisten zurück.
    """
    # Nur offene Kisten
    open_df = df[df["Bezahlt_Status"] == "Offen"].copy()

    # Namen und deren Anzahl sammeln
    name_counts = {}

    for _, row in open_df.iterrows():
        name = str(row["Name"]).strip()

        # Prüfen ob "geteilte Kisten"
        if name.lower() == "geteilte kisten":
            # Namen aus Anmerkung auslesen
            anmerkung = str(row.get("Anmerkung", ""))
            if anmerkung and anmerkung != "nan":
                # Teile an Kommas
                shared_names = [n.strip() for n in anmerkung.split(",") if n.strip()]
                # Jeder bekommt anteilig 1/Anzahl
                fraction = 1.0 / len(shared_names) if shared_names else 0
                for shared_name in shared_names:
                    name_counts[shared_name] = (
                        name_counts.get(shared_name, 0) + fraction
                    )
        else:
            # Normaler Eintrag - volle Kiste
            name_counts[name] = name_counts.get(name, 0) + 1.0

    # In DataFrame umwandeln
    if name_counts:
        result = pd.DataFrame(
            list(name_counts.items()), columns=["Name", "Offene Kisten"]
        )
        result = result.sort_values("Offene Kisten", ascending=False)
        # Runden auf 2 Dezimalstellen
        result["Offene Kisten"] = result["Offene Kisten"].round(2)
        return result
    else:
        return pd.DataFrame({"Name": [], "Offene Kisten": []})


def create_ranking_table(df):
    """
    Erstellt eine Tabelle:
    Listet Personen nach Anzahl Kisten absteigend.
    Vergibt Medaillen-Emojis für die Top 3.
    Fügt Rangnummern hinzu.
    """
    ranking = df["Name"].value_counts().reset_index()
    ranking.columns = ["Name", "Anzahl Kisten"]
    ranking["Rang"] = range(1, len(ranking) + 1)

    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    ranking["Medaille"] = ranking["Rang"].map(lambda x: medals.get(x, ""))

    return ranking[["Rang", "Medaille", "Name", "Anzahl Kisten"]]
