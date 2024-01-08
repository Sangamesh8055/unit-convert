# Dockerfile
FROM python

WORKDIR /app

COPY unit_converter.py .

CMD ["python", "unit_converter.py"]

