import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/GFR-Rechner.py", title="GFR-Rechner", icon=":material/info:")
pg_third = st.Page("views/Neue-App.py", title="Neue App", icon=":material/info:")

pg = st.navigation([pg_home, pg_second, pg_third])
pg.run()
