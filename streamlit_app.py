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

# 3 sütun oluşturuluyor.
col1, col2, col3 = st.columns(3)

# Kullanıcılardan giriş alınıyor.

# 1. sütun
with col1:
    WBC = st.number_input("WBC", value=0.0)
    LYMp = st.number_input("LYMp", value=0.0)
    NEUTp = st.number_input("NEUTp", value=0.0)
    LYMn = st.number_input("LYMn", value=0.0)
    NEUTn = st.number_input("NEUTn", value=0.0)

# 2. sütun
with col2:
    RBC = st.number_input("RBC", value=0.0)
    HGB = st.number_input("HGB", value=0.0)
    HCT = st.number_input("HCT", value=0.0)
    MCV = st.number_input("MCV", value=0.0)
    MCH = st.number_input("MCH", value=0.0)

# 3. sütun
with col3:
    MCHC = st.number_input("MCHC", value=0.0)
    PLT = st.number_input("PLT", value=0.0)
    PDW = st.number_input("PDW", value=0.0)
    PCT = st.number_input("PCT", value=0.0)

st.write("Model input shape:", model.input_shape)


if st.button("Tahmin Et"):
    X = np.array([[float(WBC), float(LYMp), float(NEUTp), float(LYMn), float(NEUTn),
               float(RBC), float(HGB), float(HCT), float(MCV), float(MCH),
               float(MCHC), float(PLT), float(PDW), float(PCT)
                  ]])
    prediction = model.predict(X)
    st.write("📌 Tahmin Sonucu:", prediction)

