FROM python:3.12-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=dependency -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3-debian13:nonroot

WORKDIR /app

COPY --from=builder /app/dependency /app/dependency

COPY --from=builder /app /app

ENV PYTHONPATH=/app/dependency

EXPOSE 5000

CMD ["-m", "gunicorn.app.wsgiapp", "-b", "0.0.0.0:5000", "main:app"]
