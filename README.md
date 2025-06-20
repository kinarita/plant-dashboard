# 🌿 Plant Dashboard

A lightweight cloud-based dashboard to visualize environmental sensor data (e.g., temperature, humidity, soil moisture) collected from a Raspberry Pi.

## 🔧 Features

- Raspberry Pi with DHT11/SEN0193 sensor logging to SQLite
- HTTP upload of `sensor_data.db` to Fly.io
- Web dashboard built with Python Bottle
- Automatic backup before overwrite (`sensor_data_backup.db`)
- Deployed using Docker on Fly.io with volume mounting

## 🚀 Architecture

```
[ Raspberry Pi ]
   ↓  (cron + upload_db.py)
[ Fly.io Web API (/upload) ]
   ↓
[ SQLite on Fly.io (with backup) ]
   ↓
[ Bottle dashboard on https://plant-dashboard.fly.dev/ ]
```

## 🛠 Requirements

- Python 3.10+
- Bottle
- Fly.io CLI
- Docker

## 📁 Directory Structure

```
project/
├── dashboard3.py           # Bottle web app
├── upload_db.py            # Raspberry Pi side uploader
├── Dockerfile              # Deployment container config
├── requirements.txt
├── sensor_data.db          # SQLite database (ignored by .gitignore)
└── .gitignore
```

## 📦 Deployment

1. Install `flyctl`
2. `flyctl launch`
3. Push updates with `flyctl deploy`
4. Raspberry Pi posts `.db` via `upload_db.py`

## 📜 License

MIT License