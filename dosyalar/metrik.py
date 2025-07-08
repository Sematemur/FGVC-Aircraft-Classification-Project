##metriklerin hesaplanması için kullanıldı
from datasets import load_dataset
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from modeltahmin import model_yukle
import torch
ds_val = load_dataset("Donghyun99/FGVC-Aircraft",split="val")
class CustomImageDataset(Dataset):
    def __init__(self, data_list, transform=None):
        
        self.data = data_list
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data[idx]['image']
        label = self.data[idx]['label']

        if self.transform:
            image = self.transform(image)

        return image, label
    

from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import transforms
import seaborn as sns
import matplotlib.pyplot as plt

transform = transforms.Compose([
    transforms.Resize((224, 224)),  
    transforms.ToTensor(),
])


val_dataset = CustomImageDataset(data_list=ds_val,transform=transform)
val_dataloader = DataLoader(val_dataset, batch_size=16, shuffle=False)

model = model_yukle()
model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for images, labels in val_dataloader:
        images = images
        labels = labels

        outputs = model(images)
        logits = outputs.logits  # Hugging Face modelleri böyle çalışır
        _, preds = torch.max(logits, 1)

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())
print(classification_report(all_labels, all_preds))
cm = confusion_matrix(all_labels, all_preds)
# Hugging Face dataset'ten sınıf isimleri
class_names = ds_val.features['label'].names

plt.figure(figsize=(35, 35))  # Eğer sınıf sayısı çoksa boyutu büyüt
sns.heatmap(cm, annot=False, fmt='d', cmap='Blues',
            xticklabels=class_names,
            yticklabels=class_names)

plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()




        