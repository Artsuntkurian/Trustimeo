import torch
from torchvision import transforms
from PIL import Image
import cv2
import timm

def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    model = timm.create_model('vit_large_patch16_224', pretrained=False, num_classes=2)
    model.load_state_dict(torch.load('app/model/best_vit_model.pth', map_location=device))
    model.to(device)
    model.eval()
    return model, transform, device

def predict_video(video_path, model, transform, device):
    cap = cv2.VideoCapture(video_path)
    real_count, manipulated_count = 0, 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)

        if predicted.item() == 0:
            real_count += 1
        else:
            manipulated_count += 1

    cap.release()
    return "Real" if real_count > manipulated_count else "Manipulated"
