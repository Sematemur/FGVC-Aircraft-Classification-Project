from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
class_names =  ('MD-11', 'BAE-125', 'C-130', 'DC-3', 'A300', 'SR-20', 'MD-80', 'DC-8',
          'Falcon 2000', 'Boeing 757', 'Tu-134', 'Boeing 727', 'DR-400', 'Saab 2000',
          'Spitfire', 'Il-76', 'ATR-42', 'Beechcraft 1900', 'DC-9', 'Embraer ERJ 145',
          'Cessna Citation', 'A340', 'CRJ-200', 'Boeing 767', 'Tu-154', 'An-12',
          'Boeing 747', 'EMB-120', 'Cessna 172', 'Fokker 50', 'Boeing 737',
          'Embraer Legacy 600', 'BAE 146', 'Metroliner', 'Fokker 70', 'Yak-42',
          'Saab 340', 'C-47', 'Global Express', 'Boeing 777', 'Cessna 208', 'F-16',
          'DC-6', 'CRJ-700', 'F/A-18', 'Challenger 600', 'PA-28', 'Hawk T1', 'DH-82',
          'A310', 'ATR-72', 'DHC-6', 'King Air', 'Boeing 707', 'A330', 'DHC-1',
          'Fokker 100', 'L-1011', 'Dash 8', 'A380', 'Embraer E-Jet',
          'Eurofighter Typhoon', 'MD-90', 'Boeing 717', 'Gulfstream', 'DC-10',
          'Tornado', 'Dornier 328', 'Falcon 900', 'A320') 

# Model ve işlemciyi yükle
image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
# Load model directly

processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
model = AutoModelForImageClassification.from_pretrained("google/vit-base-patch16-224")
# Sadece ağırlıkları yükle
model.load_state_dict(torch.load("best_model.pth", weights_only=True))
model.eval()
def tahminetme(image_path):
  
    # Eğer dosya yolu verilmişse görseli yükle
    if isinstance(image_path, str):
        image = Image.open(image_path).convert('RGB')
    else:
        image = image_path
    
    # Görseli işle
    inputs = image_processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(pixel_values=inputs['pixel_values'])
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    
    return class_names[predicted_class]

def model_yukle():
    return model
