import json

# Wähle welche Datei du sortieren willst
datei = "kader.json"  # oder "kader.json"

# Laden
with open(datei, "r", encoding="utf-8") as f:
    data = json.load(f)

# SORTIEREN - wähle eine Variante:

# Variante A: Nach Vergehen alphabetisch
# data_sorted = sorted(data, key=lambda x: x["Vergehen"])

# Variante B: Nach Strafe (niedrig -> hoch)
# data_sorted = sorted(data, key=lambda x: x["Strafe"])

# Variante C: Nach Nummer (für kader.json)
data_sorted = sorted(data, key=lambda x: x["nummer"])

# Speichern
with open(datei, "w", encoding="utf-8") as f:
    json.dump(data_sorted, f, indent=4, ensure_ascii=False)

print(f"✅ {datei} wurde sortiert!")
