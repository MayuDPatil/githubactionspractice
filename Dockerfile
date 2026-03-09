FROM python:3.12-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=dependency -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /app/dependency /app/dependency

COPY --from=builder /app /app

ENV pythonpath = /app/dependency

CMD ["app.py"]
