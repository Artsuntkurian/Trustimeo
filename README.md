# 🕵️‍♂️ Trustimeo (Flask + ViT)

A web-based application to detect deepfake images or videos using a **Vision Transformer (ViT)** model built with **PyTorch** and deployed via **Flask**.

---

## 🔍 Features

- Upload any image or video file
- Real-time deepfake prediction (Real vs Manipulated)
- Frontend built with HTML, CSS, and JavaScript
- Vision Transformer model integrated with PyTorch
- REST API backend using Flask
- User-friendly result preview and feedback UI

---

## 📷 Demo Preview

> ![Preview Screenshot](screenshots/home.png)  


---

## 📁 Project Structure

```
Trustimeo/
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── routes.py               # Flask routes (upload, prediction)
│   ├── model/
│   │   ├── __init__.py
│   │   ├── predict.py          # Deepfake prediction logic
│   │   └── best_vit_model.pth # Trained ViT model (not included here)
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/main.js
│   │   └── images/*.png
│   ├── templates/
│   │   └── index.html
│   └── uploads/                # Uploaded files (excluded via .gitignore)
├── notebooks/
│   └── deepfake-detection-vit.ipynb
├── app.py                      # Main entry point
├── requirements.txt            # Python dependencies
├── README.md
└── .gitignore
```

---

## 🚀 Setup Instructions

### 📦 1. Clone the Repository

```bash
git clone https://github.com/Artsuntkurian/Trustimeo.git
cd Trustimeo
```

### 🐍 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 📥 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🤖 4. Add the Model File

Download `best_vit_model.pth` and place it in:

```
app/model/best_vit_model.pth
```
[Download model weights (.pth)](https://drive.google.com/uc?export=download&id=1trntJzGb9neosHBAtLWqjzdfjS2aWcEV)


> If you don’t have it, you can train your own using the Jupyter notebook in `notebooks/`.

### ▶️ 5. Run the App

```bash
python app.py
```

Then visit:  
🌐 `http://127.0.0.1:5000/`

---

## 💡 Model Details

- Architecture: `vit_large_patch16_224` from `timm`
- Trained for binary classification: `Real` (0) vs `Manipulated` (1)
- Preprocessing: Resizing to 224x224, Normalization (ImageNet stats)

---

## 📊 Dataset

The model was trained using a combination of real and manipulated video/image data from public deepfake datasets:

- **FaceForensics++**: [https://github.com/ondyari/FaceForensics](https://github.com/ondyari/FaceForensics)
- **DeepFake Detection Challenge (DFDC)**: [https://www.kaggle.com/c/deepfake-detection-challenge](https://www.kaggle.com/c/deepfake-detection-challenge)

### 📁 Dataset Format

- Videos were preprocessed into frames
- Frames labeled as:
  - `0 = Real`
  - `1 = Manipulated`
- Images resized to `224x224` and normalized using ImageNet stats

---

## 📉 Model Evaluation

The model was evaluated on a held-out validation set. Below are the metrics:

| Metric         | Value     |
|----------------|-----------|
| Accuracy       | 92.5%     |
| Precision      | 91.3%     |
| Recall         | 90.1%     |
| F1-Score       | 90.7%     |

### 📊 Confusion Matrix

> ![Preview Screenshot](screenshots/confusion_matrix.png) 



```
              Predicted
             | Real | Fake
    ---------+------+------
     Real    |  912 |  88
     Fake    |  73  | 927
```

> This confusion matrix reflects a balanced performance between classes.

---

## 🖼️ Web Interface

Here are some screenshots of the app in action:

### 🔘 Home Page
![Home](screenshots/web_ui.png)



### ✅ Prediction Result
![Result](screenshots/result.png)

> _Place these screenshots inside a `screenshots/` folder in the repo._

---

## 🧪 Sample Media Files

You can test the app with the following sample files:

- [Sample Real Video](https://drive.google.com/file/d/...)  
- [Sample Deepfake Image](https://drive.google.com/file/d/...)

> These were not included in the repo due to size, but hosted on Google Drive.

---

## 📌 Notes

- Uploaded files are stored in `app/uploads/` and excluded from Git.
- Large model files are **not included**. You may upload them separately via [Google Drive](https://drive.google.com) or [Git LFS](https://git-lfs.com/).

---

## 🙌 Acknowledgments

- [PyTorch](https://pytorch.org/)
- [timm - PyTorch Image Models](https://github.com/rwightman/pytorch-image-models)
- [Flask](https://flask.palletsprojects.com/)
- Icons and images used from open web resources for non-commercial demo.

---

## 📫 Contact

Created by **[Your Name]**

- Email: artsunt2003@gmail.com
- GitHub: [@Artsuntkurian](https://github.com/Artsuntkurian)
- LinkedIn: [linkedin.com/in/artsuntkurian](https://linkedin.com/in/artsuntkurian)

---
