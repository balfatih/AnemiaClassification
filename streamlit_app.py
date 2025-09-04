import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

st.title('YSA Modeli ile Anemi Türlerinin Sınıflandırılması')

st.markdown(
    """
    ℹ️ Bu uygulama Fatih Bal tarafından *[Optimize Edilmiş Yapay Sinir Ağı Modeli](https://linkadresin.com)* 
    çalışması için geliştirilmiştir.
    """,
    unsafe_allow_html=True
)

# Modeli yükle
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("anemia_trained_model.keras")

model = load_model()


# Kullanıcılardan giriş alınıyor.
WBC = st.number_input("WBC", value=0.0)
LYMp = st.number_input("LYMp", value=0.0)
NEUTp = st.number_input("NEUTp", value=0.0)
LYMn = st.number_input("LYMn", value=0.0)
NEUTn = st.number_input("NEUTn", value=0.0)
RBC = st.number_input("RBC", value=0.0)
HGB = st.number_input("HGB", value=0.0)
HCT = st.number_input("HCT", value=0.0)
MCV = st.number_input("MCV", value=0.0)
MCH = st.number_input("MCH", value=0.0)
MCHC = st.number_input("MCHC", value=0.0)
PLT = st.number_input("PLT", value=0.0)
PDW = st.number_input("PDW", value=0.0)
PCT = st.number_input("PCT", value=0.0)


