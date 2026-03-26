FROM python:3.13-slim

WORKDIR /app

# Install uv for fast dependency management
RUN pip install uv

# Copy dependency files first (for Docker layer caching)
COPY pyproject.toml uv.lock* requirements.txt ./

# Install dependencies
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY app/ app/
COPY templates/ templates/
COPY assets/ assets/
COPY run.py ./

# Create outputs directory
RUN mkdir -p outputs

# Expose port
EXPOSE 9000

# Default: run the API server
# Override with CMD ["python", "run.py"] for one-shot CLI generation
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
