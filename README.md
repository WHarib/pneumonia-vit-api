---
title: Pneumonia ViT Classifier API
emoji: 🩺
colorFrom: blue
colorTo: green
sdk: static
sdk_version: "1.0.0"
app_file: app.py
pinned: false
---

# Pneumonia ViT Classifier (FastAPI)

This Space provides a RESTful API that accepts chest X-ray images and classifies them as **Normal** or **Pneumonia** using a Vision Transformer model.

### 🔗 Endpoints

- `POST /predict`: Upload an image to get:
  - `diagnosis` (Normal or Pneumonia)
  - `confidence` (0.00 to 1.00)

---