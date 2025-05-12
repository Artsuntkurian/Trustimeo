# 🕵️‍♂️ Deepfake Detector (Flask + ViT)

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

> ![Preview Screenshot](preview.png)  
> _Replace with your own screenshot image and rename to `preview.png`_

---

## 📁 Project Structure

```
deepfake-detector/
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
git clone https://github.com/your-username/deepfake-detector.git
cd deepfake-detector
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

- Email: deepfake@gmail.com
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [linkedin.com/in/artsuntkurian](https://linkedin.com/in/artsuntkurian)

---
