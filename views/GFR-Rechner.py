import streamlit as st 
from functions.NierenCheck import calculate_gfr  #streamlit importieren hier 
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# Initialisierung des DataFrames für die Historie
if 'history' not in st.session_state:
    st.session_state['history'] = pd.DataFrame(columns=['Nr', 'Alter', 'Geschlecht', 'Kreatinin', 'GFR'])

st.title("🩺 Interaktiver GFR-Rechner (CKD-EPI)") #Titel wird do ahzeigt
st.write("Nieren-Check: Wie fit sind Ihre Filter?") #das isch sone untertitel und wird au in de App ahzeigt 

#ab do kann man sache ihgeh damit die funktion au funktioniert 
col1, col2 = st.columns(2)

with col1:
    kreatinin_input = st.number_input("Kreatinin im Serum (mg/dl)", min_value=0.1, max_value=15.0, value=1.0, step=0.1)
    alter = st.number_input("Alter des Patienten", min_value=18, max_value=120, value=50) #do sind min und max werte damit man nid alter 500 oder so ihgeh kann, nur realistischi

with col2:
    geschlecht = st.selectbox("Geschlecht", ["Weiblich", "Männlich"]) #kasch uswähle was in de dropdown sött sie 
    einheit = st.radio("Einheit wählen", ["mg/dl", "µmol/l"]) #jenach labor sind die ja immer anders

# Umrechnig für die einheite
kreatinin_calc = kreatinin_input
if einheit == "µmol/l":
    kreatinin_calc = kreatinin_input / 88.4

# Das zeigt das ergebnis ah
if st.button("GFR berechnen"):
    result = calculate_gfr(kreatinin_calc, alter, geschlecht)
    
    # Daten für die Tabelle und das Diagramm speichern
    new_entry = {
        'Nr': len(st.session_state['history']) + 1,
        'Alter': alter,
        'Geschlecht': geschlecht,
        'Kreatinin': f"{kreatinin_input} {einheit}",
        'GFR': round(result, 1)
    }
    # Hier werden die neuen Daten in den Session State geschrieben
    st.session_state['history'] = pd.concat([st.session_state['history'], pd.DataFrame([new_entry])], ignore_index=True)
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['history'], 'data.csv')  # Speichern der Historie auf dem Switch Drive
    # Farbe die typische rot, gelb, grün 
    if result >= 90:
        st.success(f"Ergebnis: {result:.1f} ml/min/1.73m² (Normal)")
        with st.expander("✅ Tipps für Ihre Nierengesundheit"):
            st.write("Ihre Werte sind im grünen Bereich. So halten Sie Ihre Nieren fit:")
            st.markdown("- **Flüssigkeit:** Trinken Sie ausreichend Wasser (1,5 - 2 Liter).")
            st.markdown("- **Bewegung:** Regelmäßiger Sport schützt die Gefäße.")
    elif result >= 60:
        st.warning(f"Ergebnis: {result:.1f} ml/min/1.73m² (Leichte Einschränkung)")
        with st.expander("⚠️ Was Sie jetzt tun können"):
            st.info("Ihre Nierenfunktion ist leicht vermindert. Das ist oft stabil, sollte aber beobachtet werden.")
            st.markdown("- **Blutdruck:** Regelmäßig kontrollieren (Ziel meist < 130/80 mmHg).")
            st.markdown("- **Vorsicht:** Meiden Sie nierenschädliche Schmerzmittel wie Ibuprofen oder Diclofenac.")
    else:
        st.error(f"Ergebnis: {result:.1f} ml/min/1.73m² (Moderater bis schwerer Nierenfunktionsverlust)")
        with st.expander("🚨 Wichtige nächste Schritte"):
            st.markdown("### **Suchen Sie bitte einen Arzt (Nephrologen) auf.**")
            st.write("Weitere Diagnostik ist notwendig:")
            st.markdown("- **Urin-Check:** Untersuchung auf Eiweiß (Albumin).")
            st.markdown("- **Medikamenten-Check:** Besprechen Sie alle Tabletten mit Ihrem Arzt.")

    st.info("💡 Ein Wert unter 60 über mehr als 3 Monate deutet auf eine chronische Nierenerkrankung hin.")

# --- Anzeige von Tabelle und Diagramm ---
if not st.session_state['history'].empty:
    st.divider()
    st.write("### 📊 Verlauf Ihrer GFR-Werte")
    
    # Das Diagramm: Es nimmt die GFR-Spalte aus deiner History
    # Wir setzen die 'Nr' als Index für die X-Achse
    chart_data = st.session_state['history'].set_index('Nr')['GFR']
    st.line_chart(chart_data)
    
    st.write("### 📝 Tabellarische Übersicht")
    st.dataframe(st.session_state['history'], hide_index=True)
    
    # Button zum Zurücksetzen
    if st.button("Verlauf löschen"):
        st.session_state['history'] = pd.DataFrame(columns=['Nr', 'Alter', 'Geschlecht', 'Kreatinin', 'GFR'])
        st.rerun()
