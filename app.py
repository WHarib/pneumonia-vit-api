from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch, io, os

app = FastAPI(
    title="Pneumonia ViT Classifier API",
    description="Vision Transformer for binary pneumonia classification",
    docs_url="/docs",
)

CLASS_NAMES = ["Normal", "Pneumonia"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── Model & processor ────────────────────────────────────────────────────
CACHE_DIR = "/tmp/hf_cache"            # always writable in HF Spaces
os.makedirs(CACHE_DIR, exist_ok=True)

try:
    # Load ViT model weights from the current directory
    model = (
        ViTForImageClassification
        .from_pretrained(".", local_files_only=True)
        .to(device)
        .eval()
    )

    # Load the image processor, caching files in /tmp
    processor = ViTImageProcessor.from_pretrained(
        "google/vit-base-patch16-224-in21k",
        cache_dir=CACHE_DIR,
    )

except Exception as e:
    raise RuntimeError(f"Model or processor loading failed: {e}")
# ─────────────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return {"status": "API running", "device": str(device)}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        image = image.resize((224, 224))

        inputs = processor(images=image, return_tensors="pt", padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=1)
            confidence = (
                probs[0][1].item() if probs[0][1] > probs[0][0] else probs[0][0].item()
            )
            predicted = logits.argmax(dim=1).item()
            label = CLASS_NAMES[predicted]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")

    return JSONResponse(
        {
            "diagnosis": label,
            "confidence": round(confidence, 4),
            "class_index": predicted,
        }
    )
