# ✈️ Uçak Sınıflandırma Projesi
Bu projede HuggingFaceM4/FGVC-Aircraft [veriseti](https://huggingface.co/datasets/HuggingFaceM4/FGVC-Aircraft) ViT modelinin finetune edilmesi amacıyla kullanıldı. Verisetinde 70 adet uçak sınıfı bulunmaktadır.  

## 🚀 Özellikler

- ✅ Transformer tabanlı sınıflandırma
- ✅ Kolay arayüz entegrasyonu
- ✅ FastAPI ile REST API servisi
- ✅ Docker ile container haline getirilmiştir.
## Dockerhubtan projeyi çekerek local olarak kullanmak için sırası ile aşağıdakileri yapabilirsiniz.
  1)  Terminalinizi açın. 2. ve 3. satırlarda belirtilen kodları commandları yazın.
- 2)  docker pull sematemur/plane_classification_project:latest 
  3)  docker run  -p 8501:8501 -p 8000:8000 sematemur/plane_classification_project:latest
  4)  Kullandığınız taracıya http://localhost:8501/ yazarak projenin arayüzüne erişebilirsiniz.
  5)  Not: API bölümü biraz yavaş yüklendiği için arayüzden kısa bir süre sonra gelecektir. İsterseniz docker desktop üzerinden veya terminalden uvicorn mesajını takip edebilirsiniz.

# Arayüz
![image](https://github.com/user-attachments/assets/ef213b37-00df-48f9-b6cd-531212d669a4)
##  ViT Model Değerlendirme Sonuçları
<img width="378" height="82" alt="image" src="https://github.com/user-attachments/assets/96b1f7cd-fe55-45d3-971a-70833707606b" />


