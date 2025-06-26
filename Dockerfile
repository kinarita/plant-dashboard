FROM python:3.11-slim

WORKDIR /app
COPY . .

# sensor_data.db をイメージ内にコピー（initスクリプトで移動）
COPY sensor_data.db /app/init/sensor_data.db
COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "dashboard3.py"]
