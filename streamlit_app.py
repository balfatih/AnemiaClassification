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
wbc = st.number_input("WBC", value=0.0)
LYMp = st.number_input("LYMp", value=0.0)
NEUTp = st.number_input("NEUTp", value=0.0)
