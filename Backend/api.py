from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from modeltahmin import tahminetme

app = FastAPI()

@app.post("/tahminetme/")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    
    # PIL ile görseli aç
    try:
        image = Image.open(io.BytesIO(contents))
        image = image.convert("RGB")  # Opsiyonel ama çoğu model RGB ister
    except Exception as e:
        return {"error": f"Görsel açılamadı: {str(e)}"}
    
    # Görseli model fonksiyonuna gönder
    result = tahminetme(image)
    
    return {"prediction": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)