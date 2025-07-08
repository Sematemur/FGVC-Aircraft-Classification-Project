  
import streamlit as st
from PIL import Image
import requests

st.title("Uçak Sınıflandırma Arayüzü")
st.write("Bu arayüz, yüklediğiniz uçak resimlerini sınıflandırmak için tasarlanmıştır. ViT modeli fine-tune edilmiştir.")

# Resim yükleme alanı
def resimalma():
    uploaded_file = st.file_uploader("Bir resim yükleyin", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        return image, uploaded_file
    return None, None

image, uploaded_file = resimalma()

if image is not None:
    st.image(image, caption="Yüklenen Resim")
    
    st.write("Tahmin yapılıyor...")
    
    # Dosya pointer'ını başa al ve byte olarak oku
    uploaded_file.seek(0)  # Dosya pointer'ını başa al
    image_bytes = uploaded_file.read()
    files = {"file": ("image.jpg", image_bytes, "image/jpeg")}
    
    try:
        res = requests.post("http://localhost:8000/tahminetme/", files=files)
        if res.status_code == 200:
            result = res.json()["prediction"]
            st.text_area("Tahmin Sonucu", result, height=100)
        else:
            st.error("API tahmin sırasında bir hata döndürdü.")
    except Exception as e:
        st.error(f"Sunucuya istek gönderilirken hata oluştu: {e}")
else:
    st.write("Lütfen bir resim yükleyin.")
