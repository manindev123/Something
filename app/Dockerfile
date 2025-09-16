FROM python:3.11-slim AS builder
WORKDIR /install
COPY app/requirements.txt .
RUN pip install --prefix=/install/deps --no-cache-dir -r requirements.txt
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install/deps /usr/local
COPY . .
ENV PORT=8080
EXPOSE 8080
CMD ["python", "app.py"]
