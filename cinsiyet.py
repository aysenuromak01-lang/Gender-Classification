import streamlit as st
import numpy as np
import joblib

# Eğitilen Modeli Yükle
try:
    model = joblib.load("gender_classifier_model.pkl")
except:
    st.error("Model dosyası bulunamadı! Lütfen önce modeli eğitip kaydedin.")
    st.stop()

st.title("🧑‍🤝‍🧑 Fiziksel Özelliklere Göre Cinsiyet Sınıflandırması")
st.write("Aşağıdaki özellikleri doldurarak modelin cinsiyet tahminini görün.")

# İkili (Binary) Özellikler için Seçim Kutuları (Var=1, Yok=0)
st.subheader("🧬 Yapısal Özellikler")
long_hair = st.selectbox("Uzun Saç?", options=["Yok (Kısa)", "Var (Uzun)"])
long_hair_val = 1 if long_hair == "Var (Uzun)" else 0

nose_wide = st.selectbox("Geniş Burun Yapısı?", options=["Hayır", "Evet"])
nose_wide_val = 1 if nose_wide == "Evet" else 0

nose_long = st.selectbox("Uzun Burun Yapısı?", options=["Hayır", "Evet"])
nose_long_val = 1 if nose_long == "Evet" else 0

lips_thin = st.selectbox("İnce Dudak Yapısı?", options=["Hayır", "Evet"])
lips_thin_val = 1 if lips_thin == "Evet" else 0

distance_nose_to_lip_long = st.selectbox("Burun ile Dudak Arasındaki Mesafe Uzun mu?", options=["Hayır", "Evet"])
distance_nose_to_lip_val = 1 if distance_nose_to_lip_long == "Evet" else 0

# Sayısal Ölçüler (Cm cinsinden)
st.subheader("📐 Alın Ölçüleri")
forehead_width = st.slider("Alın Genişliği (cm)", 11.0, 16.0, 13.0, step=0.1)
forehead_height = st.slider("Alın Yüksekliği (cm)", 5.0, 7.0, 6.0, step=0.1)

# Tahmin Butonu
if st.button("Cinsiyeti Tahmin Et"):
    # Girdileri modelin veri setindeki orijinal sütun sırasına göre diziyoruz
    input_data = np.array([[long_hair_val, forehead_width, forehead_height, 
                            nose_wide_val, nose_long_val, lips_thin_val, distance_nose_to_lip_val]])
    
    # Tahmin gerçekleştirme
    prediction = model.predict(input_data)[0]
    
    # Sonucu ekrana basma (1=Male, 0=Female)
    if prediction == 1:
        st.success("🎯 Tahmin: **Erkek (Male)**")
    else:
        st.info("🎯 Tahmin: **Kadın (Female)**")
