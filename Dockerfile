FROM python:3.11

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Path: /app
COPY . .

# Run the application
EXPOSE 8080

CMD ["gunicorn", "-c", "gunicorn.conf.py", "--bind", "0.0.0.0:8080", "app:app"]