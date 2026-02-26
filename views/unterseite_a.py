import streamlit as st  #streamlit importieren hier 

st.title("🩺 Interaktiver GFR-Rechner (CKD-EPI)") #Titel wird do ahzeigt
st.write("Berechnen Sie die geschätzte glomeruläre Filtrationsrate basierend auf Laborwerten.") #das isch sone untertitel und wird au in de App ahzeigt 

#ab do kann man sache ihgeh damit die funktion au funktioniert 
col1, col2 = st.columns(2)

with col1:
    kreatinin = st.number_input("Kreatinin im Serum (mg/dl)", min_value=0.1, max_value=15.0, value=1.0, step=0.1)
    alter = st.number_input("Alter des Patienten", min_value=18, max_value=120, value=50) #do sind min und max werte damit man nid alter 500 oder so ihgeh kann, nur realistischi

with col2:
    geschlecht = st.selectbox("Geschlecht", ["Weiblich", "Männlich"])
    einheit = st.radio("Einheit wählen", ["mg/dl", "µmol/l"]) #jenach labor sind die ja immer anders

# Umrechnig für die einheite
if einheit == "µmol/l":
    kreatinin = kreatinin / 88.4

#Das isch unseri formle
def calculate_gfr(krea, age, sex):
    #do werde die faktore beobachtet und gändert will zb Fraue im schnitt weniger Muskelmasse hänt und somit weniger Kreatinin im Blut
    if sex == "Weiblich":
        kappa = 0.7
        alpha = -0.329
        gender_fix = 1.018
    else:
        kappa = 0.9
        alpha = -0.411
        gender_fix = 1.0

    gfr = 141 * min(krea/kappa, 1)**alpha * max(krea/kappa, 1)**-1.209 * 0.993**age * gender_fix
    return gfr

# Das zeigt das ergebnis ah 
if st.button("GFR berechnen"):
    result = calculate_gfr(kreatinin, alter, geschlecht)
    
    # Farbe die typische rot, gelb, grün 
    if result >= 90:
        st.success(f"Ergebnis: {result:.1f} ml/min/1.73m² (Normal)")
    elif result >= 60:
        st.warning(f"Ergebnis: {result:.1f} ml/min/1.73m² (Leichte Einschränkung)")
    else:
        st.error(f"Ergebnis: {result:.1f} ml/min/1.73m² (Moderater bis schwerer Nierenfunktionsverlust)")

    # Zusatzinfo
    st.info("💡 Ein Wert unter 60 über mehr als 3 Monate deutet auf eine chronische Nierenerkrankung hin.")
