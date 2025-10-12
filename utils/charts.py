"""
Diagramm- und Visualisierungsfunktionen
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_person_chart(df):
    """
    Erstellt ein gestapeltes horizontales Balkendiagramm:
    Zeigt für jede Person die Anzahl bezahlter und offener Kisten.
    Sortiert nach Gesamtanzahl.
    Zeigt die Werte direkt an den Balken.
    """
    sns.set_style("whitegrid")

    # Daten vorbereiten
    name_bezahlt = df[df["Bezahlt_Status"] == "Bezahlt"].groupby("Name").size()
    name_offen = df[df["Bezahlt_Status"] == "Offen"].groupby("Name").size()

    all_names = df["Name"].value_counts().index
    name_stats = pd.DataFrame(
        {
            "Name": all_names,
            "Bezahlt": [name_bezahlt.get(name, 0) for name in all_names],
            "Offen": [name_offen.get(name, 0) for name in all_names],
        }
    )

    name_stats["Gesamt"] = name_stats["Bezahlt"] + name_stats["Offen"]
    name_stats = name_stats.sort_values("Gesamt", ascending=True)

    # Diagramm für Kisten pro Person
    # Dynamische Höhe basierend auf Anzahl der Namen
    n_people = len(name_stats)
    height = max(8, n_people * 0.4)  # Minimum 8, sonst 0.4 pro Person
    fig, ax = plt.subplots(figsize=(12, height))
    fig.patch.set_facecolor("white")
    y_pos = range(len(name_stats))

    ax.barh(
        y_pos,
        name_stats["Bezahlt"],
        color="#16a34a",
        label="Bezahlt",
        edgecolor="darkgreen",
        linewidth=1.5,
    )
    ax.barh(
        y_pos,
        name_stats["Offen"],
        left=name_stats["Bezahlt"],
        color="#dc2626",
        label="Offen",
        edgecolor="darkred",
        linewidth=1.5,
    )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(name_stats["Name"])
    ax.set_xlabel("Anzahl Kisten", fontweight="bold", fontsize=11)
    ax.set_ylabel("Name", fontweight="bold", fontsize=11)
    ax.legend(loc="lower right")
    ax.grid(axis="x", alpha=0.3)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Werte anzeigen
    for i, row in enumerate(name_stats.itertuples()):
        ax.text(
            row.Gesamt + 0.1,
            i,
            str(row.Gesamt),
            va="center",
            fontweight="bold",
            fontsize=10,
        )

    plt.tight_layout()
    return fig


def create_payment_chart(df):
    """
    Erstellt ein Tortendiagramm:
    Zeigt den Anteil "Bezahlt" vs. "Offen" für alle Einträge.
    """
    bezahlt_counts = df["Bezahlt_Status"].value_counts()

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor("white")

    colors_pie = ["#16a34a", "#dc2626"]
    explode = (0.05, 0.05)

    wedges, texts, autotexts = ax.pie(
        bezahlt_counts.values,
        labels=bezahlt_counts.index,
        autopct="%1.1f%%",
        colors=colors_pie,
        startangle=90,
        explode=explode,
        textprops={"fontsize": 11, "fontweight": "bold"},
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )

    plt.tight_layout()
    return fig


def create_reasons_chart(df):
    """
    Erstellt ein horizontales Balkendiagramm:
    Zeigt die Top 10 häufigsten Gründe aus der Spalte "Grund".
    Werte werden direkt angezeigt.
    """
    sns.set_style("whitegrid")

    grund_counts = df["Grund"].value_counts().head(10).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("white")

    n_bars = len(grund_counts)
    colors_green = [
        plt.cm.Greens(0.5 + 0.5 * i / max(n_bars - 1, 1)) for i in range(n_bars)
    ]

    grund_counts.plot(
        kind="barh", ax=ax, color=colors_green, edgecolor="darkgreen", linewidth=1.5
    )

    ax.set_xlabel("Anzahl", fontweight="bold", fontsize=11)
    ax.set_ylabel("Grund", fontweight="bold", fontsize=11)
    ax.grid(axis="x", alpha=0.3)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Werte anzeigen
    for i, v in enumerate(grund_counts.values):
        ax.text(v + 0.05, i, str(v), va="center", fontweight="bold", fontsize=10)

    plt.tight_layout()
    return fig
