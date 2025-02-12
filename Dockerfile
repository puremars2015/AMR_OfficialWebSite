FROM python:3.10.15-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 5050
CMD ["python", "app.py"]
