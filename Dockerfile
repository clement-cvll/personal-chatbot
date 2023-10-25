#syntax=docker/dockerfile:1

FROM python:3.11

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -U pip
RUN pip3 install torch -f https://download.pytorch.org/whl/cpu
RUN pip3 install -r requirements.txt

# Path: /app
COPY . .

# Run the application
EXPOSE 8080

# Environment variables
ENV FLASK_SECRET = "floppabigcapysuper12secret14luckystrikered"

CMD ["gunicorn", "-w", "2", "--bind", "0.0.0.0:8080", "app:app"]