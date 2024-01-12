import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Davide")
    content ="""
    Ciao, sono Davide, sto seguendo un corso di python e sono molto appassionato di 
    programmazione, non veo l'ora di scoprire cosa altro potrò creare!
    """
    st.info(content)

content2 = """Qui sotto trovi tutte le applicazioni che ho creato, sentiti pure libero di 
conttattarmi dalla sezione dedicata!"""
st.write(content2)
