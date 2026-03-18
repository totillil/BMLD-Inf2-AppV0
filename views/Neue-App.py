import streamlit as st
import pandas as pd

# =========================================================
# 0) APP SETTINGS  Hier sind Informationen über die Startseite des Spiels
# =========================================================

# =========================================================
# 1)  DESIGN (CSS)  Hier sind die Designs der App aufgeführt
# =========================================================
# =========================================================
# 1) DESIGN (CSS) - KORRIGIERT FÜR BESSERE LESBARKEIT
# =========================================================
st.markdown("""
<style>
/* --- App Hintergrund --- */
/* Wir setzen ein etwas kräftigeres Rosa, damit der Kontrast besser ist */
.stApp {
    background-color: #FFB3D1; /* Ein gesättigteres Rosa */
}

/* --- Globale Textfarben --- */
/* Wir zwingen alle h1 Titel und normalen Text auf eine dunkle Farbe */
h1, p, span, div {
    color: #4B0082 !important; /* Ein dunkles Indigo/Violett für besten Kontrast */
}

/* --- Standard Cards --- */
.cute-card {
    background-color: #FFE4F1;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}
.result-card {
    background-color: #E6F7FF;
    padding: 15px;
    border-radius: 20px;
    margin-bottom: 10px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}
.hint-card {
    background-color: #F3E8FF;
    padding: 12px 14px;
    border-radius: 18px;
    margin-bottom: 10px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}

/* --- Standard Buttons --- */
div.stButton > button {
    background-color: #FFD6E8;
    color: #4B0082 !important; /* Dunkler Text auf dem Button */
    border-radius: 22px;
    border: none;
    padding: 0.6em 1.1em;
    font-weight: 700;
}
div.stButton > button:hover {
    background-color: #4B0082; /* Dunkler Hintergrund beim Drüberfahren */
    color: white !important; /* Weißer Text beim Drüberfahren */
}

/* --- Sticky App Header --- */
.app-header {
    position: sticky;
    top: 0;
    z-index: 999;
    /* Hintergrund des Headers leicht transparent, aber dunkel genug */
    background: rgba(255, 179, 209, 0.95);
    backdrop-filter: blur(8px);
    padding: 10px 6px 12px 6px;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    margin-bottom: 10px;
}
.header-row {
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
}
.header-left {
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
}
.header-pill {
    background-color: #F3E8FF;
    border-radius: 999px;
    padding: 6px 12px;
    display: inline-block;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
    font-weight: 800;
    color: #4B0082 !important;
}
.header-score {
    background-color: #E6F7FF;
    border-radius: 999px;
    padding: 6px 12px;
    display: inline-block;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
    font-weight: 800;
    color: #4B0082 !important;
}
/* Spezifisches Styling für Buttons im Header */
.app-header div.stButton > button {
    background-color: #FFE4F1 !important;
    color: #4B0082 !important;
    border-radius: 999px !important;
    padding: 0.45em 1.0em !important;
    font-weight: 800 !important;
    border: none !important;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08) !important;
}
.app-header div.stButton > button:hover {
    background-color: #4B0082 !important;
    color: white !important;
}

/* --- Laborstationen im Lab-Screen --- */
.station-grid {
    display: grid;
    grid-template-columns: repeat(5, minmax(120px, 1fr));
    gap: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
}
.station-card {
    background: #FFE4F1;
    border-radius: 22px;
    padding: 12px 12px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.07);
    border: 1px solid rgba(0,0,0,0.04);
}
.station-title {
    font-weight: 900;
    font-size: 15px;
    margin-bottom: 6px;
    color: #4B0082 !important;
}
.station-sub {
    font-size: 12px;
    opacity: 0.7;
    margin-bottom: 10px;
    color: #4B0082 !important;
}
.station-badge {
    display: inline-block;
    background: #E6F7FF;
    padding: 3px 8px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    color: #4B0082 !important;
}

/* --- Cute Agar + Mikroskop Screens --- */
.screen-box {
    background-color: #FFF0F7;
    border-radius: 28px;
    padding: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}
.plate-card {
    background: #FFE4F1;
    border-radius: 999px;
    width: 180px;
    height: 180px;
    margin: 0 auto 12px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 0 0 8px rgba(255,255,255,0.4),
                0px 8px 18px rgba(0,0,0,0.08);
    font-size: 56px;
}
.plate-label {
    text-align: center;
    font-weight: 800;
    font-size: 18px;
    margin-bottom: 8px;
    color: #4B0082 !important;
}
.microscope-box {
    background: #E6F7FF;
    border-radius: 28px;
    padding: 24px;
    text-align: center;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.08);
    margin-bottom: 16px;
}
.gram-step-card {
    background: #F3E8FF;
    border-radius: 20px;
    padding: 16px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
    margin-bottom: 10px;
    min-height: 120px;
}
.gram-step-title {
    font-weight: 800;
    margin-bottom: 8px;
    color: #4B0082 !important;
}
.big-emoji {
    font-size: 44px;
    margin-bottom: 10px;
    display: block;
}
.path-card {
    background: #FFF7D6;
    border-radius: 18px;
    padding: 12px 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-top: 10px;
    margin-bottom: 14px;
    color: #4B0082 !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 2) SESSION STATE
# =========================================================
if "screen" not in st.session_state:
    st.session_state.screen = "home"

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "unlocked" not in st.session_state:
    st.session_state.unlocked = {
        "Mikroskop": False,
        "Agarplatte": False,
        "Blutprobe": False,
        "Blutbild": False,
        "Mikrotests": False
    }

# Welcher Fall ist gewählt
if "case" not in st.session_state:
    st.session_state.case = "Fall 1"

# Welche Platte ist auf dem Agar-Screen gewählt
if "selected_plate" not in st.session_state:
    st.session_state.selected_plate = None

# Gram-Spiel: Reihenfolge + Ergebnis
if "gram_steps" not in st.session_state:
    st.session_state.gram_steps = []

if "gram_result" not in st.session_state:
    st.session_state.gram_result = None

# Welcher Blutbild-Wert ist ausgewählt?
if "selected_blood_param" not in st.session_state:
    st.session_state.selected_blood_param = None

# =========================================================
# 3) FALLDATEN Hier sind alle Falldaten aufgeführt (Patientanakten)
# =========================================================
cases = {
    "Fall 1": {"Name": "Anna Müller", "Alter": 67, "Geschlecht": "weiblich", "Symptome": "Fieber, Schüttelfrost, Verwirrtheit"},
    "Fall 2": {"Name": "Lukas Meier", "Alter": 55, "Geschlecht": "männlich", "Symptome": "Brustschmerzen, Atemnot"},
    "Fall 3": {"Name": "Sara Keller", "Alter": 24, "Geschlecht": "weiblich", "Symptome": "Übelkeit, Bauchschmerzen"},
    "Fall 4": {"Name": "Tim Weber", "Alter": 34, "Geschlecht": "männlich", "Symptome": "Juckreiz, Bauchschmerzen nach Reise"},
    "Fall 5": {"Name": "Clara Huber", "Alter": 72, "Geschlecht": "weiblich", "Symptome": "Rötung um Katheterstelle"},
    "Fall 6": {"Name": "Noah Keller", "Alter": 41, "Geschlecht": "männlich", "Symptome": "Husten, Müdigkeit"},
}

# Mikroskopischer Test bei jedem Patient
lab_info = {
    "Fall 1": {"Mikroskop": "Diff-BB: Neutrophilie, Linksverschiebung möglich.",
               "Agarplatte": "Wachstum auf Kulturmedien erwartet.",
               "Blutprobe": "Entzündungszeichen passend zu bakterieller Infektion."},
    "Fall 2": {"Mikroskop": "Kettenbild passend zu grampositiven Kokken möglich.",
               "Agarplatte": "β-Hämolyse wäre ein wichtiger Hinweis.",
               "Blutprobe": "Entzündungszeichen passend zu Infektion."},
    "Fall 3": {"Mikroskop": "Stäbchen wären passend.",
               "Agarplatte": "MAC wäre besonders spannend.",
               "Blutprobe": "Leichte Entzündungszeichen möglich."},
    "Fall 4": {"Mikroskop": "Grampositive Kokken in Haufen möglich.",
               "Agarplatte": "Wachstum möglich, aber weniger aggressiv.",
               "Blutprobe": "CRP eher wenig erhöht."},
    "Fall 5": {"Mikroskop": "Kein typisches Bakterienbild im Fokus.",
               "Agarplatte": "Standardplatten wenig hilfreich.",
               "Blutprobe": "Eosinophilie wäre ein zentraler Hinweis."},
    "Fall 6": {"Mikroskop": "Sprosszellen oder Hyphen möglich.",
               "Agarplatte": "Pilzwachstum könnte sichtbar sein.",
               "Blutprobe": "Unspezifische Entzündungszeichen."},
}
# Agar-Ergebnisse pro Fall (COS / MAC / CNA)
micro_tests = {
    "Fall 1": {"Gram": "Gram-positiv, Kokken in Haufen", "Katalase": "positiv", "Koagulase": "positiv", "Hämolyse": "β-Hämolyse möglich"},
    "Fall 2": {"Gram": "Gram-positiv, Kokken in Ketten", "Katalase": "negativ", "Koagulase": "nicht sinnvoll", "Hämolyse": "β-Hämolyse"},
    "Fall 3": {"Gram": "Gram-negativ, Stäbchen", "Katalase": "nicht zentral", "Koagulase": "nicht sinnvoll", "Hämolyse": "nicht zentral"},
    "Fall 4": {"Gram": "Gram-positiv, Kokken in Haufen", "Katalase": "positiv", "Koagulase": "negativ", "Hämolyse": "meist keine (γ)"},
    "Fall 5": {"Gram": "Nicht sinnvoll", "Katalase": "nicht sinnvoll", "Koagulase": "nicht sinnvoll", "Hämolyse": "nicht sinnvoll"},
    "Fall 6": {"Gram": "Nicht typisch / Pilzverdacht", "Katalase": "nicht primär", "Koagulase": "nicht primär", "Hämolyse": "nicht typisch"},
}
# Referenzwerte f¨r Blutprobe zur Interpretation
REF = {
    "CRP (mg/L)": (0, 5),
    "PCT (ng/mL)": (0, 0.05),
    "Leukos (G/L)": (4, 10),
    "Troponin (ng/L)": (0, 14),
    "Glukose (mmol/L)": (3.9, 5.6),
    "pH (BGA)": (7.35, 7.45),
    "Laktat (mmol/L)": (0.5, 2.0),
}
# Referenzwerte Differentialblutbild
REF_BLOOD_DIFF = {
    "Leukozyten (G/L)": (4, 10),
    "Neutrophile (%)": (40, 75),
    "Lymphozyten (%)": (20, 45),
    "Eosinophile (%)": (0, 6)
}
# Werte für die Blurprobenscreening
blood_values = {
    "Fall 1": {"CRP (mg/L)": 180, "PCT (ng/mL)": 8.5, "Leukos (G/L)": 18, "Laktat (mmol/L)": 4.2, "pH (BGA)": 7.28},
    "Fall 2": {"CRP (mg/L)": 95, "Leukos (G/L)": 14},
    "Fall 3": {"CRP (mg/L)": 35, "Leukos (G/L)": 12},
    "Fall 4": {"CRP (mg/L)": 8, "Leukos (G/L)": 8},
    "Fall 5": {"CRP (mg/L)": 4, "Leukos (G/L)": 9},
    "Fall 6": {"CRP (mg/L)": 20, "Leukos (G/L)": 10},
}
# Werte für das Weisse blutbild
blood_diff = {
    "Fall 1": {"Leukozyten (G/L)": 14, "Neutrophile (%)": 82, "Lymphozyten (%)": 12, "Eosinophile (%)": 1},
    "Fall 2": {"Leukozyten (G/L)": 13, "Neutrophile (%)": 78, "Lymphozyten (%)": 15, "Eosinophile (%)": 1},
    "Fall 3": {"Leukozyten (G/L)": 12, "Neutrophile (%)": 74, "Lymphozyten (%)": 18, "Eosinophile (%)": 1},
    "Fall 4": {"Leukozyten (G/L)": 8, "Neutrophile (%)": 60, "Lymphozyten (%)": 30, "Eosinophile (%)": 2},
    "Fall 5": {"Leukozyten (G/L)": 9, "Neutrophile (%)": 45, "Lymphozyten (%)": 25, "Eosinophile (%)": 18},
    "Fall 6": {"Leukozyten (G/L)": 10, "Neutrophile (%)": 55, "Lymphozyten (%)": 30, "Eosinophile (%)": 6},
}
# Erklärungstexte für Blutbild-Werte als Hilfestellung
blood_explanations = {
    "Leukozyten (G/L)": "Leukozyten sind weisse Blutkörperchen. Erhöhte Werte sprechen oft für eine Entzündung oder Infektion.",
    "Neutrophile (%)": "Neutrophile sind oft bei bakteriellen Infektionen erhöht.",
    "Lymphozyten (%)": "Lymphozyten sind häufig bei viralen Infektionen erhöht.",
    "Eosinophile (%)": "Eosinophile können bei Parasiten oder allergischen Reaktionen erhöht sein."
}

# Agar-Ergebnisse pro Fall (COS / MAC / CNA)
agar_results = {
    "Fall 1": {
        "COS": "Wachstum vorhanden, helle Kolonien, Hämolyse sichtbar.",
        "MAC": "Kein Wachstum.",
        "CNA": "Deutliches Wachstum."
    },
    "Fall 2": {
        "COS": "Deutliches Wachstum mit β-Hämolyse.",
        "MAC": "Kein Wachstum.",
        "CNA": "Wachstum vorhanden."
    },
    "Fall 3": {
        "COS": "Wachstum vorhanden.",
        "MAC": "Wachstum vorhanden.",
        "CNA": "Kein Wachstum."
    },
    "Fall 4": {
        "COS": "Wachstum vorhanden, keine Hämolyse.",
        "MAC": "Kein Wachstum.",
        "CNA": "Wachstum vorhanden."
    },
    "Fall 5": {
        "COS": "Kein relevantes Wachstum.",
        "MAC": "Kein relevantes Wachstum.",
        "CNA": "Kein relevantes Wachstum."
    },
    "Fall 6": {
        "COS": "Mögliches atypisches Wachstum.",
        "MAC": "Kaum relevant.",
        "CNA": "Kaum relevant."
    }
}

# Mikroskopischer Eindruck + Gram-Ziel pro Fall
microscope_info = {
    "Fall 1": {"view": "Kokken in Haufen sichtbar.", "gram_type": "Gram-positiv"},
    "Fall 2": {"view": "Kokken in Ketten sichtbar.", "gram_type": "Gram-positiv"},
    "Fall 3": {"view": "Stäbchen sichtbar.", "gram_type": "Gram-negativ"},
    "Fall 4": {"view": "Kokken in Haufen sichtbar.", "gram_type": "Gram-positiv"},
    "Fall 5": {"view": "Kein typisches Bakterienbild, evtl. parasitärer Hinweis.", "gram_type": "Nicht sinnvoll"},
    "Fall 6": {"view": "Sprosszellen / Hyphen sichtbar.", "gram_type": "Nicht sinnvoll"},
}
# Die Lösungen alles Fälle
solutions = {
    "Fall 1": "Staphylococcus aureus",
    "Fall 2": "Streptococcus pyogenes",
    "Fall 3": "Escherichia coli",
    "Fall 4": "Staphylococcus epidermidis",
    "Fall 5": "Helmintheninfektion",
    "Fall 6": "Candida spp.",
}
# Hier sind die Diagnoseoptionen, die in der Auswahlbox angezeigt werden. Sie sollten alle möglichen Diagnosen enthalten, damit die Spieler eine Auswahl treffen können. Einige Fälle sind als Verwirrung hier
DIAG_CHOICES = [
    "Staphylococcus aureus",
    "Staphylococcus epidermidis",
    "Streptococcus pyogenes",
    "Escherichia coli",
    "Klebsiella pneumoniae",
    "Pseudomonas aeruginosa",
    "Candida spp.",
    "Virale Infektion (z.B. Influenza)",
    "EBV / Mononukleose",
    "Allergische Reaktion / Hypersensitivität",
    "Helmintheninfektion",
    "Giardiasis (Protozoen)",
    "Akutes Koronarsyndrom",
    "Pneumonie (bakteriell)",
    "Pneumonie (viral)",
    "Diabetische Ketoazidose",
    "Gastroenteritis (bakteriell)",
    "Gastroenteritis (viral)",
    "Unklar",
]

# =========================================================
# 4) HELPER FUNCTIONS, z.Bsp. für die Interpretation von Blutwerten oder Mikrotests
# =========================================================
def flag(value, low, high):
    if value < low:
        return "↓"
    if value > high:
        return "↑"
    return "✓"

def interpret_blood(diff: dict) -> list[str]:
    hints = []
    neut = float(diff.get("Neutrophile (%)", 0))
    lymph = float(diff.get("Lymphozyten (%)", 0))
    eos = float(diff.get("Eosinophile (%)", 0))

    if neut >= 70:
        hints.append("🧠 Neutrophile ↑ → spricht eher für **bakterielle** Ursache (akut).")
    if lymph >= 45:
        hints.append("🧠 Lymphozyten ↑ → spricht eher für **virale** Ursache.")
    if eos >= 6:
        hints.append("🧠 Eosinophile ↑ → spricht für **Parasiten** oder **Allergie/Überempfindlichkeit**.")
    if not hints:
        hints.append("🧠 Differentialblutbild: kein klarer Hinweis → Kontext/weitere Tests wichtig.")
    return hints

def interpret_micro(mt: dict) -> list[str]:
    hints = []
    gram = mt.get("Gram", "").lower()
    kat = mt.get("Katalase", "").lower()
    koa = mt.get("Koagulase", "").lower()

    if "gram-positiv" in gram and "kokken" in gram and "haufen" in gram and "positiv" in kat:
        hints.append("🧠 Gram+ Kokken in Haufen + Katalase+ → **Staphylokokken**.")
        if "positiv" in koa:
            hints.append("🧠 Koagulase+ → Hinweis auf **Staphylococcus aureus**.")
        elif "negativ" in koa:
            hints.append("🧠 Koagulase− → eher **Staphylococcus epidermidis**.")

    if "ketten" in gram and "negativ" in kat:
        hints.append("🧠 Gram+ Kokken in Ketten + Katalase− → Hinweis auf **Streptokokken**.")

    if not hints:
        hints.append("🧠 Mikrotests: kein eindeutiger Shortcut → Kultur/weitere Schritte beachten.")
    return hints

def reset_gram_game():
    st.session_state.gram_steps = []
    st.session_state.gram_result = None

# =========================================================
# 5) SCREENS  Hier wird definiert, was auf den verschiedenen Screens angezeigt wird (Home, Level-Auswahl, Labor, etc.)
# =========================================================

# -------------------------
# HOME SCREEN 
# -------------------------
if st.session_state.screen == "home":
    st.title("🧪 Lab Diagnose Game 🎀")
    st.write("Willkommen im biomedizinischen Labor!")

    st.markdown(f"""
    <div class="hint-card">
    🎯 <b>Score:</b> {st.session_state.score}
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start", key="start_home"):
        st.session_state.screen = "level"
        st.rerun()

# -------------------------
# LEVEL SCREEN, Hier sollte die Aufführung alles Fälle sein, damit die Spieler einen Fall auswählen können. Es sollte auch der aktuelle Score angezeigt werden.
# -------------------------
elif st.session_state.screen == "level":
    st.title("Fall auswählen")

    st.markdown(f"""
    <div class="hint-card">
    🎯 <b>Score:</b> {st.session_state.score}
    </div>
    """, unsafe_allow_html=True)

    order = ["Fall 1", "Fall 2", "Fall 3", "Fall 4", "Fall 5", "Fall 6"]
    cols = st.columns(3)

    for i, f in enumerate(order):
        with cols[i % 3]:
            if st.button(f, key=f"btn_{f}"):
                st.session_state.case = f
                st.session_state.screen = "lab"
                st.session_state.feedback = None
                st.session_state.selected_plate = None
                reset_gram_game()
                st.rerun()

    if st.button("🔙 Zurück", key="back_level"):
        st.session_state.screen = "home"
        st.rerun()

# -------------------------
# LAB SCREEN zur Fallbearbeitung, hier sollten die Patientendaten, die Auswahl der Laborstationen und die Diagnoseoptionen angezeigt werden. Je nachdem, welche Laborstationen freigeschaltet wurden, sollten die entsprechenden Ergebnisse/Hinweise angezeigt werden. Es sollte auch die Möglichkeit geben, zur Level-Auswahl zurückzukehren.
# -------------------------
elif st.session_state.screen == "lab":
    case = st.session_state.case
    data = cases[case]

    # reset unlocked + feedback bei Fallwechsel
    if "last_case" not in st.session_state or st.session_state.last_case != case:
        st.session_state.unlocked = {k: False for k in st.session_state.unlocked}
        st.session_state.last_case = case
        st.session_state.feedback = None
        st.session_state.selected_plate = None
        reset_gram_game()

    # Sticky Header mit Fallname und Score + Zurück-Button
    st.markdown('<div class="app-header">', unsafe_allow_html=True)
    st.markdown('<div class="header-row"><div class="header-left">', unsafe_allow_html=True)

    if st.button("← Zurück", key=f"header_back_{case}"):
        st.session_state.screen = "level"
        st.rerun()
        # damit die Spieler jederzeit zurück zur Fallauswahl können (und damit die Seite nicht überladen ist, habe ich den Zurück-Button in den Header gepackt)
    st.markdown(f'<div class="header-pill">🧪 {case}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="header-score">🎯 Score: {st.session_state.score}</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    left, right = st.columns([1.1, 1])

    # ---------- LEFT ---------- der linke Bereich zeigt die Patientendaten, die Diagnoseoptionen und das Feedback an, während der rechte Bereich die Laborstationen und die Ergebnisse/Hinweise anzeigt. Je nachdem, welche Stationen freigeschaltet wurden, werden dort unterschiedliche Informationen angezeigt.
    with left:
        st.markdown(f"""
        <div class="cute-card">
        <h4>📄 Patientenakte</h4>
        <b>Name:</b> {data["Name"]}<br>
        <b>Alter:</b> {data["Alter"]}<br>
        <b>Geschlecht:</b> {data["Geschlecht"]}<br>
        <b>Symptome:</b> {data["Symptome"]}
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🧠 Diagnose (bitte wählen)")
        diag_options = ["— bitte wählen —"] + DIAG_CHOICES

        with st.form(key=f"diag_form_{case}", clear_on_submit=False):
            diagnosis = st.selectbox(
                "Was ist am wahrscheinlichsten?",
                diag_options,
                index=0,
                key=f"diag_{case}"
            )
            submitted = st.form_submit_button("✅ Diagnose abgeben")

        if submitted:
            if diagnosis == "— bitte wählen —":
                st.session_state.feedback = {"type": "warning", "msg": "Bitte zuerst eine Diagnose auswählen 🙂"}
            else:
                if diagnosis == solutions[case]:
                    st.session_state.score += 10
                    st.session_state.feedback = {"type": "success", "msg": "✅ Richtig! +10 Punkte"}
                else:
                    st.session_state.score -= 5
                    st.session_state.feedback = {
                        "type": "error",
                        "msg": f"❌ Falsch. Richtige Lösung: {solutions[case]} (-5 Punkte)"
                    }
            st.rerun()

        fb = st.session_state.get("feedback")
        if fb:
            if fb["type"] == "success":
                st.success(fb["msg"])
            elif fb["type"] == "error":
                st.error(fb["msg"])
            else:
                st.warning(fb["msg"])

    # ---------- RIGHT ---------- hier werden die Laborstationen angezeigt, die die Spieler freischalten können, um mehr Informationen über den Fall zu erhalten. Je nachdem, welche Stationen freigeschaltet wurden, werden dort unterschiedliche Informationen angezeigt. Es gibt auch einen Bereich für Ergebnisse/Hinweise, der sich dynamisch anpasst.
    with right:
        st.subheader("🔬 Laborstationen")
        st.write("Tippe, um Stationen freizuschalten:")

        cols = st.columns(5)
# hier werden die Stationen als Karten dargestellt, die den Namen der Station, eine kurze Beschreibung und einen Status (unlocked/locked) anzeigen. Wenn die Spieler auf "Öffnen" klicken, wird die entsprechende Station freigeschaltet und die Seite aktualisiert, um die neuen Informationen anzuzeigen.
        with cols[0]:
            st.markdown(f"""
            <div class="station-card">
                <div class="station-title">🔬 Mikroskop</div>
                <div class="station-sub">Gram / Morphologie</div>
                <div class="station-badge">{'✅ unlocked' if st.session_state.unlocked['Mikroskop'] else '🔒 locked'}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Öffnen", key=f"open_mic_{case}"):
                st.session_state.unlocked["Mikroskop"] = True
                st.session_state.screen = "mikroskop"
                reset_gram_game()
                st.rerun()
# die Agarstation könnte z.Bsp. so aussehen, dass die Spieler zwischen den verschiedenen Platten (COS / MAC / CNA) wechseln können, um die Ergebnisse zu sehen. Je nachdem, welche Platte sie auswählen, werden unterschiedliche Informationen angezeigt, die ihnen bei der Diagnose helfen können. Das könnte
        with cols[1]:
            st.markdown(f"""
            <div class="station-card">
                <div class="station-title">🧫 Agar</div>
                <div class="station-sub">COS / MAC / CNA</div>
                <div class="station-badge">{'✅ unlocked' if st.session_state.unlocked['Agarplatte'] else '🔒 locked'}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Öffnen", key=f"open_agar_{case}"):
                st.session_state.unlocked["Agarplatte"] = True
                st.session_state.screen = "agar"
                st.session_state.selected_plate = None
                st.rerun()

        with cols[2]:
            st.markdown(f"""
            <div class="station-card">
                <div class="station-title">🧪 Blutprobe</div>
                <div class="station-sub">CRP / PCT / etc.</div>
                <div class="station-badge">{'✅ unlocked' if st.session_state.unlocked['Blutprobe'] else '🔒 locked'}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Öffnen", key=f"open_blood_{case}"):
                st.session_state.unlocked["Blutprobe"] = True
                st.rerun()

        with cols[3]:
            st.markdown(f"""
            <div class="station-card">
                <div class="station-title">🩸 Blutbild</div>
                <div class="station-sub">Diff-BB</div>
                <div class="station-badge">{'✅ unlocked' if st.session_state.unlocked['Blutbild'] else '🔒 locked'}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Öffnen", key=f"open_bb_{case}"):
                st.session_state.unlocked["Blutbild"] = True
                st.session_state.screen = "blutbild"
                st.session_state.selected_blood_param = None
                st.rerun()

        with cols[4]:
            st.markdown(f"""
            <div class="station-card">
                <div class="station-title">🧬 Mikrotests</div>
                <div class="station-sub">Katalase / Koagulase</div>
                <div class="station-badge">{'✅ unlocked' if st.session_state.unlocked['Mikrotests'] else '🔒 locked'}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Öffnen", key=f"open_mt_{case}"):
                st.session_state.unlocked["Mikrotests"] = True
                st.rerun()

        st.write("---")
        st.subheader("📌 Ergebnisse / Hinweise")

        if not any(st.session_state.unlocked.values()):
            st.markdown("""
            <div class="hint-card">
            Noch keine Station gewählt. Tippe auf eine Station oben.
            </div>
            """, unsafe_allow_html=True)

        if st.session_state.unlocked["Mikroskop"]:
            st.markdown(f"""<div class="result-card">🔬 {lab_info[case]["Mikroskop"]}</div>""", unsafe_allow_html=True)

        if st.session_state.unlocked["Agarplatte"]:
            st.markdown(f"""<div class="result-card">🧫 {lab_info[case]["Agarplatte"]}</div>""", unsafe_allow_html=True)

        if st.session_state.unlocked["Blutprobe"]:
            st.markdown(f"""<div class="result-card"><b>🧪 Blutprobe – Laborbefund</b><br>{lab_info[case]["Blutprobe"]}</div>""",
                        unsafe_allow_html=True)
            values = blood_values[case]
            for param, val in values.items():
                if param in REF:
                    low, high = REF[param]
                    f = flag(val, low, high)
                    st.markdown(f"""<div class="result-card">{param}: <b>{val}</b> (Ref: {low}–{high}) <b>{f}</b></div>""",
                                unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div class="result-card">{param}: <b>{val}</b></div>""", unsafe_allow_html=True)

        if st.session_state.unlocked["Blutbild"]:
            st.markdown("""<div class="result-card"><b>🩸 Differentialblutbild</b></div>""", unsafe_allow_html=True)
            diff = blood_diff[case]
            for param, val in diff.items():
                st.markdown(f"""<div class="result-card">{param}: <b>{val}</b></div>""", unsafe_allow_html=True)

        if st.session_state.unlocked["Mikrotests"]:
            mt = micro_tests[case]
            st.markdown(f"""<div class="result-card"><b>🧬 Mikrobiologie – Schnelltests</b><br>
            Gram: <b>{mt["Gram"]}</b><br>
            Katalase: <b>{mt["Katalase"]}</b><br>
            Koagulase: <b>{mt["Koagulase"]}</b><br>
            Hämolyse: <b>{mt["Hämolyse"]}</b>
            </div>""", unsafe_allow_html=True)

        st.write("---")
        st.subheader("🧾 Interpretation (Auto-Hinweise)")

        if st.session_state.unlocked.get("Blutbild"):
            for h in interpret_blood(blood_diff[case]):
                st.markdown(f"""<div class="hint-card">{h}</div>""", unsafe_allow_html=True)

        if st.session_state.unlocked.get("Mikrotests"):
            for h in interpret_micro(micro_tests[case]):
                st.markdown(f"""<div class="hint-card">{h}</div>""", unsafe_allow_html=True)

# -------------------------
# AGAR SCREEN leitet die Agarplatte, hier können die Spieler zwischen den verschiedenen Platten wechseln (COS / MAC / CNA) und die Ergebnisse sehen, die ihnen bei der Diagnose helfen können. Es gibt auch einen Zurück-Button, um zurück zum Labor zu gelangen.
# -------------------------
elif st.session_state.screen == "agar":
    case = st.session_state.case

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🧫 Agarplatten</h1>
        <p style="text-align:center;">Wähle eine Platte aus und beurteile das Wachstum.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_agar_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown("""
    <div class="path-card">
    🧪 <b>Plattenübersicht:</b> COS = Kochblut, MAC = MacConkey, CNA = grampositive Selektion
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
# hier werden die drei Platten als Karten dargestellt, die den Namen der Platte und ein Symbol anzeigen. Wenn die Spieler auf "COS öffnen", "MAC öffnen" oder "CNA öffnen" klicken, wird die entsprechende Platte ausgewählt und die Seite aktualisiert, um die Ergebnisse für diese Platte anzuzeigen.
    with col1:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">COS</div>
        """, unsafe_allow_html=True)
        if st.button("COS öffnen", key=f"plate_cos_{case}"):
            st.session_state.selected_plate = "COS"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">MAC</div>
        """, unsafe_allow_html=True)
        if st.button("MAC öffnen", key=f"plate_mac_{case}"):
            st.session_state.selected_plate = "MAC"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="plate-card">🧫</div>
        <div class="plate-label">CNA</div>
        """, unsafe_allow_html=True)
        if st.button("CNA öffnen", key=f"plate_cna_{case}"):
            st.session_state.selected_plate = "CNA"
            st.rerun()

    if st.session_state.selected_plate:
        plate = st.session_state.selected_plate
        result = agar_results[case][plate]

        st.markdown(f"""
        <div class="result-card">
        <h4>🔍 Ausgewählte Platte: {plate}</h4>
        {result}
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# MIKROSKOP SCREEN hier können die Spieler den mikroskopischen Eindruck der Probe sehen und danach die Gram-Färbung durchführen, indem sie die Schritte in der richtigen Reihenfolge auswählen. Es gibt auch einen Zurück-Button, um zurück zum Labor zu gelangen.
# -------------------------
elif st.session_state.screen == "mikroskop":
    case = st.session_state.case

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🔬 Mikroskop</h1>
        <p style="text-align:center;">Beobachte die Probe und führe danach die Gram-Färbung durch.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_mic_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown(f"""
    <div class="microscope-box">
        <span class="big-emoji">🔬</span>
        <h3>Mikroskopischer Eindruck</h3>
        <p>{microscope_info[case]["view"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎮 Gram-Färbung Mini-Spiel")
    st.write("Wähle die Schritte in der richtigen Reihenfolge:")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🟣</span>
            <div class="gram-step-title">Kristallviolett</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"cv_{case}"):
            st.session_state.gram_steps.append("Kristallviolett")
            st.rerun()

    with c2:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🧴</span>
            <div class="gram-step-title">Lugol</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"lugol_{case}"):
            st.session_state.gram_steps.append("Lugol")
            st.rerun()

    with c3:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">💧</span>
            <div class="gram-step-title">Alkohol</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"alk_{case}"):
            st.session_state.gram_steps.append("Alkohol")
            st.rerun()

    with c4:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🩷</span>
            <div class="gram-step-title">Safranin</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Wählen", key=f"saf_{case}"):
            st.session_state.gram_steps.append("Safranin")
            st.rerun()

    col_a, col_b = st.columns([3, 1])

    with col_a:
        st.markdown(f"""
        <div class="hint-card">
        <b>Deine Reihenfolge:</b> {" → ".join(st.session_state.gram_steps) if st.session_state.gram_steps else "Noch keine Schritte gewählt."}
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        if st.button("🔄 Reset", key=f"reset_gram_{case}"):
            reset_gram_game()
            st.rerun()

    if len(st.session_state.gram_steps) == 4 and st.session_state.gram_result is None:
        correct_order = ["Kristallviolett", "Lugol", "Alkohol", "Safranin"]

        if st.session_state.gram_steps == correct_order:
            st.session_state.gram_result = microscope_info[case]["gram_type"]
        else:
            st.session_state.gram_result = "Reihenfolge nicht korrekt"

    if st.session_state.gram_result:
        if st.session_state.gram_result == "Reihenfolge nicht korrekt":
            st.error("❌ Die Reihenfolge war nicht korrekt. Versuch es nochmals.")
        else:
            st.success(f"✅ Ergebnis der Gram-Färbung: {st.session_state.gram_result}")

# -------------------------
# BLUTBILD SCREEN
# -------------------------
elif st.session_state.screen == "blutbild":
    case = st.session_state.case
    diff = blood_diff[case]

    st.markdown("""
    <div class="screen-box">
        <h1 style="text-align:center;">🩸 Blutbild</h1>
        <p style="text-align:center;">Wähle einen Blutbild-Parameter aus und beurteile ihn.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("← Zurück zum Labor", key=f"back_from_blood_{case}"):
        st.session_state.screen = "lab"
        st.rerun()

    st.markdown("""
    <div class="path-card">
    🧪 <b>Hinweis:</b> Nicht nur der Wert selbst ist wichtig, sondern auch seine Bedeutung für die Diagnose.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    params = [
        "Leukozyten (G/L)",
        "Neutrophile (%)",
        "Lymphozyten (%)",
        "Eosinophile (%)"
    ]

    with c1:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🧫</span>
            <div class="gram-step-title">Leukozyten</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ansehen", key=f"blood_leuk_{case}"):
            st.session_state.selected_blood_param = "Leukozyten (G/L)"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🛡️</span>
            <div class="gram-step-title">Neutrophile</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ansehen", key=f"blood_neut_{case}"):
            st.session_state.selected_blood_param = "Neutrophile (%)"
            st.rerun()

    with c3:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🦠</span>
            <div class="gram-step-title">Lymphozyten</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ansehen", key=f"blood_lymph_{case}"):
            st.session_state.selected_blood_param = "Lymphozyten (%)"
            st.rerun()

    with c4:
        st.markdown("""
        <div class="gram-step-card">
            <span class="big-emoji">🐛</span>
            <div class="gram-step-title">Eosinophile</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ansehen", key=f"blood_eos_{case}"):
            st.session_state.selected_blood_param = "Eosinophile (%)"
            st.rerun()

    st.write("")

    if st.session_state.selected_blood_param:
        param = st.session_state.selected_blood_param
        value = diff[param]
        explanation = blood_explanations[param]
        low, high = REF_BLOOD_DIFF[param]
        flag_symbol = flag(value, low, high)

        st.markdown(f"""
        <div class="result-card">
        <h4>🔍 Ausgewählter Wert: {param}</h4>
        <b>Wert:</b> {value} <br>
        <b>Referenzbereich:</b> {low} – {high} <br>
        <b>Bewertung:</b> {flag_symbol}
        {explanation}
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("🧾 Interpretation")

    for h in interpret_blood(diff):
        st.markdown(f"""<div class="hint-card">{h}</div>""", unsafe_allow_html=True)