# 🌿 Plant Dashboard（プラントダッシュボード）

Raspberry Pi で収集した環境センサーデータ（温度・湿度・土壌水分など）を、Fly.io 上のクラウドで可視化する軽量なWebダッシュボードです。

## 🔧 特徴

- DHT11 / SEN0193センサを用いたRaspberry Piでのデータ取得
- SQLiteへの記録と `.db` ファイルのHTTPアップロード
- Bottle（Python）による軽量Webダッシュボード
- Fly.ioへのDockerデプロイ、バックアップ保存機能付き

## 🚀 システム構成図

```
[ Raspberry Pi ]
   ↓  (cron + upload_db.py)
[ Fly.io Web API (/upload) ]
   ↓
[ Fly.io上のSQLite（バックアップ付き）]
   ↓
[ https://plant-dashboard.fly.dev/ でダッシュボード表示 ]
```

## 🛠 必要環境

- Python 3.10 以上
- Bottle ライブラリ
- Fly.io CLI
- Docker

## 📁 ディレクトリ構成

```
project/
├── dashboard3.py           # Webアプリ本体
├── upload_db.py            # Raspberry Pi用アップロードスクリプト
├── Dockerfile              # コンテナ設定
├── requirements.txt
├── sensor_data.db          # SQLiteデータベース（.gitignore対象）
└── .gitignore
```

## 📦 デプロイ手順（概要）

1. Fly.io CLI をインストール
2. `flyctl launch` で初回デプロイ
3. `flyctl deploy` で更新反映
4. Raspberry Pi側で `upload_db.py` をcron登録して定期送信

## 📜 ライセンス

MITライセンス