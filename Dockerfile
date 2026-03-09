FROM python:3.12-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=dependency -r requirements.txt

COPY . .

FROM grcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /app/dependency /app/dependency

COPY /app /app

ENV pythonpath = /app/dependency

CMD ["app.py"]