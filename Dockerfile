# ─── Dockerfile ────────────────────────────────────────────────────────────
FROM python:3.10-slim

# Prevent interactive prompts during deps install
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files (model weights, app.py, etc.)
COPY . .

# Expose default HF port
EXPOSE 7860
# ---------- allow HF to write cache ----------
ENV TRANSFORMERS_CACHE=/code/hf_cache
RUN mkdir -p /code/hf_cache

# Launch FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
# ───────────────────────────────────────────────────────────────────────────
