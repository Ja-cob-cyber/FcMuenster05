# ⚽ FC Münster 05 - 1. Mannschaft Verwaltung

Eine moderne Web-Anwendung zur Verwaltung der ersten Mannschaft des FC Münster 05, entwickelt mit Streamlit.

🔗 **Live-App:** [fcmuenster05herren.streamlit.app](https://fcmuenster05herren.streamlit.app/)

## 📋 Funktionen

### 🏠 Startseite
- Übersicht über die Mannschaft
- Aktuelle Informationen und News
- Schnellzugriff auf wichtige Bereiche

### 📦 Kistenliste
- Digitale Verwaltung der Bierkisten
- Übersicht über Spieler und ihre Kistenstände
- Einfache Aktualisierung und Tracking

### ⚠️ Strafenkatalog
- Dokumentation von Mannschaftsstrafen
- Transparente Übersicht über Strafzahlungen
- Regelwerk und Kategorien

## 🚀 Installation & Lokale Ausführung

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)

### Setup

1. Repository klonen:
```bash
git clone <repository-url>
cd fc-muenster-05
```

2. Virtuelle Umgebung erstellen (empfohlen):
```bash
python -m venv venv
source venv/bin/activate  # Unter Windows: venv\Scripts\activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Anwendung starten:
```bash
streamlit run app.py
```

Die App ist dann unter `http://localhost:8501` erreichbar.

## 📦 Abhängigkeiten

Die wichtigsten verwendeten Pakete:
- `streamlit` - Web-Framework
- `pandas` - Datenverarbeitung
- `openpyxl` - Excel-Datei-Unterstützung

Vollständige Liste in `requirements.txt`

## 🗂️ Projektstruktur

```
fc-muenster-05/
├── app.py                 # Hauptanwendung
├── modules/
│   ├── startseite.py     # Startseiten-Modul
│   ├── kistenliste.py    # Kistenlisten-Modul
│   └── strafen.py        # Strafen-Modul
├── data/                  # Datenspeicher
├── icon.png              # Vereins-Logo
├── requirements.txt      # Python-Abhängigkeiten
└── README.md             # Diese Datei
```

## 🔧 Konfiguration

Die App kann über `st.set_page_config()` angepasst werden:
- Layout (Standard: "wide")
- Seitentitel
- Favicon/Icon

## 💾 Datenverwaltung

Die Anwendung nutzt verschiedene Speichermethoden:
- Excel-Dateien für strukturierte Daten
- Session State für temporäre Daten
- Streamlit Secrets für sensible Konfiguration

## 🌐 Deployment

Die App ist auf Streamlit Community Cloud deployed:
1. Repository mit GitHub verbinden
2. App über Streamlit Cloud Dashboard deployen
3. Secrets und Umgebungsvariablen konfigurieren

## 👥 Für Entwickler

### Neue Module hinzufügen
1. Neues Python-Modul in `modules/` erstellen
2. `render()` Funktion implementieren
3. In `app.py` importieren und als Tab hinzufügen

### Stil anpassen
CSS kann über `st.markdown()` mit `unsafe_allow_html=True` eingebunden werden.

## 📝 Lizenz

Dieses Projekt ist für den internen Gebrauch des FC Münster 05 bestimmt.

## 🤝 Beitragen

Bei Fragen, Problemen oder Verbesserungsvorschlägen bitte ein Issue erstellen oder direkt kontaktieren.
