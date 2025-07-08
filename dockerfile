FROM python:3.9-slim
WORKDIR /app

# Birleştirilmiş requirements'ı yükle
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Backend dosyalarını kopyala
COPY Backend/ ./backend/

# Frontend dosyalarını kopyala
COPY dosyalar/ ./frontend/

# Gerekli portları aç
EXPOSE 8000 8501

# Startup script oluştur
COPY start.sh ./
RUN chmod +x start.sh

CMD ["./start.sh"]