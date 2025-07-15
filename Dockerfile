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

# Launch FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
# ───────────────────────────────────────────────────────────────────────────
