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

# Environment variables
ENV FLASK_SECRET = "floppabigcapysuper12secret14luckystrikered"

CMD ["gunicorn", "-c", "gunicorn.conf.py", "--bind", "0.0.0.0:8080", "app:app"]