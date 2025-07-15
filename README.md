# Pneumonia ViT Classifier (FastAPI)

This API takes a chest X-ray image and returns whether it's classified as "Normal" or "Pneumonia" using a Vision Transformer.

## Endpoints

- `POST /predict` – Upload a PNG/JPEG chest X-ray and get:
  - Diagnosis label
  - Confidence score

## How to test

```bash
curl -X POST "https://hf.space/embed/YOUR_USERNAME/YOUR_SPACE_NAME/predict" \
  -F "file=@your_xray.png"
yaml
Copy
Edit

---

## 🟢 What to Upload to Your Space

Upload these **5 files** directly in your Space's root (no folders):

- `app.py` ✅ *(code above)*
- `requirements.txt` ✅ *(code above)*
- `config.json` ✅ *(from sukhmani1303’s Space)*
- `pytorch_model.bin` ✅ *(from sukhmani1303’s Space)*
- *(optional)* `README.md`

---

### 🚀 When you deploy:
- Hugging Face will run:  
  ```bash
  uvicorn app:app --host 0.0.0.0 --port 7860