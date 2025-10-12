# FC Münster 05 - Kistenliste Dashboard

Ein interaktives Streamlit Dashboard zur Verwaltung und Visualisierung der Bierkisten-Statistiken der 1. Mannschaft des FC Münster 05.

## 📁 Projektstruktur

```
.
├── app.py                      # Hauptdatei - Einstiegspunkt der App
├── requirements.txt            # Python-Abhängigkeiten
├── Kistenliste.xlsx           # Excel-Datendatei (nicht im Repo)
├── team_foto.jpg              # Teamfoto (optional)
│
├── utils/                     # Hilfsfunktionen
│   ├── __init__.py
│   ├── data_loader.py         # Datenladen und -verarbeitung
│   └── charts.py              # Diagramm-Funktionen
│
└── tabs/                      # Tab-Module
    ├── __init__.py
    ├── startseite.py          # Startseite mit Übersicht
    ├── kistenliste.py         # Detaillierte Statistiken
    └── strafenkatalog.py      # Strafenkatalog und Regeln
```

## 🚀 Installation

1. **Repository klonen oder Dateien herunterladen**

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Excel-Datei bereitstellen:**
   - Stelle sicher, dass `Kistenliste.xlsx` im Hauptverzeichnis liegt
   - Die Datei muss ein Sheet namens "Kistenliste" enthalten

4. **Optional: Teamfoto hinzufügen:**
   - Platziere `team_foto.jpg` im Hauptverzeichnis

## ▶️ App starten

```bash
streamlit run app.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📊 Features

### 🏠 Startseite
- Schnellübersicht mit wichtigsten Statistiken
- Mannschaftskader mit Status (bezahlt/offen)
- Regelübersicht
- Top 3 Hall of Fame

### 📦 Kistenliste
- Detaillierte Statistiken
- Offene Kisten pro Person
- Gestapeltes Balkendiagramm (Kisten pro Person)
- Bezahlstatus-Tortendiagramm
- Top 10 häufigste Gründe
- Vollständige Rangliste

### ⚠️ Strafenkatalog
- Übersicht aller Strafen
- Kisten-Strafen
- Spiel-Strafen
- Weitere Regeln

## 🔧 Anpassungen

### Neue Strafen hinzufügen
Bearbeite `tabs/strafenkatalog.py` und ergänze die Strafen im entsprechenden Abschnitt.

### Design anpassen
- CSS-Styles in `app.py` anpassen
- Farben in `utils/charts.py` ändern

### Neue Tabs hinzufügen
1. Neue Datei in `tabs/` erstellen (z.B. `tabs/neue_seite.py`)
2. `render()` Funktion implementieren
3. In `tabs/__init__.py` importieren
4. In `app.py` neuen Tab hinzufügen

## 📝 Excel-Datenformat

Die `Kistenliste.xlsx` sollte folgende Spalten enthalten:
- **Name**: Spielername
- **Bezahlt**: "J" für bezahlt, leer für offen
- **Grund**: Grund für die Kiste
- **Anmerkung**: Zusätzliche Informationen (für geteilte Kisten)

## 🌐 Deployment

### Streamlit Cloud
1. Repository auf GitHub pushen
2. Bei [Streamlit Cloud](https://streamlit.io/cloud) anmelden
3. App deployen und `app.py` als Hauptdatei angeben

### Render
1. Repository auf GitHub pushen
2. Bei [Render](https://render.com) anmelden
3. Web Service erstellen mit `streamlit run app.py`

## 👥 Entwickler

Erstellt für FC Münster 05 - 1. Mannschaft

## 📄 Lizenz

Privates Projekt für den FC Münster 05
