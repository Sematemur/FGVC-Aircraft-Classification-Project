#!/bin/bash

# Backend'i arka planda başlat
cd /app/backend
python -m uvicorn api:app --host 0.0.0.0 --port 8000 &

# Frontend'i başlat
cd /app/frontend
streamlit run arayuz.py --server.port 8501 --server.address 0.0.0.0 &

# Her iki process'in çalışmasını bekle
wait